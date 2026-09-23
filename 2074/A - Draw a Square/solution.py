n = int(input())
 
def square():
    l,r,d,u = map(int, input().split())
    return l == d == r == u
 
for i in range (n):
    print("yes" if square() else "no")