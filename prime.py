n=int(input("enter a number"))
next_prime = n + 1
prime = True
while True:
        for i in range(2, next_prime//2):
            if next_prime%i ==0:
                prime = False
                break
        if prime:
            print(next_prime)
            break
        else:
            next_prime = next_prime + 1
            #if next_prime % 2 == 0:
            #    next_prime = next_prime + 1
            prime = True
