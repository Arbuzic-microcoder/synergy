minimum_capital = int(input('Минимальный капитал для инвестиций равне:'))
mike = int(input('Капитал Майкла:'))
ivan = int(input('Капитал Ивана:'))

if mike >= minimum_capital and ivan >= minimum_capital:
    print (2)
elif mike >= minimum_capital or ivan >= minimum_capital or ivan + mike >= minimum_capital:
    print(1)
else:
    print(0)