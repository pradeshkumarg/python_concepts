try:
    with open("random.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

try:
    file = open("example.txt", "r")
    # Perform some operations on the file
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    # This block will always be executed
    # Regardless of whether an exception occurred or not
    print('file' in locals())
