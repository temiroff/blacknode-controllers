# Nav2

Component of `blacknode-controllers`.

Node sources for this component belong in this folder. Until they move here,
nodes claim the component inline:

    @node(name="MyNode", component="nav2", ...)

Once sources live here, declare the folder in `blacknode-package.toml`:

    [components.nav2]
    nodes = ["components/nav2/nodes"]

and the inline `component=` argument can be dropped — the loader infers it
from the directory.
