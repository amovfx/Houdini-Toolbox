"""Perform tasks when a Houdini node has its name changed."""

# =============================================================================
# IMPORTS
# =============================================================================

# Houdini Toolbox Imports
from ht.events import runEvent

# =============================================================================
# FUNCTIONS
# =============================================================================

def main():
    """Main function."""
    runEvent("OnNameChanged", kwargs)

# =============================================================================

main()

