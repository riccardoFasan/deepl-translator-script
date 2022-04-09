from distutils.util import strtobool
import colorama


def get_truncated_text(text: str, limit: int) -> str:
    return text[:limit] + "..." if len(text) > limit else text


def get_color_by_percentage(percentage: int) -> str:
    if percentage > 90:
        return colorama.Fore.RED
    if percentage > 60:
        return colorama.Fore.YELLOW
    return colorama.Fore.RESET
