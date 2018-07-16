n = int(input('Ban muon nhap vao bao nhieu so: '))
l1=[]
odd = []
even = []

for i in range(n):
    x = int(input('Please enter the number: '))
    l1.append(x)
    if x%2 == 0:
        even.append(x)
    else:
        odd.append(x)

print('Danh sach so le:', odd)
print('Danh sach so chan:', even)
    
