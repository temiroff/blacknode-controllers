# Policy

Component of `blacknode-controllers`.

Node sources for this component belong in this folder. Until they move here,
nodes claim the component inline:

    @node(name="MyNode", component="policy", ...)

Once sources live here, declare the folder in `blacknode-package.toml`:

    [components.policy]
    nodes = ["components/policy/nodes"]

and the inline `component=` argument can be dropped — the loader infers it
from the directory.
