def calculate_average(list):
    result = 0
    for item in list:
        result+=item
    result = result/len(list)
    return result

length = int(input("Enter the length\n"))
list=[]
for i in range (length):
    list.append(int(input(f"Enter {i+1} number\n")))

print(calculate_average(list))