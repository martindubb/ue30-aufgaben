# CODE 1
def print_list(list):
    l = len(list)
    for i in range(l):
        i += 1
        print(i, list[i])

obst = ["Banane","Kirsche","Apfel","Mango","Ananas"]
autos = ["BMW","Mercedes","Volkswagen","Audi"]

print_list(obst)
print_list(autos)
