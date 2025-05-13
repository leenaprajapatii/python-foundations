"""
Loop logic practice - complex Itrations
This file contains some python loop blocks (for and while) use:
    -print world like "hello world" or "hello" or "radhe" or "krishna" ect. using tricky condition
    -practice nested loop, break, continue, variable mutations
    -learn how the control flows behave with custom increments and decrements
    
    * predict how many time each message will be printed
    Challenge yourself to trace the logic and guess outputs before running!
"""
# 1.
m=5
n=5
for i in  range(0,500,50):
    if n <= 0:
        break
    print("hello world")
    i = m*2
    n -= 1



# 2.
m = 100
he = ra = ka = 0
i = 0
while i < 200:
    for j in range(5):
        for k in range(1, j):
            i += 20
            he += 1
            print("hello")
        k = 2
        while k <= 9:
            i += 20
            ra += 1
            print("radhe")
            k = int(k * 1.5)
    l = 0
    while l < m:
        i += 10
        ka += 1
        m -= 20
        print("krishna")
        l += 1
print(f"hello counter = {he}")
print(f"radhe counter = {ra}")
print(f"krishna counter = {ka}")

print("-" * 30)

# 3.
i = 5
o = 0
op = 0
j = 500
while j > 20:
    k = 0
    while k < j or i > 0:
        print("hello")
        i -= 1
        o += 1
        k += 30
        j -= 50
        op += 1
        print(j, "vijju")
    l = 210
    while l > j and i > 0:
        print("hello")
        o += 1
        op += 1
        l -= 40
print("Total =", op)


# 4
m = 5
k = 0
i = 0
while i < 120:
    for j in range(i):
        print("hello")
        k += 1
        m *= j if j != 0 else 1
        i += m  # increases very fast
    i += 15
    print("radhe")
print("Final k =", k)

print("-" * 30)



    
    
# 5.
m = 5
n = 5
while True:
    if not (i<500 or n>0):
        break
    print("hello world")
    i = m*2
    n -= 1
    i += 50
    
# 6.
m = 5
n = 5
p = 0
i = 0
while i<500 and n>0:
    print("hello world")
    i = m*2
    n -= 1
    p += 50
    i += 50
print(f"Leena: {p} time.")



# 7
i=500
while i>100:
    print("hello world", end=" ")
    i = i - 7000 +3000
    if i < -100000:
        break

# 8
p = 12.0
while p < 89:
    print("hello world", end=" ")
    p = (p*11)/10
    if p > 100:
        break
    
# 9.
i = -12
j = 2
l = 0
while (i / 2 < 3) or (j < 20):
    print("vijay")
    i += 1
    j += 4
    l += 1
    if l > 100:  
        break