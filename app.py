# app.py

def greet():
    print("Hello from MAIN branch!")

def about():
    print("This project demonstrates Git merging and rebasing.")

def calculate_sum(a, b):
    return a + b

def calculate_difference(a, b):
    return a - b

def main():
    greet()
    about()
    print("Sum:", calculate_sum(10, 5))
    print("Difference:", calculate_difference(10, 5))

if __name__ == "__main__":
    main()