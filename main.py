a,b,c = 1,4,3
def ans(a,b,c):
    return ((-b**2 - (b**2 - 4*a*c)**0.5)/2,(-b**2 + (b**2 - 4*a*c)**0.5)/2)
print(ans(a,b,c))