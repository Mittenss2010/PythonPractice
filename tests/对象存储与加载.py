import pickle

print('原始对象**********')
print(temp_space)
temp_set = vars(temp_space)
print('字典数量：{}'.format(len(temp_set)))
print('字典数量：{}'.format(len(temp_space.__dict__)))

for index, item_dict in enumerate(temp_set):
    print('字典：{}, 元素数量：{}'.format(index, len(item_dict)))

print('对象存储**********')
with open('temp.plc', 'wb') as file:
    pickle.dump(temp_space, file)

print('对象加载**********')
with open('temp.plc', 'rb') as file:
    new_temp_space = pickle.load(file)

print('新对象**********')
print(new_temp_space)
temp_set = vars(new_temp_space)
print('字典数量：{}'.format(len(temp_set)))
print('字典数量：{}'.format(len(new_temp_space.__dict__)))

for index, item_dict in enumerate(temp_set):
    print('字典：{}, 元素数量：{}'.format(index, len(item_dict)))