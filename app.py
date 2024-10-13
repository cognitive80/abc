# Install streamlit if not already installed (in Colab or local machine)
# !pip install streamlit

import streamlit as st

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Streamlit UI
st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Enter the first number", step=1e-1, format="%.2f")
num2 = st.number_input("Enter the second number", step=1e-1, format="%.2f")

# Select operation
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.write(f"The result of {num1} + {num2} is {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.write(f"The result of {num1} - {num2} is {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.write(f"The result of {num1} * {num2} is {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.write(f"The result of {num1} / {num2} is {result}")
