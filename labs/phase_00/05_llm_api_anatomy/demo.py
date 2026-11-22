"""Offline LLM API anatomy exercise; no network or credentials are used."""

from time import perf_counter
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Message(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")

    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=1)


class Request(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", allow_inf_nan=False)

    model: str = Field(min_length=1, pattern=r"^\S(?:.*\S)?$")
    messages: list[Message] = Field(min_length=1)
    temperature: float = Field(ge=0, le=2)
    max_output_tokens: int = Field(gt=0)


class Usage(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")

    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)
    total_tokens: int = Field(ge=0)


class Response(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")

    model: str = Field(min_length=1, pattern=r"^\S(?:.*\S)?$")
    content: str = Field(min_length=1)
    finish_reason: str = Field(min_length=1)
    usage: Usage | None = None


class MockClient:
    """Return fixed example data, independent of the request."""

    def __init__(self, usage: Usage | None = None) -> None:
        self.usage = usage

    def generate(self, request: Request) -> Response:
        return Response(
            model="mock-model-v1",
            content="Example response from the offline mock.",
            finish_reason="stop",
            usage=self.usage,
        )


def measure_call(client: MockClient, request: Request) -> tuple[Response, float]:
    """Measure local elapsed time around the mock call in milliseconds."""
    started = perf_counter()
    response = client.generate(request)
    return response, (perf_counter() - started) * 1000


def main() -> None:
    request = Request(
        model="requested-example-model",
        messages=[Message(role="user", content="Explain what a token is.")],
        temperature=0.2,
        max_output_tokens=64,
    )
    print("Request (example):", request.model_dump())

    fixtures = (
        ("missing", None),
        ("simulated", Usage(input_tokens=12, output_tokens=8, total_tokens=20)),
    )
    for label, usage in fixtures:
        response, elapsed_ms = measure_call(MockClient(usage), request)
        print(f"\nResponse (mock; usage {label}):")
        print("model:", response.model)
        print("content:", response.content)
        print("finish_reason:", response.finish_reason)
        if response.usage is None:
            print("usage: unavailable (not zero; no token count inferred)")
        else:
            print("usage (simulated fixture, not actual tokens):", response.usage.model_dump())
        print(f"local mock-call latency (measured): {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
