"""Perform tasks when a Houdini node has its name changed."""

# =============================================================================
# IMPORTS
# =============================================================================

# Houdini Toolbox Imports
#import ht.nodes.colors

from ht.events import runEvents

# =============================================================================
# FUNCTIONS
# =============================================================================

def main():
    """Main function."""
    runEvents("OnNameChanged", kwargs)

# =============================================================================

main()

