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


# Font size alternatives (visual tricks since actual font size isn't controllable)
def print_small(text):
    """Print smaller text using dim style."""
    print(f"{DIM}{text}{RESET}")


def print_big(text):
    """Print bigger text - just bold and uppercase."""
    print(f"{BOLD}{text.upper()}{RESET}")


def print_header(text):
    """Print a simple clean header."""
    print(f"\n{BOLD}{text}{RESET}")


def print_title(text):
    """Print a title with simple underline."""
    print(f"\n{BOLD}{text}{RESET}")
    print("─" * len(text))


def print_large(text, color_code=None, bold_it=True, underline_it=False, italic_it=False):
    """
    Print large stylized text with optional formatting.
    
    Args:
        text: Text to print
        color_code: Color (RED, GREEN, BLUE, etc.)
        bold_it: Make it bold (default True)
        underline_it: Underline it (default False)
        italic_it: Make it italic (default False)
    
    Example: print_large("HELLO", RED, bold_it=True, underline_it=True)
    """
    # Build the style
    styles = []
    if bold_it:
        styles.append(BOLD)
    if underline_it:
        styles.append(UNDERLINE)
    if italic_it:
        styles.append(ITALIC)
    if color_code:
        styles.append(color_code)
    
    # Apply styles
    styled_text = "".join(styles) + text.upper() + RESET
    
    # Print with spacing for "large" effect
    print(f"\n  {styled_text}  \n")


def print_styled(text, color=None, bg=None, bold_it=False, italic_it=False, underline_it=False, dim_it=False):
    """
    Print text with any combination of styles.
    
    Args:
        text: Text to print
        color: Text color (RED, GREEN, BLUE, etc.)
        bg: Background color (BG_RED, BG_GREEN, etc.)
        bold_it: Make bold
        italic_it: Make italic
        underline_it: Underline
        dim_it: Dim/faint
    
    Example: print_styled("Hello", RED, BG_WHITE, bold_it=True, underline_it=True)
    """
    styles = []
    if bold_it:
        styles.append(BOLD)
    if italic_it:
        styles.append(ITALIC)
    if underline_it:
        styles.append(UNDERLINE)
    if dim_it:
        styles.append(DIM)
    if color:
        styles.append(color)
    if bg:
        styles.append(bg)
    
    print("".join(styles) + text + RESET)


def print_huge(text, color_code=None, bold_it=False):
    """
    Print HUGE ASCII art text. Works with A-Z and 0-9.
    
    Args:
        text: Text to print (A-Z, 0-9, space, !)
        color_code: Color to apply
        bold_it: Make the ASCII art bold
    
    Example: print_huge("HELLO", RED, bold_it=True)
    """
    # ASCII art font dictionary
    font = {
        'A': [
            "   ___   ",
            "  / _ \\  ",
            " / /_\\ \\ ",
            "/  _  _\\ ",
            "\\_/ \\_/ "
        ],
        'B': [
            " ____  ",
            "|  _ \\ ",
            "| |_) |",
            "|  _ < ",
            "|_| \\_\\"
        ],
        'C': [
            "  ____ ",
            " / ___|",
            "| |    ",
            "| |___ ",
            " \\____|"
        ],
        'D': [
            " ____  ",
            "|  _ \\ ",
            "| | | |",
            "| |_| |",
            "|____/ "
        ],
        'E': [
            " _____ ",
            "|  ___|",
            "| |__  ",
            "|  __| ",
            "|_____|"
        ],
        'F': [
            " _____ ",
            "|  ___|",
            "| |__  ",
            "|  __| ",
            "|_|    "
        ],
        'G': [
            "  ____ ",
            " / ___|",
            "| |  _ ",
            "| |_| |",
            " \\____|"
        ],
        'H': [
            " _   _ ",
            "| | | |",
            "| |_| |",
            "|  _  |",
            "|_| |_|"
        ],
        'I': [
            " ___ ",
            "|_ _|",
            " | | ",
            " | | ",
            "|___|"
        ],
        'J': [
            "     _ ",
            "    | |",
            " _  | |",
            "| |_| |",
            " \\___/ "
        ],
        'K': [
            " _  __",
            "| |/ /",
            "| ' / ",
            "| . \\ ",
            "|_|\\_\\"
        ],
        'L': [
            " _     ",
            "| |    ",
            "| |    ",
            "| |___ ",
            "|_____|"
        ],
        'M': [
            " __  __ ",
            "|  \\/  |",
            "| |\\/| |",
            "| |  | |",
            "|_|  |_|"
        ],
        'N': [
            " _   _ ",
            "| \\ | |",
            "|  \\| |",
            "| |\\  |",
            "|_| \\_|"
        ],
        'O': [
            "  ___  ",
            " / _ \\ ",
            "| | | |",
            "| |_| |",
            " \\___/ "
        ],
        'P': [
            " ____  ",
            "|  _ \\ ",
            "| |_) |",
            "|  __/ ",
            "|_|    "
        ],
        'Q': [
            "  ___  ",
            " / _ \\ ",
            "| | | |",
            "| |_| |",
            " \\__\\_\\"
        ],
        'R': [
            " ____  ",
            "|  _ \\ ",
            "| |_) |",
            "|  _ < ",
            "|_| \\_\\"
        ],
        'S': [
            " ____  ",
            "/ ___| ",
            "\\___ \\ ",
            " ___) |",
            "|____/ "
        ],
        'T': [
            " _____ ",
            "|_   _|",
            "  | |  ",
            "  | |  ",
            "  |_|  "
        ],
        'U': [
            " _   _ ",
            "| | | |",
            "| | | |",
            "| |_| |",
            " \\___/ "
        ],
        'V': [
            "__     __",
            "\\ \\   / /",
            " \\ \\ / / ",
            "  \\ V /  ",
            "   \\_/   "
        ],
        'W': [
            "__        __",
            "\\ \\      / /",
            " \\ \\ /\\ / / ",
            "  \\ V  V /  ",
            "   \\_/\\_/   "
        ],
        'X': [
            "__  __",
            "\\ \\/ /",
            " \\  / ",
            " /  \\ ",
            "/_/\\_\\"
        ],
        'Y': [
            "__   __",
            "\\ \\ / /",
            " \\ V / ",
            "  | |  ",
            "  |_|  "
        ],
        'Z': [
            " _____ ",
            "|__  / ",
            "  / /  ",
            " / /_  ",
            "/____|"
        ],
        '0': [
            "  ___  ",
            " / _ \\ ",
            "| | | |",
            "| |_| |",
            " \\___/ "
        ],
        '1': [
            " _ ",
            "/ |",
            "| |",
            "| |",
            "|_|"
        ],
        '2': [
            " ____  ",
            "|___ \\ ",
            "  __) |",
            " / __/ ",
            "|_____|"
        ],
        '3': [
            " _____ ",
            "|___ / ",
            "  |_ \\ ",
            " ___) |",
            "|____/ "
        ],
        '4': [
            " _  _   ",
            "| || |  ",
            "| || |_ ",
            "|__   _|",
            "   |_|  "
        ],
        '5': [
            " ____  ",
            "| ___| ",
            "|___ \\ ",
            " ___) |",
            "|____/ "
        ],
        '6': [
            "  __   ",
            " / /_  ",
            "| '_ \\ ",
            "| (_) |",
            " \\___/ "
        ],
        '7': [
            " _____ ",
            "|___  |",
            "   / / ",
            "  / /  ",
            " /_/   "
        ],
        '8': [
            "  ___  ",
            " ( _ ) ",
            " / _ \\ ",
            "| (_) |",
            " \\___/ "
        ],
        '9': [
            "  ___  ",
            " / _ \\ ",
            "| (_) |",
            " \\__, |",
            "   /_/ "
        ],
        ' ': [
            "    ",
            "    ",
            "    ",
            "    ",
            "    "
        ],
        '!': [
            " _ ",
            "| |",
            "| |",
            "|_|",
            "(_)"
        ]
    }
    
    text = text.upper()
    
    # Check if all characters are supported
    if not all(c in font for c in text):
        print(f"{BOLD}[Unsupported characters - using fallback]{RESET}")
        print_large(text, color_code)
        return
    
    # Print each line of the ASCII art
    style = ""
    if bold_it:
        style += BOLD
    if color_code:
        style += color_code
    
    for line_num in range(5):
        line = ""
        for char in text:
            line += font[char][line_num]
        print(f"{style}{line}{RESET}")
    print()  # Extra newline at the end


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
    
    print("\n--- Size alternatives ---")
    print_small("Smaller/dimmer text")
    print("Normal text")
    print_big("BIGGER TEXT")
    
    print_header("Section Header")
    print_title("Title with underline")
    
    print("\n--- Large text with styles ---")
    print_large("HELLO", RED)
    print_large("SUCCESS", GREEN, bold_it=True)
    print_large("WARNING", YELLOW, bold_it=True, underline_it=True)
    
    print("\n--- HUGE ASCII text ---")
    print_huge("HELLO", CYAN)
    print_huge("2024", GREEN)
    print_huge("OK!", BRIGHT_GREEN)
    
    print("Done! Works on Linux, Mac, and Windows!")