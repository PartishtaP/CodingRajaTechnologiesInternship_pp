from tkinter import *

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do-List')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do-List-App', font='ariel, 25 bold', width=10, bd=5, bg="yellow",
                           fg="black")
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task', font='ariel, 18 bold', width=10, bd=5, bg="yellow",
                            fg="black")
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='To-Do-List-App', font='ariel, 18 bold', width=10, bd=5, bg="yellow",
                            fg="black")
        self.label3.place(x=320, y=58)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=280, y=120)

        self.text = Text(self.root, height=2, bd=5, width=30, font="ariel, 10 bold")
        self.text.place(x=20, y=120)

        self.button = Button(self.root, text="Add", font='sarif, 20 bold italic', width=10, bd=5, bg='pink',
                             fg='black', command=self.add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='sarif, 20 bold italic', width=10, bd=5, bg='pink',
                              fg='black', command=self.delete)
        self.button2.place(x=30, y=280)

        # Initialize widgets
        self.load_tasks_from_file()

    def add(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content)
        self.text.delete(1.0, END)

    def delete(self):
        delete_ = self.main_text.curselection()
        self.main_text.delete(delete_)

    def load_tasks_from_file(self):
        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    self.main_text.insert(END, line)
        except FileNotFoundError:
            pass

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
