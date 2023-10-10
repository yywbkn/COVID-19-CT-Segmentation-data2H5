
import os
import numpy as np
import cv2
import h5py



#先把单个图片写成H5文件，同时获得np.array的图片的尺寸
def save_image_to_h5py(imgs_path,GT_path):
    dir_counter = 0

    for child_dir in os.listdir(imgs_path):
        dir_image = os.path.join(imgs_path, child_dir)
        # print('dir_image中图像的名称是:\n', dir_image)

        name, suffix = child_dir.split('.')
        # print('name = ',name)
        # print('suffix =',suffix)
        names = name + '.png'
        print('names = ', names)
        dir_label = os.path.join(GT_path , names )
        print('dir_label 中图像的名称是:\n', dir_label)

        img = cv2.imread(dir_image)
        img_0 = img[:, :, 0]
        print('img_0 shape:', img_0.shape)

        # 从GT文件里面读取图像获取label标签
        label_tmp = cv2.imread(dir_label)
        # print('label_tmp shape:', label_tmp.shape)
        label_tmp_0 = label_tmp[:,:,0]
        # print('label_tmp_0 shape:', label_tmp_0.shape)
        label_tmp_0_0 = np.int64(label_tmp_0 > 1)
        print('label_tmp_0_0 shape:', label_tmp_0_0.shape)

        result_file = h5py.File('../Pseudo-label/H5/{}.h5'.format(name), "w")
        result_file.create_dataset('image', data=img_0, compression='gzip')
        result_file.create_dataset('label', data=label_tmp_0_0, compression="gzip")
        print(f"***Finish create one database:{dir_image},***")
        result_file.close()
        dir_counter += 1
    print('dir_counter =',dir_counter)

if __name__ == '__main__':
    imgs_path = r'../Pseudo-label/Imgs'
    GT_path = r'../Pseudo-label/GT'
    save_image_to_h5py(imgs_path,GT_path)



