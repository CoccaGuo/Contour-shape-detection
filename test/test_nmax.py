# test_nmax.py by CoccaGuo at 2021/09/28 14:37
import heapq
import sys
sys.path.append('./')
from utils import nMin

m = [34,94,35,78,45,67,1, 90,23,90,1,0]
# 求一个list中最大的2个数，并排序
max_number = heapq.nlargest(3, m) 
# 最大的2个数对应的，如果用nsmallest则是求最小的数及其索引
max_index = map(m.index, heapq.nlargest(3, m)) 
print(max_number)
# max_index 直接输出来不是数，使用list()或者set()均可输出
print(list(max_index))

a, b = nMin(m, 3)
print(a, b)