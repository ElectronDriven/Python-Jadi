
def is_prime(n):
    aval = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            aval = False
            break ## har vaq mirsam b break az halqe birun miad.
    return aval

prime_count = 0
last_prime = 0

for i in range (1, 1000):
    if is_prime(i):
        last_prime = i
        prime_count = prime_count + 1

print ("")
print ("total numbers: ", prime_count, ", and last number is: ", last_prime)
