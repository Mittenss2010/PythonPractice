## ListA
a = [0 for i in range(10)]
print(a)

## ListB，其中包含三条ListA，应该是同一个对象
## 在ListB中每次添加a，使用同一个对象加入

b = []
b.insert(0,a)
b.append(a)
b.append(a)
print(b)

# 修改B其中的一个ListA，所有B中的List发生联动
b[0].append(1)
print(b)
