def check_right_triangle(a, b, c):
    if a >= b and a >= c:
        return a * a == b * b + c * c
    elif b >= a and b >= c:
        return b * b == a * a + c * c
    else:
        return c * c == a * a + b * b


a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if check_right_triangle(a, b, c):
    print("Right-angled triangle")
else:
    print("Not a right-angled triangle")
