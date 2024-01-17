coins = [5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
price = float(input("cena: ")) 
cost = float(input("kwota: ")) 
rest = price- cost
# rest = 10.0 - 3.4
print(rest)
i=0
while rest>=0 and i < len(coins):
    # print(f"reszta {rest}")
    if rest - coins[i] >= 0:
        print(f'{coins[i]}zł')
        rest = round(rest - coins[i],2)
    else:
        i+=1
    