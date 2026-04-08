a, b, c = map(int, input().split())

z = {a, b, c}

if len(z) == 1:  
    print(10000 + (z.pop()) * 1000)
elif len(z) == 2: 
    if a == b or a == c:
        print(1000 + a * 100)
    else:
        print(1000 + b * 100)
else:  
    print(max(z) * 100)