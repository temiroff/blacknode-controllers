# blacknode-controllers Agent Instructions

This is an independent Blacknode extension-package repository.

Keep generic navigation, manipulation, learned-policy, command-arbitration,
and safety controllers here. Consume stable state and command capabilities;
never import vendor hardware SDKs. Motion stays disarmed by default. Enforce
freshness, calibrated limits, idempotence, ownership, emergency stop, and
explicit shutdown at every controller boundary. Test with mock or replay
providers before supported hardware providers.

Run package tests with `python -m pytest packages/blacknode-controllers/tests`.
