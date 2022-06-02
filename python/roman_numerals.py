def to_roman(num):
    result = ''
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    while num > 0:
        if num >= 1000:
            result = result + 'M'
            num = num - 1000
        elif num >= 500:
            result = result + 'D'
            num = num - 500
        elif num >= 100:
            result = result + 'C'
            num = num - 100
        elif num >= 50:
            result = result + 'L'
            num = num - 50
        elif num >= 10:
            result = result + 'X'
            num = num -10
        elif num >= 5:
            result = result + 'V'
            num = num - 5
        elif num >= 1:
            result = result + "I"
            num = num - 1
    return(result)

print(to_roman(2022))

# def to_roman(num):
#     result = ''
