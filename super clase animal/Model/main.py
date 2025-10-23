from Perro import Perro
from Vaca import Vaca
from Abeja import Abeja
from Animal import Animal

def main():
    p = Perro( "can", 7, "sergio" )
    v = Vaca ( "vacuno", 10, "alejandro" )
    a = Abeja ( "abejorro", 6, "vazquz" )

    p.hablar()
    p.moverse()

    v.hablar()
    v.moverse()

    a.hablar()
    a.moverse()
    a.picar()

    print(Perro.__bases__)
    print(Animal.__subclasses__())
    
if __name__ == "__main__":
    main()
