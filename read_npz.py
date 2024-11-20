import numpy as np

datas = np.load('./label_mind_original.npz')
print(datas.files)

data_dict = {key: datas[key] for key in datas.files}

m = datas['labels']
print(m)
# data_dict['labels'] = np.array([0, 1, 2, 3, 4, 5, 6])#换行间隔
# print(m)

# np.savetxt('./M.txt', data_dict['labels'], delimiter=" ")    #保存为txt
# np.savetxt('./M.csv', data_dict['labels'], delimiter=",")
#
# np.savez('./label_mind.npz', **data_dict)