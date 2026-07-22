# blacknode-controllers

This repository is the controller layer. Components operate on stable robot
and perception capabilities and remain independent of vendor drivers. Motion
components begin disabled until their contracts, mock providers, and safety
tests are implemented.

Each component keeps its transport-neutral contract separate from the
adapters that put it on a wire. A ROS 2 adapter declares a versioned
dependency on `blacknode-ros2/core` and never the other way round, so a
second transport can be added later as a sibling adapter.

## Components

| Component | Default | ROS 2 adapter nodes |
|---|---|---|
| `joint-control` | on | `ROS2JointState`, `ROS2SetJoint`, `ROS2ManualMove`, `ROS2MotionDashboard` |
| `mobile-base` | off | `BaseSafetyGate`, `ROS2BaseMove`, `ROS2BaseStop`, `ROS2LaserScanCheck`, `ROS2OdomState` |
| `policy` | on | `PolicyRuntime`, `PolicySafetyGate` |
| `nav2`, `manipulation`, `command-arbitration`, `safety-supervisors` | off | contracts only, not yet implemented |

### joint-control

Drives **any** robot exposing `sensor_msgs/msg/JointState`: topics, joint
name, and units are all inputs, so robot specifics live in templates rather
than in the nodes. `transport=auto` prefers native `rclpy` and falls back to
rosbridge.

Motion is gated. `ROS2SetJoint` does nothing until `armed=true`; while
disarmed it still reads live pose, so the preview shows real numbers and the
exact target it *would* command. Armed moves sync to the current pose first,
clamp to any limits published on the config topic, and stream a heartbeat so
the robot driver's own timeout still applies.

`ROS2ManualMove` releases or holds torque for hand positioning and owns the
live joint monitor; `ROS2MotionDashboard` renders either its live pose or a
one-time before/after motion result. Both are managed live services: inspect
them with `get_editor_runtime_status` and stop them with
`stop_editor_runtime_services`. Releasing torque disables actuator holding
power, so support the arm before doing it.

Template: **Move a Robot Joint**
(`components/joint-control/adapters/ros2/templates/`).
