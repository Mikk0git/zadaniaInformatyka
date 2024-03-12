def oddNumRec(num, sum):
    if num > 100:
        return 
    
    if num % 2 != 0:
        sum = sum + num

    print(f"Liczba: {num}\n Suma: {sum}")


    return oddNumRec(num + 1 , sum )
    


def oddNumIter(num):
    sum = 0
    while num < 100:
        if num % 2 != 0:
            sum = sum + num
        num +=1 
        print(f"Liczba: {num}\n Suma: {sum}")
        
    
# oddNumIter(1)
oddNumRec(1,0)
