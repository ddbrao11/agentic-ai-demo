def calculate_square_root(text):
    import math
    try:
        num = float(text)
        return str(math.sqrt(num))
    except Exception as e:
        return f"Error: {e}"

def write_to_file(text):
    try:
        with open("output.txt", "w") as f:
            f.write(text)
        return "Written to output.txt"
    except Exception as e:
        return f"Error: {e}"

tools = {
    "CalculateSquareRoot": calculate_square_root,
    "WriteToFile": write_to_file
}
