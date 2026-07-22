# Adapters

Transport adapters for the `manipulation` component of `blacknode-controllers`.

One folder per transport, each mirroring the component layout:

    adapters/ros2/nodes/
    adapters/ros2/templates/

Declare it in `blacknode-package.toml`:

    [components.manipulation.adapters.ros2]
    description = "ROS 2 adapter for manipulation."
    default = false
    capabilities = ["adapter.manipulation.ros2"]
    nodes = ["components/manipulation/adapters/ros2/nodes"]

Adapters stay `default = false`: the capability package owns them, and
`blacknode-ros2` provides only the shared transport underneath.
