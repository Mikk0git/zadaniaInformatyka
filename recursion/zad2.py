def oddNumRec(limit,num=1, sum=0):
    if num > limit:
        return sum
    
    if num % 2 != 0:
        sum = sum + num
        

    print(f"Liczba: {num}\n Suma: {sum}")


    return oddNumRec(limit,num + 1 , sum )
    


def oddNumIter(num):
    sum = 0
    while num < 100:
        if num % 2 != 0:
            sum = sum + num
        num +=1 
        print(f"Liczba: {num}\n Suma: {sum}")
        
    
# oddNumIter(1)
print(f"Suma ostateczna: {oddNumRec(100)}")
