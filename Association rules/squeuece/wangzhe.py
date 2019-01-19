import pandas as pd
import numpy as np
import sys
sys.path.append(r'../apriori')
# python 原有apriori.py 文件故需要少些最后一个字母
import aprior

csv = pd.read_csv("edg1.csv")

content_list = csv['op_pick']

with open('op_pick1.csv','a') as f:
    for content in content_list:
        f.write(content)
        f.write('\n')

dataset = pd.read_csv('op_pick1.csv')
data = np.array(dataset).reshape(-1, 5)


print(aprior.apriori(data,min_support = 0.09))

# 我取最后两个组合，对此王者官网确定，确定（154，花木兰），（199，公孙离），（162，鸟人），（134，达摩）
# 这次的数据较少，只体现了edg在2018冬季冠军杯最喜欢的两队组合是（花木兰，公孙离）和（达摩，鸟人）
