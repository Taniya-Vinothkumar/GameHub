import tkinter as tk
from PIL import Image, ImageTk

def tf_game():


    questions = [
   
    "1.The Great Wall of China is visible from the Moon.",
    "2.An octopus has three hearts.",
    "3.A day on Venus is longer than a year on Earth.",
    "4.Bats are blind.",
    "5.An ostrich’s eye is bigger than its brain.",
    "6.The capital of Australia is Sydney.",
    "7.Octopuses have blue blood.",
    "8.Subhas Chandra Bose formed the Indian National Army.",
    "9.The Eiffel Tower can be 15 cm taller during the summer.",
    "10.A snail can sleep for three years.",
    "11.Penguins live in the North Pole.",
    "12.The shortest war in history lasted 38 minutes.",
    "13.The unicorn is the national animal of Scotland.",
    "14.The longest place name in the world is 85 letters long.",
    "15.Astronauts' height can increase in space due to the lack of gravity"



    ]

    answers = [
    "False",
    "True",
    "True",
    "False",
    "True",
    "False",
    "True",
    "True",
    "True",
    "True",
    "False",
    "True",
    "True",
    "True",
    "True"
    ]

    index=0
    score = 0

    def check_tf(i):
        nonlocal index, score
        if i == answers[index]:
            score += 1
            result= "Correct!"
        else:
            crct_answer = answers[index]
            result = "Incorrect!", f"The correct answer is:{crct_answer}"
        result_label.config(text=result)
        index += 1
        if index < len(questions):
            root.after(1000, show_question) 
        else:
            root.after(1000, show_result)

    def show_question():
        question_label.config(text=questions[index])
        result_label.config(text="")
       

    def show_result():
        question_label.config(text=f"Your score: {score} / {len(questions)}")
        result_label.config(text="Game Completed!")

    def quit_game():
      root.destroy()
      
    root = tk.Toplevel()
    root.title("True or False Game")
    root.geometry("700x550+825+100")
    root.config(bg="black")
    root.resizable(False, False)
    tf_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\tf.webp"
    
    image = Image.open(tf_path).resize((700,550))
    img = ImageTk.PhotoImage(image)
    bckg = tk.Label(root, image=img)
    bckg.image = img
    bckg.place(x=0, y=0, relwidth=1, relheight=1)




    title_label = tk.Label(root, text="  True or False  ", font=("Courier New", 24, "bold"),bg="#001F1A" ,fg="#F73155")
    title_label.pack(pady=20)

    question_label = tk.Label(root, text="", font=("Arial", 14,"bold"),fg="#000000", bg="#FFFFFF")
    question_label.pack(pady=25,anchor="center")

    buttons=[]
    b = tk.Button(root, text="True", font=("Arial", 12,"bold"), width=20,bg="#10E954", fg="#000000", command=lambda :check_tf("True"))
    b.pack(pady=20)
    buttons.append(b)      
    c= tk.Button(root, text="False", font=("Arial", 12,"bold"), width=20,bg="#B31717", fg="#000000", command=lambda :check_tf("False"))
    c.pack(pady=20)
    buttons.append(c)
       
    result_label = tk.Label(root, text="", font=("Arial", 12),bg="black",fg="#E7DD29")
    result_label.pack(pady=10)
    quit_button = tk.Button(root, text="Quit", font=("Arial", 10, "bold"), width=15, height=3, command=quit_game, bg="#950E2D", fg="white")
    quit_button.pack(pady=20)
    show_question()
    