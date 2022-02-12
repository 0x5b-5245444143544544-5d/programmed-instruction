from tkinter import *
from tkinter import font as tkfont
from tkinter import messagebox
from csv_parser import parse_csv

total_score = 0
clue_counter = 0

def draw_main_window():
    top = Tk()
    top.geometry("1280x720")
    # Code to add widgets will go here...
    font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
    label = Label(top, text="Click the button to start the test!", font=font)
    button = Button(top, text="Start Test", command=lambda: start_test(top))
    label.pack()
    button.pack()
    top.mainloop()

def start_test(top_window):
    top_window.destroy()
    test_questions = parse_csv()
    for question in test_questions:
        create_test_window(question)
    show_results(test_questions)
    
def create_test_window(question: dict):
    top = Tk()
    top.geometry("1280x720")
    font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
    Label(top, text=question['question'], font=font).pack()
    var = IntVar()
    var.set(1)
    values = {
        question['choice1']: 1,
        question['choice2']: 2,
        question['choice3']: 3,
        question['choice4']: 4
    }
    for (text, value) in values.items():
        Radiobutton(top, text=text, variable=var, value=value).pack()

    answer_placeholder = Label(top, text="", fg="#03fc30", font=font)
    button = Button(top, text="Submit!", command=lambda: check_question_response(top ,answer_placeholder, question, var))
    button.pack()
    answer_placeholder.pack()
    top.mainloop()

def check_question_response(top, answer_placeholder, question, var):
    global total_score, clue_counter
    ans = question['answer']
    if var.get() == int(ans):
        messagebox.showinfo("Excellent!", "Well done!")
        total_score += 1
        clue_counter = 0
        top.destroy()
    else:
        messagebox.showinfo("Clue", question[f'clue{clue_counter+1}'])
        clue_counter+=1
        if clue_counter == 3:
            answer_radio_button = "!radiobutton" + ("" if ans == '1' else ans)
            answer_radio_button = top.nametowidget(answer_radio_button)
            answer_radio_button.cofnfigure(bg="#03fc30")
            answer_placeholder.config(text="Answer: " + question[f'choice{question["answer"]}'])
            top.nametowidget('!button').pack_forget()
            Button(top, text="Next", command=top.destroy).pack()
            clue_counter = 0

def show_results(questions: list):
    top = Tk()
    global total_score
    top.geometry("1280x720")
    # Code to add widgets will go here...
    font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
    label = Label(top, text=f"Your Score is: {total_score}/{len(questions)}", font=font).pack()
    total_score = 0
    Button(top, text="Exit!", command=top.destroy).pack()
    Button(top, text="Retry", command=lambda: start_test(top)).pack()    


            

draw_main_window()