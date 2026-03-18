#import
import random
import tkinter as tk

#GUI
window = tk.Tk()
window.title("Microsoft Random Feature Generator")
window.geometry("800x600") 
window.configure(bg="white")

Title = tk.Label(window, text="Microsoft Random Feature Generator", font=("Arial", 24), bg="white")
Title.pack(pady=20)

# create a label
Text = tk.Label(window, text="", font=("Arial", 18), bg="white")
Text.pack(pady=10)

Text = tk.Label(window, text="Press space to generate a random feature", font=("Arial", 18), bg="white")
Text.pack(pady=10)

def generate_random_feature():
    Features = random.randint(1,100)
    if Features <= 20:
        return "Add more AI slop"
    elif Features <= 40:
        return "Add more ads"
    elif Features <= 60:
        return "Add more subscription"
    elif Features <= 70:
        return "Add more user data collection"
    elif Features <= 99:
        return "Delete good/old OS"
    else:
        return "Make a good OS"

def key_press(event):
    if event.keysym == "space":
        print(event.keysym)
        Text.config(text=generate_random_feature())

window.bind("<KeyPress>", key_press)

window.mainloop()