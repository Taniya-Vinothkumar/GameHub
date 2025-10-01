import tkinter as tk
import random
from PIL import Image, ImageTk

def emoji_memory_game():
    def start_game():
        global emojis, index
        emojis = ["😊","💌","🤖", "🚀", "🎹","🍰", "🎮"]
        random.shuffle(emojis)

        positions = list(range(len(emojis)))
        index= random.choice(positions)

        label.config(text="Memorize the emojis!", fg="black")
        emoji_display.config(text=" ".join(emojis))
        answer.config(text="")
  

        root.after(4000, hide)

    def hide():
        emoji_display.config(text="🔒 🔒 🔒 🔒 🔒 🔒 🔒")
        label.config(text=f"What was at position {index + 1}?")
    
    def check_answer(selected):
        correct = emojis[index]
        if selected == correct:
            answer.config(text="✅ Correct!", fg="green")
        else:
            answer.config(text=f"❌ Wrong! It was {correct}", fg="red")

    root = tk.Toplevel()
    root.title("Emoji Memory Game")
    root.geometry("650x400+850+225")
    # root.config(bg="#31093C")
    root.resizable(False, False)

    image_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\memo.jpg"
    image = Image.open(image_path).resize((650,400))  
    img = ImageTk.PhotoImage(image)
    bckg = tk.Label(root, image=img)  
    bckg.image = img
    bckg.place(x=0, y=0, relwidth=1, relheight=1)

    title_label = tk.Label(root, text="Memoji", font=("Courier New", 20, "bold"), bg="#09093C", fg="#F0C824")
    title_label.pack(pady=10)
    
    label = tk.Label(root, text="Click Start to begin!", font=("Arial", 12))
    label.pack(pady=10)

    emoji_display = tk.Label(root, text="🔒 🔒 🔒 🔒 🔒 🔒 🔒", font=("Arial", 20))
    emoji_display.pack(pady=5)

    answer= tk.Label(root, text="", font=("Arial", 12))
    answer.pack(pady=10)


    emoji_options = ["😊","💌","🤖", "🚀", "🎹","🍰", "🎮"]
    emoji_buttons = []

    button_frame = tk.Frame(root, bg="#09093C")
    button_frame.pack()

    for emoji in emoji_options:
        btn = tk.Button(button_frame, text=emoji, font=("Arial", 20), width=4,
                    command=lambda e=emoji: check_answer(e))
        btn.pack(side="left", padx=10)
        emoji_buttons.append(btn)


    

    start_btn = tk.Button(root, text="Start", command=start_game, bg="lightblue", font=("Arial", 12))
    start_btn.pack(pady=10)

    quit_btn = tk.Button(root, text="Quit", command=root.destroy, bg="red", font=("Arial", 12))
    quit_btn.pack(pady=10)
    
