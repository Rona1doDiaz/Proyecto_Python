val = True
while val == True:
    let = str(input("ingrese una letra: "))
    if len(let.replace(" ","")) != 1 or let.isdigit():
        pass
    else:
        val = False
print("ok")