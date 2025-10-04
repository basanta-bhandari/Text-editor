import sys


# ANSI escape codes for text formatting
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'

# Colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

# Bright colors
BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'

# Background colors
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'


def bold(text):
    """Make text bold. Example: print(bold('Hello'))"""
    return f"{BOLD}{text}{RESET}"


def italic(text):
    """Make text italic. Example: print(italic('Hello'))"""
    return f"{ITALIC}{text}{RESET}"


def underline(text):
    """Underline text. Example: print(underline('Hello'))"""
    return f"{UNDERLINE}{text}{RESET}"


def color(text, fg=None, bg=None):
    """
    Color text. Example: print(color('Hello', RED, BG_WHITE))
    
    Args:
        text: Text to color
        fg: Foreground color (RED, GREEN, BLUE, etc.)
        bg: Background color (BG_RED, BG_GREEN, etc.)
    """
    result = ""
    if fg:
        result += fg
    if bg:
        result += bg
    result += text + RESET
    return result


def style(text, *styles):
    """
    Apply multiple styles. Example: print(style('Hello', BOLD, RED, UNDERLINE))
    """
    result = "".join(styles) + text + RESET
    return result


# Simple print functions
def print_bold(text):
    """Print bold text. Example: print_bold('Hello')"""
    print(f"{BOLD}{text}{RESET}")


def print_red(text):
    """Print red text."""
    print(f"{RED}{text}{RESET}")


def print_green(text):
    """Print green text."""
    print(f"{GREEN}{text}{RESET}")


def print_blue(text):
    """Print blue text."""
    print(f"{BLUE}{text}{RESET}")


def print_yellow(text):
    """Print yellow text."""
    print(f"{YELLOW}{text}{RESET}")


def print_success(text):
    """Print success message (green, bold)."""
    print(f"{BOLD}{GREEN}{text}{RESET}")


def print_error(text):
    """Print error message (red, bold)."""
    print(f"{BOLD}{RED}{text}{RESET}")


def print_warning(text):
    """Print warning message (yellow, bold)."""
    print(f"{BOLD}{YELLOW}{text}{RESET}")


def print_info(text):
    """Print info message (blue)."""
    print(f"{BLUE}{text}{RESET}")


def clear_screen():
    """Clear the terminal screen."""
    print('\033[2J\033[H', end='')


def clear_line():
    """Clear the current line."""
    print('\033[2K', end='\r')


# Demo
if __name__ == "__main__":
    print("=== Cross-Platform Console Text Formatter ===\n")
    
    # Basic styles
    print("Normal text")
    print_bold("Bold text")
    print(italic("Italic text"))
    print(underline("Underlined text"))
    
    print("\n--- Colors ---")
    print_red("Red text")
    print_green("Green text")
    print_blue("Blue text")
    print_yellow("Yellow text")
    
    print("\n--- Combined styles ---")
    print(style("Bold + Red + Underline", BOLD, RED, UNDERLINE))
    print(color("Green text on yellow background", GREEN, BG_YELLOW))
    
    print("\n--- Message types ---")
    print_success("✓ Operation successful!")
    print_error("✗ Error occurred!")
    print_warning("⚠ Warning message")
    print_info("ℹ Information")
    
    print("\n--- Build your own ---")
    print(bold("This is bold"))
    print(color("This is red", RED))
    print(style("Bold red underlined!", BOLD, RED, UNDERLINE))
    
    print("\nDone! Works on Linux, Mac, and Windows!")