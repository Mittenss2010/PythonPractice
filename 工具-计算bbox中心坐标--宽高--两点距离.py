
import math

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class BboxUtils():

    def __init__(self):
        pass 

    @staticmethod
    def get_bbox_center(bbox):
        '''
            输入: bbox 信息
            返回: bbox 中心坐标
        '''
        xmin, ymin, xmax, ymax = [int(x) for x in bbox]
        xcenter = (xmin + xmax)/2.
        ycenter = (ymin + ymax)/2.
             
        return Point(xcenter,ycenter)

    @staticmethod
    def get_bbox_width_height(bbox):
        '''
            输入: bbox 信息
            返回: bbox 中心坐标
        '''
        xmin, ymin, xmax, ymax = [int(x) for x in bbox]

        return [xmax-xmin, ymax-ymin]   

    @staticmethod
    def get_2D_distence(point_a, point_b):
        return math.sqrt(math.pow((point_a.x - point_b.x),2) + math.pow((point_a.y-point_b.y),2))
