# CODE 3
x = 0
while x < 12:
    x + 1
    name = "datei"+str(x)+".txt"
    open(name, "a")
    print("datei", name, "erstellt")