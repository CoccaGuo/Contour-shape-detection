# iter_main.py by CoccaGuo at 2021/10/09 16:02

import os
from print_contour import result_plot

if __name__ == '__main__':
    
    data_package_path = './data/'
    if os.path.exists(data_package_path):
        files=os.listdir(data_package_path)
        for file in files:
            result_plot(os.path.join(data_package_path,file))