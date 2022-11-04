

def take_rational_part(user_number):    
    for k in range(0, len(user_number)):
        if user_number[k] != '-' and user_number[k] != '+' and user_number[k] != '/' and user_number[k] != '*':            
            rational_part.append(user_number[k])
        else:
            break
    rational_part = float(''.join(rational_part))    
    return rational_part

def take_imaginary_part(user_number):    
    imaginary_part = []    
    for i in range(0, len(user_number)):
        if user_number[i] == 'i':
            while user_number[i] != '-' and user_number[i] != '+' and user_number[i] != '/' and user_number[i] != '*':
                imaginary_part.insert(0,user_number[i - 1])
                i-= 1
    imaginary_part.pop(0)
    imaginary_part = float(''.join(imaginary_part))
    return imaginary_part

def take_symbol(user_number):
    symbol = []
    for l in range(0, len(user_number)):
        if user_number[l] == '-' and l !=0 or user_number[l] == '+' and l != 0:
            symbol.append(user_number[l])
    symbol = ''.join(symbol)
    return symbol

def addition(r1, s1, i1, r2, s2, i2):
    result = []
    result.append(r1+r2)
    if s1 == '+' and s2 == '+':
        result.append(i1+i2)
    elif s1 == '+' and s2 == '-':
        result.append(i1-i2)
    elif s1 == '-' and s2 == '+':
        result.append(i2-i1)
    else:
        result.append(-(i1+i2))
    return result

def deduction(r1, s1, i1, r2, s2, i2):
    result = []
    result.append(r1-r2)
    if s1 == '+' and s2 == '+':
        result.append(i1-i2)
    elif s1 == '+' and s2 == '-':
        result.append(i1+i2)
    elif s1 == '-' and s2 == '+':
        result.append(-i2-i1)
    else:
        result.append(i2-i1)
    return result

def multiply(r1, s1, i1, r2, s2, i2):
    result = []
    result.append(r1*r2)
    if s1 == "+" or s2 == "+" or s1 == "-" or s2 == "-":
        result.append(-i1*i2)
    else:
        result.append(i1*i2)
    if s1 == "+":
        result.append(r2*i1)
    else:
        result.append(-r2*i1)
    if s2 == "+":
        result.append(r1*i2)
    else:
        result.append(-r1*i2)
    result[0] = result[0] + result[1]
    result[1] = result[2] + result[3]
    result.pop(3)
    result.pop(2)
    return result    
    
def division(r1, s1, i1, r2, s2, i2):
    numerator = []
    denominator = []
    result = []
    numerator.append(r1*r2)
    if s1 == "+" or s2 == "+" or s1 == "-" or s2 == "-":
        numerator.append(i1*i2)
    else:
        numerator.append(-i1*i2)
    if s1 == "-":
        numerator.append(-r2*i1)
    else:
        numerator.append(r2*i1)
    if s2 == "+":
        numerator.append(-r1*i2)
    else:
        numerator.append(r1*i2)
    numerator[0] = numerator[0] + numerator[1]
    numerator[1] = numerator[2] + numerator[3]
    numerator.pop(3)
    numerator.pop(2)
    denominator.append(r2**2+i2**2)
    result.append(round(numerator[0]/denominator[0], 3))
    result.append(round(numerator[1]/denominator[0], 3))
    print(result)
    return result

def record_in_file(result):
    pr=[]
    with open('results.json', 'a') as data:
        print('0',result[1])
        if result[1] != 0:
            for i in range(0, 2):
                if result[i] > 0 and i == 1:
                    print('+ ', end='')
                    data.write('+ ')
                    pr.append('+')
                elif result[i] < 0 and i == 1:
                    result[i] = -result[i]
                    result[i] = str(result[i])
                    print('- ', end='')
                    data.write('- ')
                    pr.append('-')
                else:
                    result[i] = str(result[i])
                    print(f'{result[i]}', end='')
                    data.write(result[i])
                    pr.append(result[i])
                if i != 1:
                    print(' ', end='')
                    data.write(' ')
            print(f'{result[1]}i')
            data.write(f'{result[1]}i\n')
            pr.append(f'{result[1]}i')
        else:
            result[0] = str(result[0])
            print(f'99 = {result[0]}\n')
            data.write(f'{result[0]}\n')
            pr.append(result[0])
    print(pr)
    data.close()
    return pr