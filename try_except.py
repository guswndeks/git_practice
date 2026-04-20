try:
    a = [1, 2, 3]
    print(a[5])  # This will raise an IndexError
except Exception as e:
    # Handle the exception
    print(f"An error occurred: {e}")

finally:
    print("This block will always execute, regardless of exceptions.")