# calculator.py
import streamlit as st


# Function to perform addition
def add(num1, num2):
    return num1 + num2


# Function to perform subtraction
def subtract(num1, num2):
    return num1 - num2


# Function to perform multiplication
def multiply(num1, num2):
    return num1 * num2


# Function to perform division
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero!"
    else:
        return num1 / num2


def main():
    st.title("Dr. Rabia Nazar Calculator")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    operation = st.selectbox(
        "Select operation",
        ("+", "-", "*", "/")
    )

    result = 0.0

    if st.button("Calculate"):
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        st.success(f"Result: {result}")

        # Display calculation history
        if 'history' not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append(f"{num1} {operation} {num2} = {result}")

    # Display history of calculations
    st.sidebar.header("Calculation History")
    if 'history' in st.session_state:
        for calc in reversed(st.session_state.history):
            st.sidebar.write(calc)


if __name__ == "__main__":
    main()
