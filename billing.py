print("CHOOSE YOUR AMOUNT \n-->\n₹375, ₹244, ₹456,₹35:")
amt = float(input("Enter the amount of your odered item:\t \t \n-->"))
a = None
def bill(a):
    if amt <= 300 and amt >= 50:
        return amt*0.2
    elif amt >= 300 or amt <= 50:
        return amt * 0.15
    else:
        print("Talk to the Manager")
print(f"total tip:- ₹{bill(a)}/-\n")
print(f"Your ordered item ₹{amt}/-\n")
print(f"Your total PAYMENT ₹{amt + bill(a)}/-\n")
print("\n\t!!!...THANKS FOR VISITING...!!!")
