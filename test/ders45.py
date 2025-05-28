def isPowTwo(num) -> bool:
    n =0
    for i in range(num):
        if num == 2**n:
            return True
        n +=1
    return False

print(isPowTwo(0))

print("ılovepython")