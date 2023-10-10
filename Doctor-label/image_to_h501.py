
import os
import numpy as np
import cv2
import h5py



#SSL4MIS里面对ACDC数据处理成H5文件的代码
# for slice_ind in range(image.shape[0]):
#     f = h5py.File('/home/xdluo/data/ACDC/data/{}_slice_{}.h5'.format(item, slice_ind), 'w')
#     f.create_dataset('image', data=image[slice_ind], compression="gzip")
#     f.create_dataset('label', data=mask[slice_ind], compression="gzip")
#     f.close()
#     slice_num += 1
# x = label_tmp.reshape(label_tmp.shape[0], -1)
# np.savetxt("{}.csv".format(name), x, delimiter=",")

#先把单个图片写成H5文件，同时获得np.array的图片的尺寸
def save_image_to_h5py(imgs_path,GT_path):
    img_list = []
    label_list = []
    dir_counter = 0

    for child_dir in os.listdir(imgs_path):
        dir_image = os.path.join(imgs_path, child_dir)
        print('dir_image中图像的名称是:\n', dir_image)

        name, suffix = child_dir.split('.')
        print('name = ',name)
        print('suffix =',suffix)
        names = name + '.png'
        print('names = ', names)
        dir_label = os.path.join(GT_path , names )
        print('dir_label 中图像的名称是:\n', dir_label)

        # img = cv2.imread(dir_image)
        # print('img type:', type(img))
        # print('img shape:', img.shape)
        # # img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#单通道，分辨率会下降
        # # 从GT文件里面读取图像获取label标签
        # img_0 = img[:, :, 0]
        # print('img_0 shape:', img_0.shape)
        # img_1 = img[:, :, 1]
        # print('img_1 shape:', img_1.shape)
        # img_2 = img[:, :, 2]
        # print('img_2 shape:', img_2.shape)
        # img_2_1 = img_2 - img_1
        # img_1_0 = img_1 - img_0
        # print('Is img_2_1 all zeros?: ', not (np.any(img_2_1)))
        # print('Is img_1_0 all zeros?: ', not (np.any(img_1_0)))




        label_tmp = cv2.imread(dir_label)
        print('label_tmp shape:', label_tmp.shape)
        label_tmp_0 = label_tmp[:,:,0]
        # print('label_tmp_0 shape:', label_tmp_0.shape)
        # label_tmp_1 = label_tmp[:, :, 1]
        # # print('label_tmp_1 shape:', label_tmp_1.shape)
        # label_tmp_2 = label_tmp[:, :, 2]
        # # print('label_tmp_2 shape:', label_tmp_2.shape)
        # label_tmp_2_1 = label_tmp_2 - label_tmp_1
        # label_tmp_1_0 = label_tmp_1 - label_tmp_0
        # print('Is label_tmp_2_1 all zeros?: ', not (np.any(label_tmp_2_1)))
        # print('Is label_tmp_1_0 all zeros?: ', not (np.any(label_tmp_1_0)))

        label_tmp_0_0 = np.int64(label_tmp_0 > 1)
        np.savetxt('label_tmp_0.txt', label_tmp_0)
        np.savetxt('label_tmp_0_0.txt',label_tmp_0_0)


    #     result_file = h5py.File('Doctor-label/H5/COVID_2.h5', "w")
    #     result_file.create_dataset(f"train/{dir_image}/data", data=img, compression='gzip')
    #     result_file.create_dataset(f"train/{dir_image}/label", data=label_tmp)
    #     print(f"***Finish create one database:{dir_image},***")
    #     result_file.close()
    # # 返回的img_list转成了 np.array的格式
    # dir_counter += 1


if __name__ == '__main__':
    imgs_path = r'../Doctor-label/Imgs'
    GT_path = r'../Doctor-label/GT'
    save_image_to_h5py(imgs_path,GT_path)



