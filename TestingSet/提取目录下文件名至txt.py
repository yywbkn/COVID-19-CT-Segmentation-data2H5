import os


file_path = r'F:\Program Files\pycharm\workspace03\COVID-19 CT Segmentation data2H5\TestingSet\H5'

list = []
list = os.listdir(file_path)

for i  in list:
    print(i)
    name, suffix = i.split('.')
    print('name = ', name)
    print('suffix =', suffix)
    with open("val.txt", "a") as f:
        f.write(str(name) + '\n')
