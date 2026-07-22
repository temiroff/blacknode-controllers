# Command Arbitration

Component of `blacknode-controllers`.

Node sources for this component belong in this folder. Until they move here,
nodes claim the component inline:

    @node(name="MyNode", component="command-arbitration", ...)

Once sources live here, declare the folder in `blacknode-package.toml`:

    [components.command-arbitration]
    nodes = ["components/command-arbitration/nodes"]

and the inline `component=` argument can be dropped — the loader infers it
from the directory.
