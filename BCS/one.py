print("one.py is running")

print(f"Name inside one.py is {__name__}")


def foo():
    print("Inside foo")


if __name__ == "__main__":
    print("one.py is the main file")
else:
    print("one.py is being imported")