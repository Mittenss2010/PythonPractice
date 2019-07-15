dictA = {'AAA':1,'BBB':1,'CCC':1,
         'ddd':5,'eee':7,'fff':8
         }

# minKey = min(dictA, key=dictA.get)              # 

# minKeyList = []

# for key in dictA:
#     if dictA[key] == dictA[minKey]:
#         minKeyList.append(key)
        
# print(minKeyList)

# print(dictA)
# print(minKey)


listA = ['ddd','eee','fff']

for item in listA:
    if item in dictA:
        
        print(item)