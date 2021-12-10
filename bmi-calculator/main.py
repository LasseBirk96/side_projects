
import tkinter as tk
import random


#Calculates the BMI
def calculate_bmi(weight, height):
    bmi = float(weight) / (float(height)/100)**2
    return bmi

#In Python3.10 you can use "match case" instead of the if-statements but i don't like python3.10 yet
#":.1f" means the floating point number will be printed with one number behind the comma
def get_label_based_on_bmi(bmi): 
    if bmi >= 30:
        return return_and_print_message("Your BMI is {:.1f}! This is consired obeis!".format(bmi))
    if bmi_range(bmi, 25.0, 29.9):
       return return_and_print_message("Your BMI is {:.1f}! This is consired overweight!".format(bmi))
    if bmi_range(bmi, 18.5, 24.9):
        return return_and_print_message("Your BMI is {:.1f}! This is consired healthy weight!".format(bmi))
    if bmi < 18.5:
        return return_and_print_message("Your BMI is {:.1f}! This is consired underweight!".format(bmi))

#The range function in python only takes int, not float, so i wrote my own "range method"
#If the bmi is larger than the first_number, but smaller than the second_number, then it must be in range
def bmi_range(bmi, first_number, second_number):
    if bmi > first_number and bmi < second_number:
        return True

#I like printing what i return, so i made method that does just that
def return_and_print_message(message):
    print(message)
    return message

#This method updates the label and sends it to the interface
def send_message_to_interface(message):
        label.config(text=message)
        canvas1.create_window(200, 230, window=label)


#The method gets the bmi, the label based on that bmi, and sends it to the "send_message_to_interface"
def get_and_send_bmi_result_to_interface():
    try: 
        bmi = calculate_bmi(weight.get(), height.get())
        message = get_label_based_on_bmi(bmi)
        send_message_to_interface(message)
    except ValueError:
        send_message_to_interface("ERROR: Please enter valid data in both fields")
    except ZeroDivisionError:
        send_message_to_interface("ERROR: Please enter valid data in both fields")

#Method that allows the title to change colour, minor easter egg
#You need the "even=None", otherwise you can't bind the command later
array_of_colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
def change_color(event=None):
        random_number = random.randint(0, len(array_of_colors) - 1)
        header.config(fg=array_of_colors[random_number])

#Creates the blank interface
root= tk.Tk()
root.title("BMI-CALCULATOR")
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack(pady=10)

#Creates the header and binds method
header = tk.Label(root,text="Totally Sick BMI Calculator")
header.bind("<Button-1>",change_color)
canvas1.create_window(200, 100, window=header)

#The field that handles the weight field
weight = tk.Entry(root) 
canvas1.create_window(200, 140, window=weight)
canvas1.create_text(65, 140, text = "Weight (kg)")

#The field that handles the height field
height = tk.Entry(root) 
canvas1.create_window(200, 170, window=height)
canvas1.create_text(65, 170, text = "Height (cm)")

#This is the submit button, called "Calculate BMI"! It calls a given method in the "command" parametre
button = tk.Button(text='Calculate BMI', activeforeground="#B1B0B0", command=get_and_send_bmi_result_to_interface)
canvas1.create_window(200, 200, window=button)

#This creates the label that shows the bmi results in the interface
label = tk.Label(root, text = '')

#mainloop() roughly updates the state of the interface, it also blocks all code coming after it
root.mainloop()


