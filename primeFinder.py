print("\n")
limit = 0
limit = int(input("Please enter the ceiling\n"))
primes = []
counter = 2
while counter <= limit:
    if counter == 2:
        primes.append(counter)
    else:
        prime = True;
        for b in primes:
            if counter%b==0:
                prime = False;
                break
        if prime:
            primes.append(counter)
    counter +=1
print("The prime numbers up to "+str(limit)+" are: ")
for a in primes:
    print(str(a),end = " ")