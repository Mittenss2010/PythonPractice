import sys
sys.path.append('../')                       # 添加模块导入路径


## class Layout_code_element 测试
# from rule import Layout_code_element

# if __name__ == "__main__":
#     lce = Layout_code_element('1','10')
#     print(lce.dir)
#     print(lce.length)

## class LayoutCode 测试
from rule import Layout_code_element
from rule import Layout_code_matrix

if __name__ == "__main__":

    obj_classes = ['yeqidaqian','bihemen','zhuanpan']
    prohibit_type = 0           # 缺位禁止
    check_class = 'bihemen'

    # 构造矩阵
    # temp =  [[None,0,0],
    #         [0,None,0],
    #         [0,0,None]]
# 复杂方法**********************************************************************
    element_Matrix = []
    element_list = []
    element_list.append(None)
    element_list.append(Layout_code_element('0','2'))
    element_list.append(Layout_code_element('4','1'))
    element_Matrix.append(element_list)

    element_list = []
    element_list.append(Layout_code_element('2','3'))
    element_list.append(None)
    element_list.append(Layout_code_element('3','3'))
    element_Matrix.append(element_list)

    element_list = []
    element_list.append(Layout_code_element('8','3'))
    element_list.append(Layout_code_element('8','3'))
    element_list.append(None)
    element_Matrix.append(element_list)

    lce = Layout_code_matrix(element_Matrix, obj_classes ,prohibit_type, check_class)

# 简便方法**********************************************************************

# 构造矩阵
def construct_element_Matrix(self):
    ele_list_1 = [-1, Layout_code_element('0','2'), Layout_code_element('4','1')]
    ele_list_2 = [Layout_code_element('2','3'), -1, Layout_code_element('3','3')]
    ele_list_3 = [Layout_code_element('8','3'), Layout_code_element('8','3'), -1]
    ele_Matrix = [ele_list_1, ele_list_2, ele_list_3]
    return ele_Matrix

# 原始方法**********************************************************************

def get_raw_Matrix(self):
    return [[-1 , 0.2, 4.1],
            [2.3, -1 , 3.3],
            [8.3, 8.3,  -1]]