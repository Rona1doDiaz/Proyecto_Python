def divisors(x):
    List_divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            List_divisors.append(i)
    return List_divisors

def run():
    try:
        x = int(input("ingrese un numero: "))
        assert x > 0, ""
        print(divisors(x))
    except ValueError:
        print("ingrese un numero entero")
    except AssertionError:
        print("Ingrese un numero mayor que 0")
if __name__ == "__main__":
    run() 