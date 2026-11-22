"""Exercise the lab contracts and offline mock."""

import pytest
from pydantic import ValidationError

import demo
from demo import Message, MockClient, Request, Response, Usage, measure_call


@pytest.fixture
def sample_request() -> Request:
    return Request(
        model="example-model",
        messages=[Message(role="user", content="Hello")],
        temperature=0.2,
        max_output_tokens=16,
    )


@pytest.mark.parametrize(
    "changes",
    [
        {"model": ""},
        {"messages": []},
        {"messages": [{"role": "unknown", "content": "Hello"}]},
        {"temperature": 2.1},
        {"temperature": float("nan")},
        {"max_output_tokens": 0},
        {"max_output_tokens": "16"},
    ],
)
def test_invalid_requests_are_rejected(
    sample_request: Request, changes: dict[str, object]
) -> None:
    data = sample_request.model_dump()
    data.update(changes)
    with pytest.raises(ValidationError):
        Request.model_validate(data)


def test_missing_request_field_is_rejected(sample_request: Request) -> None:
    data = sample_request.model_dump(exclude={"model"})
    with pytest.raises(ValidationError):
        Request.model_validate(data)


@pytest.mark.parametrize(
    "changes",
    [
        {"model": ""},
        {"content": ""},
        {"finish_reason": ""},
        {"usage": {"input_tokens": -1, "output_tokens": 2, "total_tokens": 1}},
        {"usage": {"input_tokens": 1, "output_tokens": "2", "total_tokens": 3}},
    ],
)
def test_invalid_responses_are_rejected(changes: dict[str, object]) -> None:
    data = {"model": "mock", "content": "example", "finish_reason": "stop"}
    data.update(changes)
    with pytest.raises(ValidationError):
        Response.model_validate(data)


def test_mock_is_deterministic_and_usage_can_be_missing(sample_request: Request) -> None:
    client = MockClient()
    first = client.generate(sample_request)
    assert first == client.generate(sample_request)
    other_request = Request(
        model="other-model",
        messages=[Message(role="user", content="A different prompt")],
        temperature=1.0,
        max_output_tokens=10,
    )
    assert first == client.generate(other_request)
    assert first.model == "mock-model-v1"
    assert first.content == "Example response from the offline mock."
    assert first.finish_reason == "stop"
    assert first.usage is None


def test_response_missing_usage_remains_unknown() -> None:
    response = Response(model="mock", content="example", finish_reason="stop")
    assert response.usage is None


def test_mock_can_return_explicit_simulated_usage(sample_request: Request) -> None:
    usage = Usage(input_tokens=12, output_tokens=8, total_tokens=20)
    response = MockClient(usage).generate(sample_request)
    assert response.usage == usage


def test_measure_call_uses_elapsed_monotonic_time(
    sample_request: Request, monkeypatch: pytest.MonkeyPatch
) -> None:
    readings = iter((100.0, 100.25))
    monkeypatch.setattr(demo, "perf_counter", lambda: next(readings))
    response, latency_ms = measure_call(MockClient(), sample_request)
    assert response.usage is None
    assert latency_ms == 250.0


def test_demo_labels_missing_simulated_and_measured_values(
    capsys: pytest.CaptureFixture[str],
) -> None:
    demo.main()
    output = capsys.readouterr().out
    assert "usage: unavailable (not zero; no token count inferred)" in output
    assert "usage (simulated fixture, not actual tokens)" in output
    assert "local mock-call latency (measured)" in output
    assert "mock-model-v1" in output
    assert "finish_reason: stop" in output
