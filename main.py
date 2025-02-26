import tkinter as tk
import time


def freeze_system():
    # Create fullscreen black window
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background='black')

    # Update the window to show it
    root.update()

    # Freeze for 10 seconds
    time.sleep(10)

    # Destroy the window
    root.destroy()


if __name__ == "__main__":
    print("System will freeze for 10 seconds...")
    # Give user a moment to read the message
    time.sleep(2)
    freeze_system()
    print("Freeze complete!")


# only use to test your system please
