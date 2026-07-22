import blacknode  # noqa: F401
from blacknode.packages import _PACKAGE_REGISTRY


def test_controller_layer_loads_joint_control_and_policy_by_default():
    info = _PACKAGE_REGISTRY["blacknode-controllers"]
    assert info.ok
    assert info.layer == "controllers"
    assert info.component_mode is True
    assert info.enabled_components == ["joint-control", "policy"]
    assert set(info.components) == {
        "joint-control", "mobile-base", "nav2", "manipulation", "policy",
        "command-arbitration", "safety-supervisors",
    }


def test_joint_control_ros2_adapter_is_enabled_and_owns_the_motion_nodes():
    info = _PACKAGE_REGISTRY["blacknode-controllers"]
    adapter = info.components["joint-control"]["adapters"]["ros2"]
    assert adapter["enabled"] is True
    assert set(adapter["node_types"]) == {
        "ROS2JointState", "ROS2ManualMove", "ROS2MotionDashboard", "ROS2SetJoint",
    }
    # the adapter must rest on the ROS 2 integration layer, never the reverse
    assert adapter["requirements"][0]["package"] == "blacknode-ros2"
