def read():
    num =[]
    with open("./archivos/numero.txt", "r", encoding="utf-8") as rd:
        for line in rd:
            num.append(int(line))
    print(num)
def write():
    pass

def run():
    read()

if __name__ == "__main__":
    run()