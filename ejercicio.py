def function(a, b, n):
    for i in range(n):
        print(a/b)
        a=b
        b=(a/b)

print(function(3,1,4))