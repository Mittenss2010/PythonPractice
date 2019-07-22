#导入相关库
import numpy as np
import os
import shutil
from tqdm import tqdm

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# detection中的类别属性
# newList = ('zhuanpan','yeqidaqian_close','yeqidaqian','taoguanqian','taoguan','bxingdiaoqian','gunzifangbuxin','xiaofangbuxin','diaoqia','diaoqia_xiaozi','tishengduanjie','zuanting',
#             'qiawa','anquanqiawa','duopianqiawa','zuangan','xuanzhuanbuwei_nawujian','youtong','anquanlian','anquanlian_no','fangpenqi','gouzi','shudongguan','shudongkou',
#             'zuangantou',         # 特有的一些项
#             'xiaozi_inhand','fangzuangan','qianzi','banshou','langtou','guaniqi','huangyouqiang','gangju','zuantou','zuantouhezi','tieqiao'
#             'ren','anquanmao_red','kouzhao','gongxie','bianxie','gongzhuang','bianzhuang','shoutao','shou',
#             'shouji','shuiping','chouyan','beizi','benzi','mabu',
#             'chelun')


'''
    字典：要修改的旧，新名称
'''
classnames_dict = {
            'roi_zhuan_pan':'zhuanpan',
            'zhuanpan_roi':'zhuanpan',
            'roi_zhuan_pan1':'zhuanpan',
            'zhuanpan':'zhuanpan',

            'yeqidaqian_close':'yeqidaqian_close',
            'ye_qi_da_qian':'yeqidaqian',
            'yeqidaqian1':'yeqidaqian',
            'yeqidqian':'yeqidaqian',
            'yeqidaqian':'yeqidaqian',
            'yeyagan':'yeyagan',

            'taoguanqian':'taoguanqian',
            'taoguan':'taoguan',
            'bxingdiaoqian':'bxingdiaoqian',
            'bxdq':'bxingdiaoqian',
            'bxdiaoqian':'bxingdiaoqian',
            'b_xing_diao_qian':'bxingdiaoqian',

            'gun_zi_fang_bu_xin':'gunzifangbuxin',
            'gunzifangbuxin':'gunzifangbuxin',

            'xiao_bu_xin':'xiaofangbuxin',
            'xiaofangbuxin':'xiaofangbuxin',

            'diaoqia':'diaoqia',
            'diao_qia':'diaoqia',
            'diaoqia-noxiaozi':'diaoqia',
            'diaoqia-xiaozi':'diaoqia_xiaozi',
            'tishengduanjie':'tishengduanjie',
            'zuanting':'zuanting',
            'qiawa':'qiawa',
            'anquanqiawa':'anquanqiawa',
            'duopianqiawa':'duopianqiawa',
            
            'zuangan':'zuangan',
            'none':'xuanzhuanbuwei_nawujian',
            'youtong':'youtong',
            'you_tong':'youtong',
            'anquanlian':'anquanlian',
            'anquanlian_no':'anquanlian_no',
            'fangpenqi':'fangpenqi',
            'fang_pen_qi':'fangpenqi',
            'fangkongqi':'fangpenqi',

            'gouzi':'gouzi',
            'shudongguan':'shudongguan',

            'shudongkou':'shudongkou',
            'shu_dong_kou':'shudongkou',
            'shoudongkou':'shudongkou',

            'zuangantou':'zuangantou',         # 特有的一些项
            'zhuanpan1':'zhuanpan',            
            'xiaozi-in-hand':'xiaozi_inhand',
            'fangzuangan':'fangzuangan',
            'ye_ya_mao_tou':'yeyamaotou',
            'yeyamaotou':'yeyamaotou',

            'tisi':'tisi',


            'roi_ti_sheng_duan_jie':'tishengduanjie_roi',
            'tishengduanjie_roi':'tishengduanjie_roi',
            'roi_hu_lian':'hulian_roi',
            'hulian_roi':'hulian_roi',

            'roi_hu_lan':'hulan_roi',
            'hulan_roi':'hulan_roi',

            'roi_zuan_gan':'zuangan_roi',
            'roi_zuan_ju':'zuangan_roi',
            'zuangan_roi':'zuangan_roi',

            'fengdongjiaoche':'fengdongjiaoche',
            'feng_dong_jiao_che':'fengdongjiaoche',

            'san_pian_shi_qia_wa':'sanpianshiqiawa',
            'sanpianshiqiawa':'sanpianshiqiawa',     

            'tianjiu':'tieqiao',
            'tieqiao':'tieqiao',

            'qianzi':'qianzi',
            'banshou':'banshou',
            'langtou':'langtou',
            'guaniqi':'guaniqi',
            'huangyouqiang':'huangyouqiang',
            'gangju':'gangju',
            'zuantou':'zuantou',
            'zuantouhezi':'zuantouhezi',
            'zuan_tou_he_zi':'zuantouhezi',

            'person':'ren',
            'ren':'ren',

            'anquanmao_no':'anquanmao_no',
            'anquanmao-red':'anquanmao_red',
            'anquanmao_red':'anquanmao_red',
            'anquanmao_white':'anquanmao_white',
            'anquanmao_yellow':'anquanmao_yellow',

            'kouzhao':'kouzhao',
            'gongxie':'gongxie',
            'bianxie':'bianxie',
            'gongzhuang':'gongzhuang',
            'bianzhuang':'bianzhuang',
            'shoutao':'shoutao',
            'shaoutao':'shoutao',
            'shou':'shou',
            'humujing':'humujing',
            'houmujing':'humujing',

            'shuitong':'shuitong',
            'tuoba':'tuoba',
            'shuiping':'shuiping',
            'chouyan':'chouyan',
            'beizi':'beizi',
            'benzi':'benzi',
            'mabu':'mabu',
            'shouji':'shouji',
            'yusan':'yusan',
            
            'none':'chelun',
            'shou-na':'shou',
            'shou-down':'shou',
            'shou-up':'shou',
            }



def rename_label(filename, xmlsPath, xmlsPath_new):
    """
        Parse xml file and return labels.
        解析xml，并根据字典中的项目来修订新的名称
    """

    anno_path = xmlsPath + filename
    tree = ET.parse(anno_path)
    root = tree.getroot()

    for obj in root.findall('object'):                      # 使用list not iter  
        cls_name = obj.find('name').text.strip().lower()    # 获取classname
        cls_name = classnames_dict[cls_name]                # 更新classname
        obj.find('name').text = cls_name

    outputPath = xmlsPath_new + filename
    tree.write(outputPath, "UTF-8")


if __name__ == "__main__":

    #xmlsPath = 'G:/cqsy_collection/2019-07-16-mix/'
    #xmlsPath = 'G:/cqsy_collection/数据标注管理/1670/'
    #xmlsPath = 'G:/【cqsy_collection】/数据标注管理/【已标注】接收的图片/合并/01/'
    xmlsPath = 'G:/2019-07-21/'
    xmlsPath = 'G:/VOCdevkit/'

    dirName = xmlsPath.split('/')[-2]
    originPath = xmlsPath[:-len(dirName)-2]
    xmlsPath_new = originPath + '/newXmls/'
    #print(xmlsPath_new)
    if not os.path.exists(xmlsPath_new):
       os.mkdir(xmlsPath_new)
       
    for filename in tqdm(os.listdir(xmlsPath)):
        if filename[-4:] == '.xml':
            # print(filename)
            rename_label(filename, xmlsPath, xmlsPath_new)
            # break