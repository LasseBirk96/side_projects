""""This is a simple BMI-calculator, i made to primarily practice with the tkinter library"""
import tkinter as tk
import random

# BMI-CALCULATOR #
def calculate_bmi(weight, height):
    """Calculates the BMI"""
    bmi = float(weight) / (float(height) / 100) ** 2
    return bmi


def get_label_based_on_bmi(bmi):
    """In Python3.10 you can use "match case" instead of the if-statements,
    :.1f" means the floating point number will be printed with one number behind the comma"""
    if bmi >= 30:
        return f"Your BMI is {bmi:.1f}! This is consired obeis!"
    if bmi_range(bmi, 25.0, 29.9):
        return f"Your BMI is {bmi:.1f}! This is consired overweight!"
    if bmi_range(bmi, 18.5, 24.9):
        return f"Your BMI is {bmi:.1f}! This is consired healthy weight!"
    if bmi < 18.5:
        return f"Your BMI is {bmi:.1f}! This is consired underweight!"


def bmi_range(bmi, first_number, second_number):
    """The range function in python only takes int, not float, so i wrote my own "range method"""
    if bmi > first_number and bmi < second_number:
        return True


def send_message_to_interface(message):
    """Takes a message and send it to the interface"""
    label.config(text=message)
    canvas1.create_window(200, 230, window=label)


def get_and_send_bmi_result_to_interface():
    """The method gets the bmi,
    the label based on that bmi,
    and sends it to the "send_message_to_interface"""
    try:
        bmi = calculate_bmi(weight_field.get(), height_field.get())
        message = get_label_based_on_bmi(bmi)
        send_message_to_interface(message)
    except ValueError:
        send_message_to_interface("ERROR: Please enter valid data in both fields")
    except ZeroDivisionError:
        send_message_to_interface("ERROR: Please enter valid data in both fields")


def change_color(event=None):
    """Changes color on the header, if clicked"""
    array_of_colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
    random_number = random.randint(0, len(array_of_colors) - 1)
    header.config(fg=array_of_colors[random_number])


# INTERFACE #

# Creates the blank interface
root = tk.Tk()
root.title("BMI-CALCULATOR")
canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack(pady=10)

# Creates the header and binds method
header = tk.Label(root, text="Totally Sick BMI Calculator")
header.bind("<Button-1>", change_color)
canvas1.create_window(200, 100, window=header)

# The field that handles the weight field
weight_field = tk.Entry(root)
canvas1.create_window(200, 140, window=weight_field)
canvas1.create_text(65, 140, text="Weight (kg)")

# The field that handles the height field
height_field = tk.Entry(root)
canvas1.create_window(200, 170, window=height_field)
canvas1.create_text(65, 170, text="Height (cm)")

# This is the submit button, called "Calculate BMI"!
button = tk.Button(
    text="Calculate BMI",
    activeforeground="#B1B0B0",
    command=get_and_send_bmi_result_to_interface,
)
canvas1.create_window(200, 200, window=button)

# This creates the label that shows the bmi results in the interface
label = tk.Label(root, text="")

# mainloop() roughly updates the state of the interface, it also blocks all code coming after it
root.mainloop()
