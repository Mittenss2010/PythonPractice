import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()             # 参数解析器                                 
    parser.add_argument('--ch', type=int, default=1, help='select channel of camera')   # 增加参数描述
    args = parser.parse_args()                     # 构造参数管理对象
    print(args.ch)                                 # 获取python 参数