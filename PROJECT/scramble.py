import tkinter as tk
import random
from PIL import Image, ImageTk

def scramble_game():
    global words, index, score, word, jumbled

    words = [ "daisy", "sunflower", "tulip", "jasmine", "banana", "grape", "orange", "cherry","hibiscus","calculator", "backpack", "newspaper", "television", "refrigerator", "headphones"]
    random.shuffle(words)
    index = 0
    score = 0

    def new_word():
        global index, word, jumbled
        if index >= len(words):
            word_label.config(text="Game Over!")
            result_label.config(text=f"Your Score: {score}")
            entry.config(state="disabled")
            return
        word = words[index]
        jumbled = ''.join(random.sample(word, len(word)))
        word_label.config(text=f"Unscramble: {jumbled}")
        entry.delete(0, tk.END)
        result_label.config(text="")
        index += 1

    def check():
        global score
        guess = entry.get()
        if guess.lower() == word:
            result_label.config(text="Correct!", fg="green")
            score += 1
        else:
            result_label.config(text=f"Wrong! It was '{word}'", fg="red")
        score_label.config(text=f"Score: {score}")
        root.after(1500, new_word)

    root = tk.Toplevel()
    root.title("Jumbled Word Game")
    root.geometry("600x600+850+100")
    root.config(bg="black")
    root.resizable(False, False)

    image_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\jumb.webp"
    image = Image.open(image_path).resize((600,600))  
    img = ImageTk.PhotoImage(image)
    bckg = tk.Label(root, image=img)  
    bckg.image = img
    bckg.place(x=0, y=0)

    score_label = tk.Label(root, text="Score: 0", font=("Arial", 14), fg="white", bg="black")
    score_label.pack(pady=10)

    word_label = tk.Label(root, text="", font=("Arial", 16), fg="yellow", bg="black")
    word_label.pack(pady=10)

    entry = tk.Entry(root, font=("Arial", 14))
    entry.pack(pady=10)

    check_btn = tk.Button(root, text="Check", command=check, font=("Arial", 12), bg="green", fg="white")
    check_btn.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Arial", 14), bg="black")
    result_label.pack(pady=10)

    quit_btn = tk.Button(root, text="Quit", command=root.destroy, font=("Arial", 12), bg="red", fg="white")
    quit_btn.pack(pady=10)

    new_word()
