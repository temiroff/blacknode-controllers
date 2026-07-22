# Safety Supervisors

Component of `blacknode-controllers`.

Node sources for this component belong in this folder. Until they move here,
nodes claim the component inline:

    @node(name="MyNode", component="safety-supervisors", ...)

Once sources live here, declare the folder in `blacknode-package.toml`:

    [components.safety-supervisors]
    nodes = ["components/safety-supervisors/nodes"]

and the inline `component=` argument can be dropped — the loader infers it
from the directory.
