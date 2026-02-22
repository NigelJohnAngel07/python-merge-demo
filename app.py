# app.py

def greet():
    print("Hello from LOGGING + ANALYTICS branch!")

def about():
    print("This project demonstrates Git merging and rebasing.")
    print("Logging and Analytics features are both active.")

def calculate_sum(a, b):
    result = a + b
    print(f"Calculating sum of {a} and {b}")
    print(f"[ANALYTICS] Tracking sum operation for {a} and {b}")
    return result

def calculate_difference(a, b):
    result = a - b
    print(f"Calculating difference of {a} and {b}")
    print(f"[ANALYTICS] Tracking difference operation for {a} and {b}")
    return result

def new_logging_feature():
    print("Logging system initialized.")

def analytics_report():
    print("Generating analytics report...")

def main():
    greet()
    about()
    new_logging_feature()
    analytics_report()
    print("Sum:", calculate_sum(10, 5))
    print("Difference:", calculate_difference(10, 5))

if __name__ == "__main__":
    main()
  