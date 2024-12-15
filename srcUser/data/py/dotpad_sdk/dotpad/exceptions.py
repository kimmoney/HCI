class DotPadError(Exception):
    """Base exception for DotPad SDK errors."""
    pass

class DotPadInitializationError(DotPadError):
    """Raised when initialization fails."""
    pass

class DotPadDisplayError(DotPadError):
    """Raised when a display operation fails."""
    pass
