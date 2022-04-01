import statistics

max_age = 0
min_age = 130
max_country = ()
min_country = ()
with open("life-expectancy.csv") as main:
    for line in main:
        parts = line.split(",")
        entity = parts[0]
        code = parts[1]
        year = float(parts[2])
        l_exp = float(parts[3])
        if l_exp > max_age:
            max_age = year
            max_country = entity
        elif l_exp < min_age:
            min_age = year
            min_country = entity
        else:
            continue

mxle_age = 0
mnle_age = 130
mxle_country = ()
mnle_country = ()

with open("life-expectancy.csv") as main:
    yr_int = int(input("Enter the year of interest: "))
    av_list = []
    for line in main:
        parts = line.split(",")
        entity = parts[0]
        code = parts[1]
        year = float(parts[2])
        l_exp = float(parts[3])
        if yr_int == year:
            av_list.append(age)
            if l_exp > max_age:
                max_age = year
                max_country = entity
            elif l_exp < min_age:
                min_age = year
                min_country = entity
            else:
                continue

average_age = statistics.fmean(av_list)

print(f"Result:")
print(f"The max recorded age in the whole database is for {max_country} and it is {max_age}")
print(f"The min recorded age in the whole database is for {min_country} and it is {min_age}")
print()
print(f"For the year {yr_int}:")
print(f"The average life expectancy across all countries was {average_age:.2f}")
print(f"The max life expectancy was in {mxle_country} with {mxle_age}")
print(f"The min life expectancy was in {mnle_country} with {mnle_age}")