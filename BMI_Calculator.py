import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        height_unit = height_unit_var.get()
        
        if height_unit == "cm":
            height /= 100  # Convert cm to meters
        elif height_unit == "feet":
            height *= 0.3048  # Convert feet to meters
        
        if height <= 0 or weight <= 0:
            raise ValueError("Height and Weight must be positive numbers.")
        
        bmi = weight / (height ** 2)
        bmi_result.set(f"BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight"
            color = "blue"  # Set color to blue for underweight
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            color = "green"  # Set color to green for normal weight
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "orange"  # Set color to orange for overweight
        else:
            category = "Obesity"
            color = "red"  # Set color to red for obesity
        
        bmi_category.set(f"Category: {category}")
        label_category.config(foreground=color)  # Set label color based on category
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x250")
root.resizable(False, False)

# Create a frame for the input fields
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Height input
ttk.Label(frame, text="Height:").grid(row=0, column=0, padx=5, pady=5)
entry_height = ttk.Entry(frame)
entry_height.grid(row=0, column=1, padx=5, pady=5)
height_unit_var = tk.StringVar(value="m")
height_unit_menu = ttk.OptionMenu(frame, height_unit_var, "m", "m", "cm", "feet")
height_unit_menu.grid(row=0, column=2, padx=5, pady=5)

# Weight input
ttk.Label(frame, text="Weight (kg):").grid(row=1, column=0, padx=5, pady=5)
entry_weight = ttk.Entry(frame)
entry_weight.grid(row=1, column=1, padx=5, pady=5)

# Calculate button
button_calculate = ttk.Button(frame, text="Calculate", command=calculate_bmi)
button_calculate.grid(row=2, column=0, columnspan=3, pady=10)

# Result display
bmi_result = tk.StringVar()
bmi_category = tk.StringVar()
label_result = ttk.Label(frame, textvariable=bmi_result, font=('Arial', 12))
label_result.grid(row=3, column=0, columnspan=3, pady=5)
label_category = ttk.Label(frame, textvariable=bmi_category, font=('Arial', 12))
label_category.grid(row=4, column=0, columnspan=3, pady=5)

# Run the application
root.mainloop()
