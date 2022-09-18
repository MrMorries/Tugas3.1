import math
from math_function import add,sub, multi



def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = add(data_1, data_2)
    elif operator == "*":
        result = multi( data_1,data_2)
    elif operator =="/":
        result = sub(data_1,data_2)
    else :
        print("ERROR")

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()