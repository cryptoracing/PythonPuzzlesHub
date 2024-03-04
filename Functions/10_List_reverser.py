def reverse_list(input_list):
    return input_list[::-1]

def main():
    input_list = input("List: ")
    input_list = eval(input_list)  # Convert the input string to a list
    reversed_list = reverse_list(input_list)
    print("Reversed List:", reversed_list)

main()