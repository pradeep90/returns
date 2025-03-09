from returns.contrib.hypothesis.laws import lawful_interfaces
from returns.result import Result

from .test_laws import (
    test_custom_interface_with_laws,
    test_custom_type_applicative,
)


def test_lawful_interfaces__container_defined_in_returns() -> None:
    """Check that it returns all interfaces for a container in `returns`."""
    result = lawful_interfaces(Result)

    assert sorted(str(interface) for interface in result) == [
        "<class 'returns.interfaces.altable.AltableN'>",
        "<class 'returns.interfaces.applicative.ApplicativeN'>",
        "<class 'returns.interfaces.bimappable.BiMappableN'>",
        "<class 'returns.interfaces.bindable.BindableN'>",
        "<class 'returns.interfaces.container.ContainerN'>",
        "<class 'returns.interfaces.equable.Equable'>",
        "<class 'returns.interfaces.failable.DiverseFailableN'>",
        "<class 'returns.interfaces.failable.FailableN'>",
        "<class 'returns.interfaces.lashable.LashableN'>",
        "<class 'returns.interfaces.mappable.MappableN'>",
        "<class 'returns.interfaces.specific.result.ResultBasedN'>",
        "<class 'returns.interfaces.specific.result.ResultLikeN'>",
        "<class 'returns.interfaces.specific.result.UnwrappableResult'>",
        "<class 'returns.interfaces.swappable.SwappableN'>",
        "<class 'returns.interfaces.unwrappable.Unwrappable'>",
        "<class 'returns.primitives.container.BaseContainer'>",
        "<class 'returns.primitives.hkt.KindN'>",
        "<class 'returns.primitives.hkt.SupportsKindN'>",
        "<class 'returns.primitives.types.Immutable'>",
    ]


def test_lawful_interfaces__container_defined_outside_returns() -> None:
    """Check container defined outside `returns`."""
    result = lawful_interfaces(test_custom_type_applicative._Wrapper)  # noqa: SLF001

    assert sorted(str(interface) for interface in result) == [
        "<class 'returns.interfaces.applicative.ApplicativeN'>",
        "<class 'returns.interfaces.mappable.MappableN'>",
        "<class 'returns.primitives.container.BaseContainer'>",
        "<class 'returns.primitives.hkt.KindN'>",
        "<class 'returns.primitives.hkt.SupportsKindN'>",
        "<class 'returns.primitives.types.Immutable'>",
    ]


def test_lawful_interfaces__interface_defined_outside_returns() -> None:
    """Check container with interface defined outside `returns`."""
    result = lawful_interfaces(test_custom_interface_with_laws._Wrapper)  # noqa: SLF001

    # NOTE: The interface `_MappableN` is missing.
    assert sorted(str(interface) for interface in result) == [
        "<class 'returns.primitives.container.BaseContainer'>",
        "<class 'returns.primitives.hkt.KindN'>",
        "<class 'returns.primitives.hkt.SupportsKindN'>",
        "<class 'returns.primitives.types.Immutable'>",
    ]
