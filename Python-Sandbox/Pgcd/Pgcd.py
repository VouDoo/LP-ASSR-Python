def pgcd_basicAlgo(a, b) :
    i = max(a, b)
    while i != 0 :
        if a % i == 0 and b % i == 0 :
            return i
        i -= 1
    return 1

def pgcd_optimalAlgo(a, b):
    while b != 0:
        a,b = b, a % b
    return a

def pgcd_recursiveAlgo(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd_recursiveAlgo(b, r)

nbr_a, nbr_b = map(int, input("Enter two numbers : ").split())

print('*** Basic algorithm ***')
print("PGCD of", nbr_a, "and", nbr_b, ":", pgcd_basicAlgo(nbr_a, nbr_b))

print('*** Optimal algorithm ***')
print("PGCD of", nbr_a, "and", nbr_b, ":", pgcd_optimalAlgo(nbr_a, nbr_b))

print('*** "Recursive function" algorithm ***')
print("PGCD of", nbr_a, "and", nbr_b, ":", pgcd_recursiveAlgo(nbr_a, nbr_b))
