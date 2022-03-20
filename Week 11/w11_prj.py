with open("life-expectancy.csv") as main:
    for line in main:
        parts = line.split(",")

        entity = parts[0]
        code = parts[1]
        year = parts[2]
        l_exp = parts[3]
       
        max_exp = max(l_exp)
        min_exp = min(l_exp)

        print(f'the highest value for life expectancy {max_exp}')
        print(f'the lowest value for life expectancy {min_exp}')
