import sys
from rich import print
from time import sleep

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def printLyrics():
    title = " TORE UP - Don Toliver "

    lines = [
        ("If you believe in yourself", 0.062),
        ("It will get you through it", 0.038),
        ("Oh, I believed in myself", 0.068),
        ("Well, can you see what I'm doin'?", 0.062),
        ("In the club with some ones and I'm piped up", 0.040),
        ("Shawty got me high, too high", 0.052),
        ("I be steppin' on a bitch in some white 1s", 0.072),
        ("Can't control me, I think I'm too fly", 0.052),
        ("TORE UP, TORE UP, TORE UP, TORE UP, TORE UP, TORE UP, TORE UP", 0.072),

    ]

    delays = [1.2, 1.2, 1.2, 1.6, 0.6, 0.9, 0.9, 0.9, 0.9]

    hide_cursor()
    try:
        print(f"\n[bold #FFD700]{title}[/bold #FFD700]\n")

        for i, (line, char_delay) in enumerate(lines):
            for char in line:
                print(f"[bold #0A1A3F]{char}[/bold #0A1A3F]", end="")
                sys.stdout.flush()
                sleep(char_delay)
            print()
            if i < len(delays):
                sleep(delays[i])
    finally:
        sleep(3)
        show_cursor()

printLyrics()