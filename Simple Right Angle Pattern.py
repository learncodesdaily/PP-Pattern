def alphabetPattern(n):
    for i in range(1,n+1):
        for j in range(65, 65 + i):
            a = chr(j)
            print(a, end=" ")
        print("\r")


n = int(input("Enter Pattern Size : "))
alphabetPattern(n)
