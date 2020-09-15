import tkinter as tk


#   Define Button Commands

def Calculate():
    calculate_result = weight_entry/(height_entry**2)

def Exit():
    exit()





win = tk.Tk()
win.title("BMI Calculator BY Sian")
#win.configure(bg="skyblue")
win.geometry("600x400")
win.resizable(False,False)


#Set TITLE
bmi_title_lb = tk.Label(win, text="Body Mass Index", bg="skyblue", font="Calibri 35")
bmi_title_lb.pack(fill='x')

#label entry_height(meter)
entry_height = tk.Label(win, text="Enter your height (meter):", font="Calibri 20")
entry_height.pack()



#height entry
height_entry = tk.Entry(win, borderwidth=3)
height_entry.pack()



#label entry_weight(kilogram)
entry_height = tk.Label(win, text="Enter your weight (kilogram):", font="Calibri 20")
entry_height.pack()


#height entry
weight_entry = tk.Entry(win, borderwidth=3)
weight_entry.pack()
str(weight_entry)


#define calculate_btn
calculate_btn = tk.Button(win, text="Calculate", font="Calibri 25", command=Calculate)
calculate_btn.pack()


#define exit_btn
exit_btn = tk.Button(win, text="Exit", font="Calibri 25", command=Exit)
exit_btn.pack()





win.mainloop()