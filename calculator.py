def addition(a, b):
    sum = a + b
    return sum
    
def subtraction(a, b):
    sub = a - b 
    return sub 

def multiplication(a, b):
    mult = a * b
    return mult 

def divison(a, b):
    div = a / b
    return div 

def print_calc(a, b):
    sum_for_print = addition(a, b)
    sub_for_print = subtraction(a, b)
    mult_for_print = multiplication(a, b)
    div_for_print = divison(a, b)
    print(f"addition of {a} and {b} is {sum_for_print}")
    print(f"subtraction of {a} and {b} is {sub_for_print}")
    print(f"multiplication of {a} and {b} is {mult_for_print}")
    print(f"divison of {a} and {b} is {div_for_print}")

print_calc(2, 3)
