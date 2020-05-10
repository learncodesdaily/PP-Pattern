def starPattern(n):
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


n = int(input("Enter Pattern Size : "))
starPattern(n)