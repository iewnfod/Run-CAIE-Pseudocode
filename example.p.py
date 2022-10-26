
def READ(f):
    with open(f, 'r') as f:
        return f.read()
    
# 1
a = 0
a = 1
print(a)

# 2
if a == 1:
	print(a+1)
elif a == 2:
	print(a+2)
else:
	print(a + 3)
	

# 3
if a == "1":
	print("Equal to 1")
else:
	print("Not equal to 1")
	

# 3
a = int(input())
print(a)

# 4
def add10(a):
	print(a + 10)
	return a + 10


print(add10(a))

# 5
b = ''
print(a, b)

# 6
for i in range(1, 10+1):
	print(i)


# 7
temp_file = open("Desktop/test.txt", 'w+')
temp_file.write(str(a))
temp_file.close()

# 8
while True:
	a = a + 1
	print(a)
	if a == 100: 
		break

# 9
while a != 1000:
	a = a + 1
	print(a)

