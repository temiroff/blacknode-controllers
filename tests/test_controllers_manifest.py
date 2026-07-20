import blacknode  # noqa: F401
from blacknode.packages import _PACKAGE_REGISTRY


def test_controller_layer_loads_policy_runtime_by_default():
    info = _PACKAGE_REGISTRY["blacknode-controllers"]
    assert info.ok
    assert info.layer == "controllers"
    assert info.component_mode is True
    assert info.enabled_components == ["policy"]
    assert set(info.components) == {
        "mobile-base", "nav2", "manipulation", "policy",
        "command-arbitration", "safety-supervisors",
    }
