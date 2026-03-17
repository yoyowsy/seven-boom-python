lst = input("enter list:")

def seven_boom(lst):
    all_digits = "".join(str(num) for num in lst)
    count = all_digits.count("7")
    if (count > 0):
        return "Boom! "* count
    else:
        return "there is no 7 in the array"
        

clean_lst = lst.strip("[]").replace(" ","").split(",")

print(seven_boom(clean_lst))
