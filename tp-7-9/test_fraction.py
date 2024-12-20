from fraction import Fraction 

try:
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    f3 = Fraction(5, 0) 
except ValueError as e:
    print(f"Erreur lors de la création de f3 : {e}")

# test addition
try:
    result_add = f1 + f2
    print(f"{f1} + {f2} = {result_add}")
except Exception as e:
    print(f"Erreur lors de l'addition : {e}")

# test soustraction
try:
    result_sub = f1 - f2
    print(f"{f1} - {f2} = {result_sub}")
except Exception as e:
    print(f"Erreur lors de la soustraction : {e}")

# test multiplication
try:
    result_mul = f1 * f2
    print(f"{f1} * {f2} = {result_mul}")
except Exception as e:
    print(f"Erreur lors de la multiplication : {e}")

# test division
try:
    result_div = f1 / f2
    print(f"{f1} / {f2} = {result_div}")
except Exception as e:
    print(f"Erreur lors de la division : {e}")

# teqt égalité 
try:
    f4 = Fraction(3, 4)
    print(f"f2 == f4 ? {f2 == f4}")  # Cela devrait être vrai
except Exception as e:
    print(f"Erreur lors de l'égalité : {e}")

# test simplification de fraction
try:
    f5 = Fraction(2, 4)
    print(f"Fraction simplifiée de 2/4 : {f5}")
except Exception as e:
    print(f"Erreur lors de la création de f5 : {e}")


try:
    f_invalid = Fraction(3, 0)  # Cela devrait lever une exception
except ValueError as e:
    print(f"Erreur lors de la création de f_invalid : {e}")


# test as_mixed_number
try:
    result_mixed = f1.as_mixed_number()
    print(f"{f1} en nombre mixte = {result_mixed}")
except Exception as e:
    print(f"Erreur lors de la conversion en nombre mixte : {e}")

# test __pow__
try:
    result_pow = f1 ** 2
    print(f"{f1} ^ 2 = {result_pow}")
except Exception as e:
    print(f"Erreur lors de l'exponentiation : {e}")

# test __float__
try:
    result_float = float(f1)
    print(f"Valeur décimale de {f1} = {result_float}")
except Exception as e:
    print(f"Erreur lors de la conversion en float : {e}")

# test is_zero
try:
    print(f"f1 est-elle égale à zéro ? {f1.is_zero()}")
except Exception as e:
    print(f"Erreur lors de la vérification de zéro : {e}")

# test is_integer
try:
    print(f"f1 est-elle un entier ? {f1.is_integer()}")
except Exception as e:
    print(f"Erreur lors de la vérification de l'entier : {e}")

# test is_proper
try:
    print(f"f1 est-elle une fraction propre ? {f1.is_proper()}")
except Exception as e:
    print(f"Erreur lors de la vérification de la fraction propre : {e}")

# test is_unit
try:
    print(f"f1 est-elle une fraction unitaire ? {f1.is_unit()}")
except Exception as e:
    print(f"Erreur lors de la vérification de la fraction unitaire : {e}")

# test is_adjacent_to 
try:
    f6 = Fraction(1, 3)
    print(f"f1 est-elle adjacente à f6 ? {f1.is_adjacent_to(f6)}")
except Exception as e:
    print(f"Erreur lors de la vérification des fractions adjacentes : {e}")
