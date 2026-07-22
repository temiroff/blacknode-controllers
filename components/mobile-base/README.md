# Mobile Base

Component of `blacknode-controllers`.

Node sources for this component belong in this folder. Until they move here,
nodes claim the component inline:

    @node(name="MyNode", component="mobile-base", ...)

Once sources live here, declare the folder in `blacknode-package.toml`:

    [components.mobile-base]
    nodes = ["components/mobile-base/nodes"]

and the inline `component=` argument can be dropped — the loader infers it
from the directory.
