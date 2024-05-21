def combinations(n):
    combinations1 = 0
    for a in range(0,n):
        for b in range(0,n):
            c = n -(a+b)
            if(c<= 0):
                combinations1 =combinations1 + 1
    return combinations1

def main():
    print(combinations(5))
main()