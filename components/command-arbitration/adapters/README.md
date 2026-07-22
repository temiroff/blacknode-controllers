# Adapters

Transport adapters for the `command-arbitration` component of `blacknode-controllers`.

One folder per transport, each mirroring the component layout:

    adapters/ros2/nodes/
    adapters/ros2/templates/

Declare it in `blacknode-package.toml`:

    [components.command-arbitration.adapters.ros2]
    description = "ROS 2 adapter for command-arbitration."
    default = false
    capabilities = ["adapter.command-arbitration.ros2"]
    nodes = ["components/command-arbitration/adapters/ros2/nodes"]

Adapters stay `default = false`: the capability package owns them, and
`blacknode-ros2` provides only the shared transport underneath.
