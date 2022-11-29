# both 2x2 and3x3 matrix:
m = int(input("enter the number of rows:"))
n = int(input("enter the number of coloum:"))
k = m * n
# the character equation for 2x2 matrix
if k == 4:
    a11 = int(input("enter a a11 element in A matrix:"))
    a12 = int(input("enter a a12 element in A matrix:"))
    a21 = int(input("enter a a21 element in A matrix:"))
    a22 = int(input("enter a a22 element in A matrix:"))
    s1 = a11 + a22
    s2 = a11 * a22 - a21 * a12
    s1 = -1 * s1
    print("the value of s1:", -1 * s1)
    print("the value of s2:", s2)
    print("the character equation is :x**2", s1, "x", s2, "=0")
    a = 1
    b = s1
    c = s2
    r1 = (b ** 2 - 4 * a * c)
    r1 = -b + r1 ** 0.5
    r1 = r1 / 2 * a
    r2 = (b ** 2 - 4 * a * c)
    r2 = -b - r2 ** 0.5
    r2 = r2 / 2 * a
    roots = [r1, r2]
    roots.sort()
    print("the eigen values are:", roots)

# the character equation for 3x3 matrix
elif k == 9:
    a11 = int(input("enter a a11 element in A matrix:"))
    a12 = int(input("enter a a12 element in A matrix:"))
    a13 = int(input("enter a a13 element in A matrix:"))
    a21 = int(input("enter a a21 element in A matrix:"))
    a22 = int(input("enter a a22 element in A matrix:"))
    a23 = int(input("enter a a23 element in A matrix:"))
    a31 = int(input("enter a a31 element in A matrix:"))
    a32 = int(input("enter a a32 element in A matrix:"))
    a33 = int(input("enter a a33 element in A matrix:"))
    s1 = a11 + a22 + a33
    s2 = a22 * a33 - a32 * a23 + a11 * a33 - a31 * a13 + a11 * a22 - a21 * a12
    s3 = a11 * (a22 * a33 - a32 * a23) - a12 * (a21 * a33 - a31 * a23) + a13 * (a21 * a32 - a31 * a22)
    s1 = -1 * s1
    s3 = -1 * s3
    print("the value of s1:", -1 * s1)
    print("the value of s2:", s2)
    print("the value of s3:", -1 * s3)
    print("the character equation is :x**3", s1, "x**2", s2, "x", s3, "=0")
    n1 = 1
    n2 = s1
    n3 = s2
    n4 = s3
    check = n1 + n2 + n3 + n4
    op = n1 + n3
    ep = n2 + n4
    c2 = -n2 / n1
    check2 = c2 * 1 / 3
    c3 = -n4 / n1
    check3 = c3 ** 0.34

    if n4 == 0:
        r3 = 0
        a = n1 + 0
        b = a * r3
        b = (n2 + b)
        c = b * r3
        c = (n3 + c)
        r1 = (b ** 2 - 4 * a * c)
        r1 = -b + r1 ** 0.5
        r1 = r1 / 2 * a
        r2 = (b ** 2 - 4 * a * c)
        r2 = -b - r2 ** 0.5
        r2 = r2 / 2 * a
        r1 = int(r1)
        r2 = int(r2)
        roots = [r1, r2, r3]
        roots.sort()

        print("the eigen values are:", roots)

    elif check == 0:
        r3 = 1
        a = n1 + 0
        b = a * r3
        b = (n2 + b)
        c = b * r3
        c = (n3 + c)
        r1 = (b ** 2 - 4 * a * c)
        r1 = -b + r1 ** 0.5
        r1 = r1 / 2 * a
        r2 = (b ** 2 - 4 * a * c)
        r2 = -b - r2 ** 0.5
        r2 = r2 / 2 * a
        r1 = int(r1)
        r2 = int(r2)
        roots = [r1, r2, r3]
        roots.sort()
        print("the eigen values are:", roots)
    elif op == ep:
        r3 = -1
        a = n1 + 0
        b = a * r3
        b = (n2 + b)
        c = b * r3
        c = (n3 + c)
        r1 = (b ** 2 - 4 * a * c)
        r1 = -b + r1 ** 0.5
        r1 = r1 / 2 * a
        r2 = (b ** 2 - 4 * a * c)
        r2 = -b - r2 ** 0.5
        r2 = r2 / 2 * a
        r1 = int(r1)
        r2 = int(r2)
        r3 = int(r3)
        roots = [r1, r2, r3]
        roots.sort()
        print("the eigen values are:", roots)
    elif check2==int:
        r3 = check2
        a = n1 + 0
        b = a * r3
        b = (n2 + b)
        c = b * r3
        c = (n3 + c)
        r1 = (b ** 2 - 4 * a * c)
        r1 = -b + r1 ** 0.5
        r1 = r1 / 2 * a
        r2 = (b ** 2 - 4 * a * c)
        r2 = -b - r2 ** 0.5
        r2 = r2 / 2 * a
        r1 = int(r1)
        r2 = int(r2)
        r3 = int(r3)
        roots = [r1, r2, r3]
        roots.sort()
        print("the eigen values are:", roots)
    elif check3==int:
        r3 = check3
        a = n1 + 0
        b = a * r3
        b = (n2 + b)
        c = b * r3
        c = (n3 + c)
        r1 = (b ** 2 - 4 * a * c)
        r1 = -b + r1 ** 0.5
        r1 = r1 / 2 * a
        r2 = (b ** 2 - 4 * a * c)
        r2 = -b - r2 ** 0.5
        r2 = r2 / 2 * a
        r1 = int(r1)
        r2 = int(r2)
        r3 = int(r3)
        roots = [r1, r2, r3]
        roots.sort()
        print("the eigen values are:", roots)
    else:
        for i in range(1, 100):
            r3 = i + 1
            a = n1 + 0
            b = a * r3
            b = n2 + b
            c = b * r3
            c = n3 + c
            d = c * r3
            d = n4 + d
            if d == 0:
                print(r3)
                r1 = (b ** 2 - 4 * a * c)
                r1 = -b + r1 ** 0.5
                r1 = r1 / 2 * a
                r2 = (b ** 2 - 4 * a * c)
                r2 = -b - r2 ** 0.5
                r2 = r2 / 2 * a
                r1 = int(r1)
                r2 = int(r2)
                r3 = int(r3)
                roots = [r1, r2, r3]
                roots.sort()
                print("the eigen values are:", roots)
                break
            else:
                print(end="")
else:
    print("2x2 and 3x3 matrix only exist ")
