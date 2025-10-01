import tkinter as tk
import random
from PIL import Image, ImageTk
def rps_game():
   options = ["rock", "paper", "scissors"]
   global user_score, computer_score


   user_score = 0
   computer_score = 0

   def game(user_choice):
      global user_score, computer_score
      computer_choice = random.choice(options)
      result = ""

      if user_choice == computer_choice:
        result = "It's a tie!"
      elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        result = "You won!"
        user_score += 1
      else:
        result = "You lost!"
        computer_score += 1

    
      results.config(text=f"Computer chose: {computer_choice}\n{result}")
      score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")


   def quit_game():
      root.destroy()


   root = tk.Toplevel()
   root.title("Rock Paper Scissors")
   root.geometry("500x600+950+100")
   root.config(bg="#F9F6F6")
   root.resizable(False, False)
   image_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\rps.jpg"
   image = Image.open(image_path).resize((500,600))  
   img = ImageTk.PhotoImage(image)
   bckg = tk.Label(root, image=img)  
   bckg.image = img
   bckg.place(x=0, y=0)


   title_label = tk.Label(root, text="Rock Paper Scissors 🪨📄✂️", font=("Courier New", 20, "bold"), bg="#000000", fg="#C1C54C")
   title_label.pack(pady=10)

   button_frame = tk.Frame(root,bg="#6B1619")
   button_frame.pack(padx=10,pady=10)


   rock = tk.Button(button_frame, text=" 🪨Rock ", width=12,height=2,font=("Arial", 16, "bold"), bg="#000000", fg="white" ,command=lambda: game("rock"))
   rock.grid(row=0, column=1, padx=10)

   paper= tk.Button(button_frame, text="📄 Paper ", width=12,height=2,font=("Arial", 16, "bold"), bg="#000000", fg="white", command=lambda: game("paper"))
   paper.grid(row=1, column=1, padx=10)

   scissors= tk.Button(button_frame, text="✂️ Scissors", width=12,height=2,font=("Arial",16 , "bold"), bg="#000000", fg="white", command=lambda: game("scissors"))
   scissors.grid(row=2, column=1, padx=10)

   results = tk.Label(root, text="", font=("Arial", 14),  bg="black", fg="white")
   results.pack(pady=20)

   score= tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 14), bg="black", fg="white")
   score.pack(pady=5)


   quit= tk.Button(root, text="Quit",font=("Ariel",10,"bold"), width=15,height=3, command=quit_game, bg="#383DD1", fg="white")
   quit.pack(side="bottom")

   




