# def digits(num):
#     counter = 1
#     digits = 0
#     while counter <= num:
#         digits +=1
#         counter = counter * 10
#     return digits
n = 101
y = 1
res = 0
while y <= n:
    counter = 1
    dig = 0
    while counter <= y:
        dig += 1
        counter = counter * 10
    res = (res * (10 ** dig))
    res += y
    y += 1
print(res)


