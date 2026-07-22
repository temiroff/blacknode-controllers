# Adapters

Transport adapters for the `safety-supervisors` component of `blacknode-controllers`.

One folder per transport, each mirroring the component layout:

    adapters/ros2/nodes/
    adapters/ros2/templates/

Declare it in `blacknode-package.toml`:

    [components.safety-supervisors.adapters.ros2]
    description = "ROS 2 adapter for safety-supervisors."
    default = false
    capabilities = ["adapter.safety-supervisors.ros2"]
    nodes = ["components/safety-supervisors/adapters/ros2/nodes"]

Adapters stay `default = false`: the capability package owns them, and
`blacknode-ros2` provides only the shared transport underneath.
