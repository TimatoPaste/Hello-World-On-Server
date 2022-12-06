print("\n")
limit = int(input("Please enter the ceiling\n"))
primes = []
for a in range(2,limit+1):
    if a == 2:
        primes.append(a)
    else:
        prime = True;
        for b in range(0,len(primes)):
            if a%primes[b]==0:
                prime = False;
                break
        if prime:
            primes.append(a)
output = "The prime numbers up to "+str(limit)+" are: "
for a in range(0,len(primes)):
    output += str(primes[a])+" "
print(output)