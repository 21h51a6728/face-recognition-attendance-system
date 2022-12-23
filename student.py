from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=700)

        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current course details",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=135,width=720,height=200)

        dep_label=Label(current_course_frame,text="department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17)
        dep_combo
        dep_combo.grid(row=0,column=1)
         # right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=730,height=700)

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()