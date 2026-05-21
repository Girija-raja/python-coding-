from pynput import keyboard

def press(key):
    try:
        print("You pressed:", key.char)
    except:
        print("Special key pressed:", key)

    if key == keyboard.Key.esc:
        print("Program Closed")
        return False

print("KEYBOARD CHECKER")
print("Press keys...")
print("Press ESC to exit")

with keyboard.Listener(on_press=press) as listener:
    listener.join()

