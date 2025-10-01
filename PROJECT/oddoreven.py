import tkinter as tk
import random
from PIL import Image, ImageTk

def odd_or_even_game():
   numbers = list(range(1, 51))
   random.shuffle(numbers)

   index = 0
   score = 0

   def check(choice):
    nonlocal index, score
    if index >= len(numbers):
        return

    num = numbers[index]
    correct = "Even" if num % 2 == 0 else "Odd"

    if choice == correct:
        score += 1
        index += 1
        if index < len(numbers):
            number_label.config(text=f"Number: {numbers[index]}")
            result_label.config(text="✅ Correct!", fg="green")
        else:
            result_label.config(text=f"🎉 All done! Final Score: {score}", fg="blue")
           
    else:
        result_label.config(text=f"❌ Wrong! It was {correct}\n Game Over! \n Final Score: {score}", fg="red")
 
   root = tk.Toplevel()
   root.title("Odd or Even")
   root.geometry("600x500+850+200")  

   root.resizable(False, False)
   image_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\oe.jpeg"
   image = Image.open(image_path).resize((600,500)) 
   img = ImageTk.PhotoImage(image)
   bckg = tk.Label(root, image=img)  
   bckg.image = img
   bckg.place(x=0, y=0, relwidth=1, relheight=1)

   lab=tk.Label(root,text="Odd or Even",font=("Noto Sans", 16, "bold"),bg="#0F2B2D", fg="white")
   lab.pack(pady=10)

   number_label = tk.Label(root, text=f"Number: {numbers[0]}", font=("Arial", 16,"bold"), bg="#BDAB0B", fg="black")
   number_label.pack(pady=10)

   odd_button = tk.Button(root, text="Odd", width=12,height=2, command=lambda: check("Odd"),bg="#B80F3F", fg="white")
   odd_button.pack(pady=5)

   even_button = tk.Button(root, text="Even", width=12,height=2, command=lambda: check("Even"),bg="#531B83", fg="white")
   even_button.pack(pady=5)



   result_label = tk.Label(root, text="", font=("Arial", 12),bg="black")
   result_label.pack(pady=10)

   quit_button = tk.Button(root, text="Quit", width=10,bg="crimson",command=root.destroy)
   quit_button.pack(pady=10)

 
