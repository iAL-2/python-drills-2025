def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Enter a valid number. ")
        return None
    