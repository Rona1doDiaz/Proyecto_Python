def run():
    pal = lambda x:x == x[::-1]
    print(pal(str(input("Ingrese una plabra: "))))
if __name__ == "__main__":  
    run()