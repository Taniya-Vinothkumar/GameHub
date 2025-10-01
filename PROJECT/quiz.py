import tkinter as tk
from PIL import Image, ImageTk


def quizgame():
   questions = [
    "Which is the largest country in the world by area?",
    "Which is the longest river flowing through Tamil Nadu?",
    "What is the capital of Germany?",
    "Which city is known as the Manchester of South India?",
    "Which country is known as the Land of the Rising Sun?",
    "Which Indian city is known as the Silicon Valley of India?",
    "Which is the highest civilian award in India?",
    "Which gas is most abundant in the Earth's atmosphere?",
    "Who is known as the father of the computer?",
    "Which country won the ICC Cricket World Cup in 2011?",
    "Which programming language is known as the mother of all languages?",
    "Which is the largest continent in the world?",
    "Which Chola king built the Brihadeeswarar Temple in Thanjavur?"


     ]
   options = [
    ["Russia", "Canada", "China"],
    ["Vaigai", "Kaveri", "Thamiraparani"],
    ["Berlin", "Paris", "London"],
    ["Chennai","Tiruppur","Coimbatore"],
    ["Japan", "China", "India"],
    ["Bangalore", "Hyderabad", "Chennai"],
    ["Padma Vibhushan","Bharat Ratna", "Padma Bhushan"],
    ["Oxygen","Carbon Dioxide","Nitrogen"],
    ["Alan Turing","Charles Babbage","Bill Gates"],
    ["India", "Australia", "England"],
    ["C","Python","Java"],
    ["Africa", "Europe","Asia"],
    ["Rajaraja Chola I", "Rajendra Chola I", "Vijayalaya Chola"]
      ]
   answers = [0, 1, 0, 2, 0, 0, 1, 2, 1, 0, 0, 2, 0]

   q_index = 0
   score = 0

   def check_answer(i):
      nonlocal q_index, score
      if i == answers[q_index]:
        score += 1
        result= "Correct!"
      else:
        crct_answer = options[q_index][answers[q_index]]
        result = f"Incorrect!,The correct answer is:{crct_answer}"
      result_label.config(text=result)
      q_index += 1
      if q_index < len(questions):
        root.after(1000, show_question) 
      else:
        root.after(1000, show_result)

   def show_question():
        nonlocal q_index
        question_label.config(text=questions[q_index])
        for i in range(3):
            buttons[i].config(text=options[q_index][i], command=lambda i=i: check_answer(i))

   def show_result():
        question_label.config(text=f"Your score: {score} / {len(questions)}")
        result_label.config(text="Quiz Completed!")
   def quit_game():
      root.destroy()
   root = tk.Toplevel()
   root.title("Quiz Game")
   root.geometry("700x550+825+100")
   root.config(bg="black")
   root.resizable(False, False)
   image_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\imag.jpg"
   image = Image.open(image_path).resize((700,550)) 
   img = ImageTk.PhotoImage(image)
   bckg = tk.Label(root, image=img)  
   bckg.image = img
   bckg.place(x=-20, y=0, relwidth=1, relheight=1)

   title_label = tk.Label(root, text="Quiz Time", font=("Courier New", 24, "bold"),bg="#104E88" ,fg="#FFFFFF")
   title_label.pack(pady=20)

   question_label = tk.Label(root, text="", font=("Arial", 14,"bold"),bg="#0D2943", fg="#FFFFFF")
   question_label.pack(pady=25,anchor="center")

   buttons = []
   for i in range(3):
       b = tk.Button(root, text="", font=("Arial", 12,"bold"), width=20,bg="#1768B3", fg="#000000", command=lambda i=i: check_answer(i))
       b.pack(pady=2)
       buttons.append(b)
   result_label = tk.Label(root, text="", font=("Arial", 12),bg="black",fg="#E7DD29")
   result_label.pack(pady=10)
   quit_button = tk.Button(root, text="Quit", font=("Arial", 10, "bold"), width=15, height=3, command=quit_game, bg="#950E2D", fg="white")
   quit_button.pack(pady=20)
   show_question()
   