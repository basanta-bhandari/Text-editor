import ctypes as cts
import ctypes.wintypes as wts


LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11


class CONSOLE_FONT_INFOEX(cts.Structure):
    _fields_ = (
        ("cbSize", wts.ULONG),
        ("nFont", wts.DWORD),
        ("dwFontSize", wts._COORD),
        ("FontFamily", wts.UINT),
        ("FontWeight", wts.UINT),
        ("FaceName", wts.WCHAR * LF_FACESIZE)
    )


# Setup Windows API
kernel32 = cts.WinDLL("Kernel32.dll")
stdout = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def _get_font():
    """Internal: Get current font settings."""
    font = CONSOLE_FONT_INFOEX()
    font.cbSize = cts.sizeof(CONSOLE_FONT_INFOEX)
    kernel32.GetCurrentConsoleFontEx(stdout, False, cts.byref(font))
    return font


def _set_font(font):
    """Internal: Apply font settings."""
    kernel32.SetCurrentConsoleFontEx(stdout, False, cts.byref(font))


# Simple functions you can use
def font_size(height):
    """Change the font size. Example: font_size(20)"""
    font = _get_font()
    font.dwFontSize.Y = height
    _set_font(font)


def font_bold():
    """Make font bold. Example: font_bold()"""
    font = _get_font()
    font.FontWeight = 700
    _set_font(font)


def font_normal():
    """Make font normal weight. Example: font_normal()"""
    font = _get_font()
    font.FontWeight = 400
    _set_font(font)


def font_name(name):
    """Change font type. Example: font_name('Consolas')"""
    font = _get_font()
    font.FaceName = name
    _set_font(font)


def show_font():
    """Show current font settings."""
    font = _get_font()
    print(f"Font: {font.FaceName}")
    print(f"Size: {font.dwFontSize.Y}")
    print(f"Weight: {'Bold' if font.FontWeight >= 700 else 'Normal'}")


# Demo
if __name__ == "__main__":
    print("=== Simple Console Font Demo ===\n")
    
    # Show current settings
    print("Current font:")
    show_font()
    
    # Try different sizes
    print("\n--- Changing sizes ---")
    font_size(12)
    print("Size 12: Small text")
    
    font_size(16)
    print("Size 16: Normal text")
    
    font_size(24)
    print("Size 24: Large text")
    
    # Try bold
    print("\n--- Bold text ---")
    font_bold()
    print("This is BOLD!")
    
    font_normal()
    print("Back to normal weight")
    
    # Try different font
    print("\n--- Different font ---")
    font_name("Courier New")
    print("Now using Courier New")
    
    print("\nDone! Use font_size(), font_bold(), font_normal(), font_name() in your code.")