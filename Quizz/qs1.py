sales = [105, 95, 130, 105, 160, 140, 115, 160, 115, 160]

# Calculate the average of the sales
average = sum(sales) / len(sales)
print(f"Average daily sales : {average}") 

# Determone the day with the highest sales and lowets sales
def highest_sales(sales):
    n = len(sales)
    day = 1
    tertinggi = sales[0]
    for i in range(1, n):
        if sales[i] > tertinggi:
            tertinggi = sales[i]
    return tertinggi
def lowest_sales(sales):
    n = len(sales)
    day = 1
    terkecil = sales[0]
    for i in range(1, n):
        if sales[i] < terkecil:
            terkecil = sales[i]
    return terkecil
print(f"highest values : {highest_sales(sales)} day {sales.index(highest_sales(sales))}")
print(f"lowets values : {lowest_sales(sales)} day {sales.index(lowest_sales(sales))}")

# Sort the sales data from lowets to highest
sales.sort()
print(f"sort data lowets to hignets : {sales}")

# Create a function that takes a specific value and returns how many times that values appears in the list
def count_kejadian(value, sales):
    count = 0
    for i in sales:
        if i == value:
            count += 1
    return count
print(count_kejadian(160, sales))
print(count_kejadian(105, sales))
print(count_kejadian(200, sales))

# Modify the list so that it only contains unique values(no duplicates)
def unique_values(sales):
    unique = []
    for i in sales:
        if i not in unique: 
            unique.append(i)
    return unique
print(unique_values(sales))
