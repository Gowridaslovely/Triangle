def classify_triangle (a,b,c):
    if a <=0 or b <=0 or c <=0:
        return "Not a Triangle"
    if a+b <=c or a+c<=b or b+c<=a:
        return "Not a Triangle"
    sides = sorted([a,b,c])

    a,b,c = sides

    triangle_type =""

    if a==b==c:
        triangle_type = "Equilateral Triangle"
    elif a==b or b==c:
        triangle_type = "Isosceles Triangle"
    else:
        triangle_type = "Scalane Triangle"
    
    if a**2 + b**2 == c**2:
        triangle_type ="Right Angled Triangle"
    
    
    return triangle_type

if __name__ =="__main__":
    examples = [(6,7,8) , (5,5,5) , (4,4,5) , (3,5,7)]
    for sides in examples:
        print (sides, "->", classify_triangle(*sides))