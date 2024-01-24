def calcu_area(length,width):
    if length == width:
        return "square"
    else:
        a=length+width
        return a
def main():
    length=float(input("enter length : "))
    width=float(input("enter width : "))
    result=calcu_area(length,width)
    print(result)
if __name__ == "__main__":
    main()
