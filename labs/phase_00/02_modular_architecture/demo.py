"""Run two implementations through the same caller."""

from collections.abc import Callable

from formatter import concise, friendly


def show(name: str, formatter: Callable[[str], str]) -> None:
    print(formatter(name))


if __name__ == "__main__":
    show("MATHK", friendly)
    show("MATHK", concise)
