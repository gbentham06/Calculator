from Basic import basic_calc
import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry('400x200')

if __name__ == '__main__':
    def show_input():
        lbl.config(text=basic_calc(txt.get('1.0', 'end-1c')))


    # TextBox for input
    txt = tk.Text(root, height=5, width=40)
    txt.pack()

    # Button to print input
    btn = tk.Button(root, text="Calculate", command=show_input)
    btn.pack()

    # Label to display input
    lbl = tk.Label(root, text="")
    lbl.pack()

    root.mainloop()