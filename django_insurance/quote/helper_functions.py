import random 

def create_quote_id():
    # Start the string with "d" and "j"
    result = "dj"
    # Append 6 randomly selected numbers from the range 1 to 10
    for _ in range(6):
        result += str(random.randint(1, 10))
    return result
