# 时间输出测试

import time 

temp = 0
t1 = time.time()
for i in range(10000000):
    temp += i

print(temp)
print('time: ' + '{:.3}'.format(time.time() - t1) + 's')