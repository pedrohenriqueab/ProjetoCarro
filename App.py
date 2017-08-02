from Carro import *
from Hibrido import *

def main():
    carro1 = Carro("cinza", "fox", 2012)
    carro2 = Carro("preto", "HB20", 2013)
    carro3 = carro1
    print(Carro)
    print(carro2.cor)
    print(carro3)

if __name__ == "__main__":
    main()
