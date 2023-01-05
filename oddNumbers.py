##n = 17
##aval = True
##for i in range(2, n):
##    if n % i == 0:
##        aval = False
##        print('be khatere ', i,'aval nist')

##if aval:
##    print ('it is prime')
##else:
##    print ("not prime")

def is_prime(n):
    aval = True
    for i in range(2, n):
        if n % i == 0:
            aval = False
    return aval

##print (is_prime(17))

prime_count = 0
for i in range (1, 1000):
##    print(i, is_prime(i))
    if is_prime(i):
        prime_count = prime_count + 1
        ##print (i)

print ("")
print ("total numbers: ", prime_count)
