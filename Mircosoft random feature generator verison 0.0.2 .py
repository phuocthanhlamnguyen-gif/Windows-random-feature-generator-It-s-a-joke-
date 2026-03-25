import random
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading

# GUI
window = tk.Tk()
window.title("Microsoft Random Feature Generator")
window.geometry("1000x950")
window.configure(bg="white")
window.resizable(False, False)

Title = tk.Label(window, text="Microsoft Random Feature Generator",
                 font=("Arial", 24), bg="white")
Title.pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 18), bg="white", highlightthickness=0)
result_label.pack(pady=10)

instruction_label = tk.Label(window,
    text="Press space or click a button to generate a random feature",
    font=("Arial", 18), bg="white")
instruction_label.pack(pady=10)

# Button canvas
canvas1 = tk.Canvas(window, width=200, height=100, bg="white", highlightthickness=0)
canvas1.pack()
shape = canvas1.create_oval(8, 8, 100, 100, fill='red', outline='red')
# Text for buttons
button_text = canvas1.create_text(55, 55, text="Generate", fill="white", font=("Arial", 12, "bold"))

# Make button1 clickable
def on_canvas_click(event):
    if 10 <= event.x <= 90 and 10 <= event.y <= 90:
        result_label.config(text=generate_random_feature())
    elif 110 <= event.x <= 190 and 10 <= event.y <= 90:
        result_label.config(text=generate_random_feature())

canvas1.bind("<Button-1>", on_canvas_click)

# Text path notes
text_path_label = tk.Label(window, text="Note: This is patch notes 26900.8037", font=("Arial", 12), bg="white")
text_path_label.pack(pady=5)

# Image loader with error handling
def load_image_from_url(url, size):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img = img.resize(size)
            return ImageTk.PhotoImage(img)
        else:
            print(f"Failed to load image: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

# Load initial images
photo = load_image_from_url(
    "https://blogs.microsoft.com/wp-content/uploads/2012/08/8867.Microsoft_5F00_Logo_2D00_for_2D00_screen.jpg",
    (500, 200)
)

if photo:
    label = tk.Label(window, image=photo, bg="white")
    label.image = photo
    label.pack()

photo2 = load_image_from_url(
    "https://msftstories.thesourcemediaassets.com/sites/620/2021/09/Hero-Bloom-Logo-800x533.jpg",
    (500, 300)
)

# Text for rules
news_label = tk.Label(window, text="Press E for Windows 10\nPress Q for Windows Server 2025\nPress W for Windows 11\nPress R for Windows Server 2022\nPress T for Windows Server 2019\nPress Y for Windows Server 2016\nPress U for Windows Server 2012",
    font=("Arial", 14), bg="white")
news_label.pack(pady=10)

label2 = tk.Label(window, bg="white")
if photo2:
    label2.config(image=photo2)
    label2.image = photo2
label2.pack()

# Random feature generator
def generate_random_feature():
    Features = random.randint(1, 100)
    if Features <= 20:
        return 'Add more AI slop that is called a "feature"'
    elif Features > 20 and Features <= 40:
        return "Add more ads by 300% for more profit"
    elif Features > 40 and Features <= 60:
        return "Add more subscription services that are required to use the OS"
    elif Features > 60 and Features <= 70:
        return "Add more user data collection to sell it to others"
    elif Features > 70 and Features <= 90:
        return 'Delete good/old OS to "encourages" users to upgrade'
    elif Features > 90 and Features <= 99:
        return "Add more bloatware/malware/spyware and forced useless update so the OS is slower"
    else:
        return "Make it generally better but it's only happen 1% of the time"

# Load image in background thread
def load_image_async(url, size):
    def _load():
        new_photo = load_image_from_url(url, size)
        if new_photo:
            label2.config(image=new_photo)
            label2.image = new_photo
    threading.Thread(target=_load, daemon=True).start()

# Key handler
def key_press(event):
    print(event.keysym)
    if event.keysym == "space":
        result_label.config(text=generate_random_feature())
    elif event.keysym == "e":
        load_image_async("https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Windows_10_Logo.svg/1280px-Windows_10_Logo.svg.png", (600, 230))
    elif event.keysym == "q":
        load_image_async("https://upload.wikimedia.org/wikipedia/commons/2/25/Windows_Server_2025_Logo.png", (750, 250))
    elif event.keysym == "w":
        load_image_async("https://msftstories.thesourcemediaassets.com/sites/620/2021/09/Hero-Bloom-Logo-800x533.jpg", (500, 300))
    elif event.keysym == "r":
        load_image_async("https://res-academy.cache.wpscdn.com/images/6b740b18f6cb2f3cbc117909b960b5ea_0.79_6126.png", (780, 300))
    elif event.keysym == "t":
        load_image_async("https://blog.trustedtechteam.com/static/00649cac9f2bc93414a8921798fd982c/4ce6a/hero-2020-07_16.png", (780, 300))
    elif event.keysym == "y":
        load_image_async("https://aidanfinn.com/wp-content/uploads/2016/09/3252.windows-server-2016.png", (500, 300))
    elif event.keysym == "u":
        load_image_async("https://cdn.neowin.com/news/images/uploaded/2014/08/windows-server-2012-01_story.jpg", (860, 300))
    elif event.keysym == "Escape":
        window.destroy()
    else:
        window.bell()

# Bind keys
window.bind("<Key>", key_press)

window.mainloop()