def digits(num):
    counter = 1
    digits = 0
    while counter <= num:
        digits +=1
        counter = counter * 10
    return digits

# print(digits(11),"function")

x = 11100
y = 1
res = 0
while y <= x:
    dig = digits(y)
    res = (res * (10 ** dig))
    res += y
    y += 1
print(res)

# x = 1000
# counter = 1
# digits = 0
# while counter <= x:
#     digits += 1
#     counter = counter * 10

# print(digits, counter)
