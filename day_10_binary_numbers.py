def convertToBinary(n):
    x = bin(n).replace("0b","").split("0")
    print(len(max(x)))
