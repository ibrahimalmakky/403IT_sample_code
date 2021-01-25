
while True:
    try:
        inp_val = input("Please enter a number to be divided. Else to quit enter q.")
        inp_num = int(inp_val)
    except:
        if inp_val == "q":
            break
        else:
            print("Invalid input by user")
            continue
    input_num2 = int(input("Please enter another number"))
    # Arithmetic error that would happen when input_num2 = 0
    print(inp_num / input_num2)
