import sys, os
import pyfiglet

import embeds
from .colors import Colors

APP_COLOR = Colors.APP_COLOR

class Console:

    def print_banner():
        Colors.rainbow_text(
            pyfiglet.figlet_format("Embeds", font = "epic").strip() 
            + f" v{embeds.__version__} By: {embeds.__author__} \n \n"
        )

    def print_app_color():
        """ Converts terminal text to the app color """
        sys.stdout.write(f"\x1b[38;2;{APP_COLOR[0]};{APP_COLOR[1]};{APP_COLOR[2]}m")

    def clear():
        os.system("cls")

    def get_input():
        Console.print_app_color()
        return input(f"root@Embeds v{embeds.__version__}:~$ ")

    def pause():
        os.system("pause")

       