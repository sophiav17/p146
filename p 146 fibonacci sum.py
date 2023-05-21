from tkinter import*

root = Tk()

root.title("Fibonacci Sum")
root.geometry("400x400")
root.configure(background = "pink")

take_input = Entry(root)
fibonacci_series = Label(root)
fibonacci_sum = Label(root)

def fibonacci() :
    get_input = take_input.get()
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    sum2 = 0
    while (counter <= get_input) :
        fibonacci_series["text"] = "Fibonacci Series: " + str(sum) + " "
        fibonacci_sum["text"] = "Fibonacci Sum: " + str(sum2)
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + sum
 
btn = Button(root, text = "Show Fibonacci Series", command = fibonacci, bg = "purple", fg = "white")
take_input.pack()
btn.pack()
fibonacci_series.pack()
fibonacci_sum.pack() 
        
root.mainloop()