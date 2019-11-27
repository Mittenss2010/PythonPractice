import cv2 
import xml.etree.cElementTree as ET
import os



classList = [
            'anquanmao_white',
            'anquanmao_red'
            ]


def clip_cigarette(filePath, img_name):
    img_path = filePath + img_name
    img = cv2.imread(img_path)
    anno_path = filePath[:-4] +  'xml/' + img_name[:-4]+'.xml'
    
    cv2.imshow("img", img)
    cv2.waitKey(30)
    print(img_path)
    print(anno_path)

    # tree = ET.parse(anno_path)
    # root = tree.getroot()

    # for obj in root.findall('object'):                      
    #     cls_name = obj.find('name').text.strip().lower()   
    #     xml_box = obj.find('bndbox')
    #     xmin = (int(xml_box.find('xmin').text) - 0)
    #     ymin = (int(xml_box.find('ymin').text) - 0)
    #     xmax = (int(xml_box.find('xmax').text) - 1)
    #     ymax = (int(xml_box.find('ymax').text) - 1)

    #     if cls_name in classList:
    #         coef = 0.75
    #         height_nocoef = int((ymax - ymin))
    #         height = int((ymax - ymin)*coef)
    #         # width = int((xmax - xmin)*coef)
    #         # cv2.rectangle(img,(xmin,ymin + height_nocoef), (xmax,ymax + height),(255,255,0), 2)
    #         cv2.imshow("img", img)
    #         # img_new = img[ ymin+height_nocoef:ymax+height, xmin:xmax]

    #         cv2.imwrite(img_name[-20:], img_new)
    #         # cv2.imshow("img", img)
    #         cv2.imshow("img_new", img_new)
    #                     cv2.imshow("img", img)

    #         cv2.waitKey(30)

if __name__ == "__main__":
    
    filePath = 'G:/data/40656-数据集/【接收】/20190813-no/test/img/'
    for img_name in os.listdir(filePath):
        clip_cigarette(filePath, img_name)