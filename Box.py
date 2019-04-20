class Box:
    def __init__(self, rune=""):
        self.rune = rune
    
    def is_empty(self):
        return self.rune == ""

    def fill(self, new_rune):
        self.rune = new_rune
     
if __name__ == "__main__":
    fila = list()
    for i in range(3):
        fila.append(Box("Y"))
    fila[1].fill("X")

    for box in fila:
        print(box.rune, end=' ')
    print("")