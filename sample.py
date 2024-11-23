def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    # Example usage
    print(add(10, 5))
    print(subtract(10, 5))
    print(multiply(10, 5))
    print(divide(10, 5))

    print(divide(10, 0))  # This will raise an exception
    print("lsgo")