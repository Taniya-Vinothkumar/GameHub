import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image, ImageTk
import mysql.connector          
from rockpaper import rps_game
from scramble import scramble_game
from quiz import quizgame
from memory import emoji_memory_game
from truefalse import tf_game
from oddoreven import odd_or_even_game  


def db_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )



def signup_fn(data):
    user, pwd, confirm_pwd, mail,age,gender,city = data
   
    
    if pwd != confirm_pwd:
        messagebox.showerror("Error !!", "Passwords do not match!")
        return
    
    if user=="" or pwd=="" or confirm_pwd=="" or mail=="" or age=="" or gender=="" or city=="Select City":
        messagebox.showerror("Error !!", "All fields are required!")
        return
    

    Connection=db_connect()
    cursor=Connection.cursor()

    try:
        cursor.execute("INSERT INTO login(Username, Password, Confirmpassword, MailId, Age, Gender, City) VALUES (%s, %s,%s,%s,%s,%s,%s)", (user, pwd, confirm_pwd, mail, age,gender,city))
        Connection.commit()
        messagebox.showinfo("Success", "Account created successfully!")
    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        cursor.close()
        Connection.close()

def login_fn(user, pwd):
     
    if user == "" or pwd == "":
        messagebox.showerror("Error !!", "All fields are required!")
        return
    
    Connection = db_connect()
    cursor = Connection.cursor()

    try:
        cursor.execute("SELECT * FROM login WHERE Username=%s AND Password=%s", (user, pwd))
        row = cursor.fetchone()
        if row:
            messagebox.showinfo("Success", f"Welcome {user}!")
            launch_game_hub()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        cursor.close()
        Connection.close()

def open_signup():
    signup = tk.Toplevel(root)
    signup.title("Sign Up")
    signup.geometry("600x600+200+0")
    signup.config(bg="#010416")

    form_frame = tk.Frame(signup, bg="#010416")
    form_frame.pack(pady=20)

    a=tk.Label(form_frame, text="🎮 Sign Up 🎮", font=("Consolas", 20, "bold"), bg="#010416",fg="#FF2E9A")
    a.grid(row=0, column=0, columnspan=2, pady=(0, 5))
    b=tk.Label(form_frame, text="Create your account", font=("Lucida Handwriting", 14), bg="#010416", fg="white")
    b.grid(row=1, column=0, columnspan=2, pady=(0, 20))

    c=tk.Label(form_frame, text="Username :", font=("Arial", 14, "bold"), bg="#010416", fg="white")
    c.grid(row=2, column=0, padx=15, pady=10, sticky="e")
    user_entry = tk.Entry(form_frame, bg="#1E1E2E", fg="white", insertbackground="white")
    user_entry.grid(row=2, column=1, sticky="w", padx=10)

    d=tk.Label(form_frame, text="Password :", font=("Arial", 14, "bold"), bg="#010416", fg="white")
    d.grid(row=3, column=0, padx=15, pady=10, sticky="e")
    pwd_entry = tk.Entry(form_frame, show="*", bg="#1E1E2E", fg="white", insertbackground="white")
    pwd_entry.grid(row=3, column=1, sticky="w", padx=10)


    e=tk.Label(form_frame, text="Confirm Password :", font=("Arial", 14, "bold"), bg="#010416", fg="white")
    e.grid(row=4, column=0, padx=15, pady=10, sticky="e")
    confirm_pwd_entry = tk.Entry(form_frame, show="*", bg="#1E1E2E", fg="white", insertbackground="white")
    confirm_pwd_entry.grid(row=4, column=1, sticky="w", padx=10)

    f=tk.Label(form_frame, text="Mail Id :", font=("Arial", 14, "bold"), bg="#010416", fg="white")
    f.grid(row=5, column=0, padx=15, pady=10, sticky="e")
    mail_entry = tk.Entry(form_frame, bg="#1E1E2E", fg="white", insertbackground="white")
    mail_entry.grid(row=5, column=1, sticky="w", padx=10)


    g=tk.Label(form_frame, text="Age :", font=("Arial", 14, "bold"), bg="#010416", fg="white")
    g.grid(row=6, column=0, padx=15, pady=10, sticky="e")
    age_entry = tk.Entry(form_frame, bg="#1E1E2E", fg="white", insertbackground="white")
    age_entry.grid(row=6, column=1, sticky="w", padx=10)


    h=tk.Label(form_frame, text="Gender :", font=("Arial", 14, "bold"), bg="#010416", fg="white")
    h.grid(row=7, column=0, padx=15, pady=10, sticky="e")
    gender_var = tk.StringVar()
    gender_var.set("Male")
    gender_frame = tk.Frame(form_frame, bg="#010416")
    gender_frame.grid(row=7, column=1, sticky="w")
    tk.Radiobutton(gender_frame, text="Male",font=("Arial", 12), variable=gender_var, value="Male", bg="#010416", fg="white", selectcolor="#1E1E2E").pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(gender_frame, text="Female",font=("Arial", 12), variable=gender_var, value="Female", bg="#010416", fg="white", selectcolor="#1E1E2E").pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(gender_frame, text="Other", font=("Arial", 12),variable=gender_var, value="Other", bg="#010416", fg="white", selectcolor="#1E1E2E").pack(side=tk.LEFT, padx=5)


    i=tk.Label(form_frame, text="City :", font=("Arial", 14, "bold"), bg="#010416", fg="white")
    i.grid(row=8, column=0, padx=15, pady=10, sticky="e")
    city_combo = Combobox(form_frame, state="readonly")
    city_combo['values'] = ["Chennai", "Coimbatore", "Madurai","Mumbai", "Delhi", "Bangalore", "Hyderabad", "Kolkata","Visakhapatnam","Cochin"  ]
    city_combo.set("Select City")
    city_combo.grid(row=8, column=1, sticky="w", padx=10)

    
    def signup_submit():
        data = [
          user_entry.get(),
          pwd_entry.get(),
          confirm_pwd_entry.get(),
          mail_entry.get(),
          age_entry.get(),
          gender_var.get(),
          city_combo.get()
         ]
        signup_fn(data)
    tk.Button(form_frame, text="Submit", command=signup_submit, width=15, height=2, bg="#1DB954", fg="white", font=("Arial", 12, "bold")).grid(row=9, column=0, columnspan=2, pady=20)



def open_login():
    login = tk.Toplevel(root)
    login.title("Login")
    login.geometry("500x400+200+0")
    login.config(bg="#010416")

    tk.Label(login, text="🎮 Login 🎮", font=("Consolas", 20, "bold"),bg="#010416",fg="white").pack(pady=20)

    tk.Label(login, text="Username",font=("Calibri",14,"bold"), bg="#5C1F4F",fg="white").pack()
    username_entry = tk.Entry(login, width=50)
    username_entry.pack(pady=5)

    tk.Label(login, text="Password",font=("Calibri",14,"bold"), bg="#5C1F4F",fg="white").pack()
    password_entry = tk.Entry(login, width=50, show="*")
    password_entry.pack(pady=5)


    def handle_login():
        user = username_entry.get()
        pwd = password_entry.get()
        login_fn(user, pwd)



    tk.Button(login,text="Launch Hub 🚀 ",font=("Orbitron",12,"bold"),bg="#75AD0D", fg="white",width=20,height=2,command=handle_login).pack(pady=20)



def launch_game_hub():
    hub = tk.Toplevel(root)
    hub.title("🎮 Game Selection")
    hub.geometry("800x600+0+0")
    hub.config(bg="#0F0F1E")

    tk.Label(hub, text="🎯 Choose Your Game", font=("Consolas", 22, "bold"), bg="#0F0F1E", fg="#FFD700").pack(pady=20)

    icon_frame = tk.Frame(hub, bg="#0F0F1E")
    icon_frame.pack(pady=20)

 
    rps_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\rps_icon.jpg" 
    rps_img = Image.open(rps_path).resize((100,100))
    rps_icon = ImageTk.PhotoImage(rps_img)

    rps_btn = tk.Button(icon_frame, image=rps_icon, command=rps_game, bg="#0F0F1E", borderwidth=0)
    rps_btn.image = rps_icon 
    rps_btn.grid(row=0, column=0, padx=50,pady=20)
    tk.Label(icon_frame, text="Rock Paper", fg="white", bg="#0F0F1E").grid(row=1, column=0)

    scramble_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\jumb_icon.jpeg"
    scramble_img = Image.open(scramble_path).resize((100,100))
    scramble_icon = ImageTk.PhotoImage(scramble_img)

    scramble_btn = tk.Button(icon_frame, image=scramble_icon, command=scramble_game, bg="#0F0F1E", borderwidth=0)
    scramble_btn.image = scramble_icon
    scramble_btn.grid(row=0, column=1, padx=20, pady=20)
    tk.Label(icon_frame, text="Scrambled Word", fg="white", bg="#0F0F1E").grid(row=1, column=1)

    quiz_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\quiz_icon.jpeg"
    quiz_img = Image.open(quiz_path).resize((100,100))
    quiz_icon = ImageTk.PhotoImage(quiz_img)
    quiz_btn = tk.Button(icon_frame, image=quiz_icon, command=quizgame, bg="#0F0F1E", borderwidth=0)
    quiz_btn.image = quiz_icon
    quiz_btn.grid(row=0, column=2, padx=50, pady=20)
    tk.Label(icon_frame, text="Quiz Time", fg="white", bg="#0F0F1E").grid(row=1, column=2)

    memory_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\memory_icon.png"
    memory_img = Image.open(memory_path).resize((100,100))
    memory_icon = ImageTk.PhotoImage(memory_img)
    memory_btn = tk.Button(icon_frame, image=memory_icon, command=emoji_memory_game, bg="#0F0F1E", borderwidth=0)
    memory_btn.image = memory_icon  
    memory_btn.grid(row=3, column=0, padx=50, pady=20)
    tk.Label(icon_frame, text="Memoji", fg="white", bg="#0F0F1E").grid(row=4, column=0)

    tfg_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\tf_icon.png"
    tfg_img = Image.open(tfg_path).resize((100,100))
    tfg_icon = ImageTk.PhotoImage(tfg_img)
    tfg_btn = tk.Button(icon_frame, image=tfg_icon, command=tf_game, bg="#0F0F1E", borderwidth=0)
    tfg_btn.image = tfg_icon
    tfg_btn.grid(row=3, column=1, padx=20, pady=20)
    tk.Label(icon_frame, text="True or False", fg="white", bg="#0F0F1E").grid(row=4, column=1)

    oe_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\oddeven_icon.png"
    oe_img = Image.open(oe_path).resize((100,100))  
    oe_icon = ImageTk.PhotoImage(oe_img)
    oe_btn = tk.Button(icon_frame, image=oe_icon, command=odd_or_even_game, bg="#0F0F1E", borderwidth=0)
    oe_btn.image = oe_icon
    oe_btn.grid(row=3, column=2, padx=50, pady=20)
    tk.Label(icon_frame, text="Odd or Even", fg="white", bg="#0F0F1E").grid(row=4, column=2)
    



    
    tk.Button(hub, text="Quit", command=hub.destroy, bg="#FF6347", fg="white", font=("Arial", 12, "bold")).pack(pady=20)




root= tk.Tk()
root.title("Welcome to Game Hub")
root.geometry("1600x900")
root.config(bg="navy blue")



image_path = r"C:\Users\taniy\OneDrive\Documents\PYTHON\PROJECT\back.png"
image = Image.open(image_path).resize((1600, 900))
img = ImageTk.PhotoImage(image)
bckg = tk.Label(root, image=img)  
bckg.place(x=0, y=0)

frame= tk.Frame(root, bg="#000000")
frame.place(relx=0.8, rely=0.5, anchor="center")
frame.config(padx=30, pady=30)

welcome= tk.Label(frame, text="Welcome to GameHub 🎮",font=("Audiowide", 26, "bold"), bg="black", fg="#BD336F")
welcome.pack(padx=5, pady=5)

line=tk.Label(frame, text="Where  fun  never  logs  out 😎 ", font=("Lucida Handwriting", 12), fg="#DCF293", bg="black")
line.pack(pady=5)

login=tk.Button(frame, text="🔐 Login",font=("Courier New",14,"bold"), width=15, height=3, bg="#400768", fg="white", command=open_login)
login.pack(padx=50, pady=30)


signup=tk.Button(frame, text="📝 Sign Up",font=("Courier New",14,"bold"), width=15, height=3, bg="#088931", fg="white", command=open_signup)
signup.pack()

quit_button = tk.Button(frame, text="Quit", font=("Arial", 10, "bold"), width=15, height=3, command=root.destroy, bg="#950E2D", fg="white")
quit_button.pack(padx=50, pady=30)

root.mainloop()



