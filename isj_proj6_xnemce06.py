class Polynomial():
    """Trieda reprezentujúca polynom"""

    def __init__(self, *args, **kwargs):
        """
        Inicializácia polynómu
        """
        self.polynom = list()
        if args and isinstance(args[0], list):
            self.polynom = args[0] #koeficienty sú zadané ako zoznam
        elif args:
            self.polynom = args #koeficienty sú zadané ako čísla
        else:
            #koeficienty sú zadané s indexom
            for name, value in kwargs.items():
                for i in range(1+int(name.split("x")[1]) - len(self.polynom)):
                    self.polynom.append(0)
                self.polynom[int(name.split("x")[1])] = value


    def __str__(self):
        """
        str metóda
        vstup: self
        výstup: Polynóm v správnej forme stringu
        """
        Polynom_List = []
        if len(self.polynom) > 0:
            for i in range(len(self.polynom)):
                if self.polynom[i] == 0:
                    continue #vynechanie nulových hodnôt
                if self.polynom[i] > 0: #osetrenie znamienka
                    sign = " + "
                else:
                    sign = ""
                if i > 1: #x^i
                    x = sign + str(self.polynom[i]) + "x^" + str(i)
                elif i == 1: #x
                    x = sign + str(self.polynom[i]) + "x"
                else: #x^0
                    x = sign + str(self.polynom[i])
                Polynom_List.insert(0, x)

        if len(Polynom_List) == 0:
            return "0"

        Equation = ''.join(Polynom_List).replace('-', ' - ').replace('1x', 'x') #spojenie listu na string a úprava
        if Equation[1] == '+':
            Equation = Equation[3:]
        return Equation

    def __eq__(self, other):
        """
        Rovnosť polynómov
        vstup: 2 polynómy pre porovnávanie
        výstup: výsledok rovnosti => True/False
        """
        if str(self) == str(other):
            return True
        else:
            return False

    def __add__(self, other):
        new_polynom = self.polynom[:]
        i = 0
        for tmp_digits, o_digits in zip(self.polynom, other.polynom):
            new_polynom[i] = tmp_digits + o_digits #iteracia cez koeficienty rovnakej mocniny
            i += 1
        if(len(self.polynom) < len(other.polynom)): #prvý polenom obsahuje menej koeficientov
            for i in range(len(self.polynom), len(other.polynom)):
                new_polynom.append(other.polynom[i]) #pridanie zvysných koeficientov

        return Polynomial(new_polynom)

    def __pow__(self, power):
        """
        metóda pre umocňovanie
        vstup: self, mocnina
        výstup: umocnený polynóm
        """
        if power < 0: #záporná mocnina
            raise ValeuError("Power has to be positive number")
        elif power == 0: #nulová mocnina
            return Polynomial(1)
        elif power == 1: #mocnina 1
            return self
        else:
            i = 1
            base = self.polynom
            while i < power: #pocet cyklov výpočtu podla hodnoty mocniny
                a = 0
                b = 0
                new_polynom = [0]*(len(base) + len(self.polynom)+1) #prázdny list na výsledky
                while a < len(self.polynom):
                    while b < len(base):
                        new_polynom[a+b] += self.polynom[a] * base[b] #medzivýpočet
                        b += 1
                    a += 1
                    b = 0
                base = new_polynom #uloženie výsledku do dočastnej premennej
                i += 1
            return Polynomial(new_polynom)

    def derivative(self):
        """
        Derivácia
        vstup: self
        výstup: zderivovaný polynóm
        """
        new_polynom = [0]*(len(self.polynom)+1) #prázdny list na výsledky
        for i, item in enumerate(self.polynom): #výpočet derivácie všetkých členov
            if i != 0:
                new_polynom[i-1] = item *i
            else:
                new_polynom[i] = 0
        return Polynomial(new_polynom)


    def at_value(self, x, *y):
        """
        Výpočet hodnoty
        vstup: self, hodnota x, voliteľná hodnota y
        výstup: numerický výsledok rovnice s hodnotou x alebo rozdiel rovníc y-x
        """
        result_x = 0
        result_y = 0

        for i in range(len(self.polynom)):
            result_x += self.polynom[i] * (x ** i) #výpočet polynómu s hodnotou x
            if len(y) != 0:
                result_y += self.polynom[i] * (y[0] ** i) #výpočet polyómu s hodnotou y
        if not y:
            return result_x
        else:
            return result_y - result_x


def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
