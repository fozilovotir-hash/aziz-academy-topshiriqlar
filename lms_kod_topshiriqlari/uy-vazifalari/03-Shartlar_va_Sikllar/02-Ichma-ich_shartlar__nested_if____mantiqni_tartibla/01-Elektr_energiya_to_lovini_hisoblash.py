kWh =  int(input())
if kWh  < 0:
    print("Notogri qiymat")
else:
    if kWh <= 100:
        tolov = kWh * 450 
    elif kWh <= 200:
        tolov = (100 * 450) + ((kWh - 100) * 600)
    else:
        tolov = (100 * 450) + (100 * 600) +((kWh - 200) * 900)
print(tolov)