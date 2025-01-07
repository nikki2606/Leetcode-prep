def is_colorful(num):
    numstr = str(num)
    prod = set()
    for i in range(len(numstr)):
        temp = 1
        for j in range(i,len(numstr)):
            temp *= int(numstr[j])
            if temp in prod:
                return False
            prod.add(temp)
    return True 

input = 3245
print(is_colorful(input))