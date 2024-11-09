def count_case(n):
    countupper = 0
    countlower = 0
    for _ in n:
        if _.isupper() == True:
            countupper += 1
            
        elif _.islower() == True:
            countlower += 1
            
    print(f"No. of Upper case characters:{countupper}, No. of Lower case characters:{countlower}")

count_case("The quick Brow Fox")
