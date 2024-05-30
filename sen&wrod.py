talk = input("talk: ")
code = ""

for char in talk:
    if char == "A" or char == "a":
        code += "2"
    elif char == "B" or char == "b":
        code += "22"
    elif char == "C" or char == "c":
        code += "222"
    elif char == "D" or char == "d":
        code += "3"
    elif char == "E" or char == "e":
        code += "33"
    elif char == "F" or char == "f":
        code += "333"
    elif char == "G" or char == "g":
        code += "4"
    elif char == "H" or char == "h":
        code += "44"
    elif char == "I" or char == "i":
        code += "444"
    elif char == "J" or char == "j":
        code += "5"
    elif char == "K" or char == "k":
        code += "55"
    elif char == "L" or char == "l":
        code += "555"
    elif char == "M" or char == "m":
        code += "6"
    elif char == "N" or char == "n":
        code += "66"
    elif char == "O" or char == "o":
        code += "666"
    elif char == "P" or char == "p":
        code += "7"
    elif char == "Q" or char == "q":
        code += "77"
    elif char == "R" or char == "r":
        code += "777"
    elif char == "S" or char == "s":
        code += "7777"
    elif char == "T" or char == "t":
        code += "8"
    elif char == "U" or char == "u":
        code += "88"
    elif char == "V" or char == "v":
        code += "888"
    elif char == "W" or char == "w":
        code += "9"
    elif char == "X" or char == "x":
        code += "99"
    elif char == "Y" or char == "y":
        code += "999"
    elif char == "Z" or char == "z":
        code += "9999"
    elif char == " ":
        code += "0"
    elif char == ".":
        code += "d"
    elif char == ",":
        code += "c"
    elif char == "*":
        code += "<-"
    elif char == "/":
        code += "->"
    elif char == "-":
        code += "top"
    elif char == "-":
        code += "bottom"
    else:
        code += char


print(code)