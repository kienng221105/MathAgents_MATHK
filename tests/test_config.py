from pathlib import Path

import pytest

from mathk.config import AppConfig, ConfigurationError, load_config


@pytest.fixture(autouse=True)
def clear_config_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in (
        "MATHK_MODEL",
        "MATHK_TIMEOUT_SECONDS",
        "MATHK_MAX_LLM_CALLS",
        "MATHK_ALLOW_FALLBACK",
    ):
        monkeypatch.delenv(name, raising=False)


@pytest.fixture
def config_file(tmp_path: Path) -> Path:
    path = tmp_path / "config.yaml"
    path.write_text(
        "model: example-model\ntimeout_seconds: 30\n"
        "max_llm_calls: 4\nallow_fallback: false\n",
        encoding="utf-8",
    )
    return path


def test_default_yaml_is_valid() -> None:
    config = load_config(Path(__file__).resolve().parents[1] / "configs/default.yaml")
    assert isinstance(config, AppConfig)
    assert config.model == "example-model"
    assert config.timeout_seconds == 30
    assert config.max_llm_calls == 4
    assert config.allow_fallback is False


def test_environment_overrides_yaml_and_explicit_overrides_win(
    config_file: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("MATHK_MODEL", "another-model")
    monkeypatch.setenv("MATHK_TIMEOUT_SECONDS", "12.5")
    monkeypatch.setenv("MATHK_MAX_LLM_CALLS", "8")
    monkeypatch.setenv("MATHK_ALLOW_FALLBACK", "true")

    config = load_config(config_file, overrides={"timeout_seconds": 2})

    assert config.model == "another-model"
    assert config.timeout_seconds == 2
    assert config.max_llm_calls == 8
    assert config.allow_fallback is True


def test_explicit_override_wins_over_malformed_environment(
    config_file: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("MATHK_TIMEOUT_SECONDS", "[")
    assert load_config(config_file, overrides={"timeout_seconds": 2}).timeout_seconds == 2


def test_malformed_environment_is_rejected_without_echoing_input(
    config_file: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    private_marker = "[private-value-for-testing"
    monkeypatch.setenv("MATHK_TIMEOUT_SECONDS", private_marker)
    with pytest.raises(ConfigurationError) as error:
        load_config(config_file)
    assert "timeout_seconds" in str(error.value)
    assert private_marker not in str(error.value)


@pytest.mark.parametrize(
    ("overrides", "field"),
    [
        ({"model": ""}, "model"),
        ({"timeout_seconds": 0}, "timeout_seconds"),
        ({"timeout_seconds": float("inf")}, "timeout_seconds"),
        ({"max_llm_calls": -1}, "max_llm_calls"),
        ({"max_llm_calls": True}, "max_llm_calls"),
        ({"max_llm_calls": "4"}, "max_llm_calls"),
        ({"allow_fallback": "false"}, "allow_fallback"),
    ],
)
def test_invalid_values_are_rejected(
    config_file: Path, overrides: dict[str, object], field: str
) -> None:
    with pytest.raises(ConfigurationError, match=field):
        load_config(config_file, overrides=overrides)


def test_missing_required_field_is_reported(config_file: Path) -> None:
    config_file.write_text("model: example-model\n", encoding="utf-8")
    with pytest.raises(ConfigurationError, match="timeout_seconds"):
        load_config(config_file)


@pytest.mark.parametrize(
    ("original", "replacement", "field"),
    [
        ("timeout_seconds: 30", "timeout_seconds: -1", "timeout_seconds"),
        ("max_llm_calls: 4", 'max_llm_calls: "4"', "max_llm_calls"),
        ("allow_fallback: false", 'allow_fallback: "false"', "allow_fallback"),
    ],
)
def test_invalid_yaml_field_values_are_rejected(
    config_file: Path, original: str, replacement: str, field: str
) -> None:
    content = config_file.read_text(encoding="utf-8").replace(original, replacement)
    config_file.write_text(content, encoding="utf-8")
    with pytest.raises(ConfigurationError, match=field):
        load_config(config_file)


def test_invalid_environment_value_is_rejected_without_echoing_input(
    config_file: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    private_marker = "private-value-for-testing"
    monkeypatch.setenv("MATHK_MAX_LLM_CALLS", private_marker)
    with pytest.raises(ConfigurationError) as error:
        load_config(config_file)
    assert "max_llm_calls" in str(error.value)
    assert private_marker not in str(error.value)


@pytest.mark.parametrize("contents", ["[", "- list\n- not-a-mapping", ""])
def test_invalid_yaml_or_non_mapping_is_rejected(
    config_file: Path, contents: str
) -> None:
    config_file.write_text(contents, encoding="utf-8")
    with pytest.raises(ConfigurationError):
        load_config(config_file)


def test_unknown_fields_are_rejected_without_echoing_key_or_value(
    config_file: Path,
) -> None:
    private_marker = "private-value-for-testing"
    with pytest.raises(ConfigurationError) as error:
        load_config(config_file, overrides={private_marker: private_marker})
    assert "unknown configuration field" in str(error.value)
    assert private_marker not in str(error.value)


def test_missing_file_is_reported_without_echoing_path(tmp_path: Path) -> None:
    with pytest.raises(ConfigurationError) as error:
        load_config(tmp_path / "private-value-for-testing")
    assert "private-value-for-testing" not in str(error.value)


def test_unrelated_secret_environment_variable_is_not_loaded(
    config_file: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    private_marker = "private-value-for-testing"
    monkeypatch.setenv("MATHK_API_KEY", private_marker)
    config = load_config(config_file)
    assert private_marker not in repr(config)
    assert private_marker not in str(config.model_dump())
