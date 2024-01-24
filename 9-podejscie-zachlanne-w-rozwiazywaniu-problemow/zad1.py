def main():
    values = [128,64,32,16,8,4,2,1]
    num = int(input("Liczba mniejsza niż 256: "))
    if num >=256:
        return
    
    i=0
    while num >0 and values[i] :
        if num-values[i] >= 0:
            num = num-values[i]
            print(f"NUM: {num}")
            print(f"value: {values[i]}")
        else:
            i+=1


main()