import math

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : den != 0 le dénominateur doit être différent de 0 pour ne pas obtenir une erreur
        POST : créer une fraction 
        """
        if den == 0:
            raise ValueError("le dénominateur ne peut pas être égale à 0")
        
        gcd = math.gcd(num, den) 
        self._numerator = num // gcd
        self._denominator = den // gcd

        if self._denominator < 0:
            self._numerator = -self._numerator
            self._denominator = -self._denominator

    @property
    def numerator(self):
        return self._numerator
    @property
    def denominator(self):
        return self._denominator


# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : ?
        POST : ?
        """
        return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : ?
        POST : Retourne une chaîne représentant la fraction sous forme de nombre mixte
        """
        integer_part = self.numerator // self.denominator  #partie entière
        remainder = abs(self.numerator) % self.denominator  #reste de la division
        if remainder == 0:
            return str(integer_part)  
        else:
            return f"{integer_part} {remainder}/{self.denominator}"  

    
# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Additionner deux fractions.

        PRE : `other` doit etre une instance de la classe fraction.
        POST : retourne une nouvelle fraction qui est la somme des deux fractions.
        """

        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction")

        common_denominator = self.denominator * other.denominator # pour addtioner il faut un dénominateur commun 
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator

        return Fraction(new_numerator, common_denominator)


    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : `other` doit etre une instance de la classe fraction.
        POST : retourne une nouvelle fraction mais qui cette fois ci est la soustraction des deux fractions
        """
        common_denominator = self.denominator * other.denominator
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator

        return Fraction(new_numerator, common_denominator)


    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : encore une fois other doit etre une instance de la classe fraction 
        POST : retourne la multiplication des deux fractions
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)


    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other ==> instance de la classe fraction 
        POST : retourne une novuelle fraction qui est la division des deux
        """
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        return Fraction(new_numerator, new_denominator)


    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other doit etre un int
            si other < 0 alors self.numerator doit être différent de 0

            exemple : (0/2)^-1 = (2/0) ==> division par 0 qui doit absolument être évité 

        POST : retourne une fraction qui est elevé a la fraction exposant other
        """

        if not isinstance(other, int):
            raise TypeError("L'exposant doit être un entier")  # Vérifie que other est un entier.
        if other < 0 and self.numerator == 0:
            raise ValueError("La fraction ne peut pas être inversée car son numérateur est 0")  # Évite la division par zéro.


        if other < 0:
            num = self.denominator ** abs(other) 
            den = self.numerator ** abs(other)
        else:
            num = self.numerator ** other
            den = self.denominator ** other

        return Fraction(num, den)
    
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : other doit être une instance de fraction
        POST : return True si les 2 fraction sont égaux 
        
        """

        return self.numerator == other.numerator and self.denominator == other.denominator
        
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : la fraction doit être correctement initialisée (numérateur et dénominateur non nuls).
        POST : retourne la valeur décimale correspondant à la fraction, c'est-à-dire le résultat de la division
           du numérateur par le dénominateur.
        """
        return self.numerator / self.denominator
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)




# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : aucun
        POST : Retourne True si la fraction est égale à zéro, sinon False
        """
        return self.numerator == 0


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : Aucun prérequis 
        POST : Retourne True si la fraction représente un entier, sinon False.
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : aucun prérequis
        POST : retourne True si la fraction est propre 
        """
        return abs(self.numerator) < self.denominator

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : aucun prérequis
        POST : retourne True si le numérateur est égal à 1 dans la forme réduite de la fraction, sinon False.
        """
        return self.numerator == 1

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction

        PRE : 'other` doit être une instance de la classe `Fraction`
        POST : Retourne True si la différence absolue entre les deux fractions est une fraction unitaire 
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'objet comparé doit être une instance de Fraction")

        numerator_diff = abs(self.numerator * other.denominator - self.denominator * other.numerator)
        denominator_diff = self.denominator * other.denominator

        return numerator_diff == 1 and denominator_diff > 0

