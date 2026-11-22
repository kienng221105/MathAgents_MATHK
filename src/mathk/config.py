"""Load and validate the Foundation's non-secret configuration."""

import os
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, ValidationError
import yaml


class ConfigurationError(ValueError):
    """Configuration could not be loaded or validated."""


class AppConfig(BaseModel):
    """Foundation settings; example budgets are not production limits."""

    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)

    model: str = Field(strict=True, min_length=1, pattern=r"^\S(?:.*\S)?$")
    timeout_seconds: float = Field(strict=True, gt=0)
    max_llm_calls: int = Field(strict=True, gt=0)
    allow_fallback: bool = Field(strict=True)


_ENV_FIELDS = {
    "MATHK_MODEL": "model",
    "MATHK_TIMEOUT_SECONDS": "timeout_seconds",
    "MATHK_MAX_LLM_CALLS": "max_llm_calls",
    "MATHK_ALLOW_FALLBACK": "allow_fallback",
}


def load_config(
    path: str | Path,
    *,
    overrides: Mapping[str, Any] | None = None,
) -> AppConfig:
    """Load YAML, then apply environment and explicit non-secret overrides."""
    try:
        with Path(path).open(encoding="utf-8") as config_file:
            data = yaml.safe_load(config_file)
    except (OSError, UnicodeError, yaml.YAMLError):
        raise ConfigurationError("Cannot read a valid YAML configuration file") from None

    if not isinstance(data, dict):
        raise ConfigurationError("Configuration must be a YAML mapping")

    for env_name, field in _ENV_FIELDS.items():
        if overrides is not None and field in overrides:
            continue
        if env_name in os.environ:
            value = os.environ[env_name]
            if field != "model":
                try:
                    value = yaml.safe_load(value)
                except yaml.YAMLError:
                    raise ConfigurationError(f"Invalid value for {field}") from None
            data[field] = value

    if overrides is not None:
        data.update(overrides)

    try:
        return AppConfig.model_validate(data)
    except ValidationError as exc:
        fields = AppConfig.model_fields
        messages = []
        for error in exc.errors(include_input=False, include_url=False):
            location = error["loc"]
            field = location[0] if location and location[0] in fields else None
            if field is None:
                messages.append("unknown configuration field")
            else:
                messages.append(f"{field}: {error['msg']}")
        raise ConfigurationError("Invalid configuration: " + "; ".join(messages)) from None
