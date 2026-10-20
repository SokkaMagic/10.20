# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = []
TopOfStack = -1
for i in range(8):
    Stack.append("")
# Write code here to fill Stack with 8 elements, all "" (empty string)


def Push(Word):
    global Stack, TopOfStack
    if TopOfStack == 7:
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = Word
        return True


def Pop():
    global TopOfStack, Stack
    if TopOfStack == -1:
        return False
    else:
        Stack[TopOfStack] = ""
        TopOfStack -= 1
        return True


def GetText():
    global TopOfStack, Stack
    text = ""
    for i in range(TopOfStack):
        text = text + Stack[i]
        text = text +"\n"
    text = text + Stack[TopOfStack]
    return text


# Exercise 2
def DecimalToBinary(Number):
    bin=""
    global TopOfStack, Stack
    TopOfStack = -1
    if Number == 0:
        return "0"
    while Number != 0:
        bin = bin + str(Number%2)
        Number = Number //2
    return bin
