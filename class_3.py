from functools import reduce
#Filtrand DATOS

DATABASE = [
    {
        "name": "Ronaldo",
        "job": "not job",
    },
    {
        "name": "Carlos",
        "job": "jobss",
    },
    {
        "name": "Ramiro",
        "job": "jobss",
    },
    {
        "name": "Franco",
        "job": "jobss ",
    },
    {
        "name": "juan",
        "job": "not job",
    }
]

def run():
    en=str(input("ingrese el filtro: "))
    li = [i["name"] for i in DATABASE if i["job"]==en]

    for i in li:
        print(i)
if __name__ == "__main__":
    run() 