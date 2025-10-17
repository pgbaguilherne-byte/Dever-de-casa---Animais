class Animal():
    def __init__(self, nome, familia, especie):
        self.nome = nome
        self.familia = familia
        self.especie = especie

    def falar(self, som):
        print(f"{self.nome} faz: {som}")


animal1 = Animal("Leão", "Felídeos", "Panthera leo")
animal1.falar("Rawr")

animal2 = Animal("Gato", "Felino", "gatitos felinus")
animal2.falar("miauuuu")

animal3 = Animal("Ben-te-vi", "Tiranídeos", "Bentevinius")
animal3.falar("Ben-te-vi")

animal4 = Animal("Cachorro", "Canideo", "Minicaninos")
animal4.falar("Auau")

animal5 = Animal("Cascavel","Repteis","Cobraços")
animal5.falar("ssssss")

animal6 = Animal("Coruja", "Strigiformes", "edwingius")
animal6.falar("hu-hu")

animal7 = Animal("Sapo", "anfibios", "frokies")
animal7.falar("croac-croac") 
