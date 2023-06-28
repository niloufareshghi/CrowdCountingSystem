import pandas as pd 
import os

print("Hello World")

'''We are trying to get the ground truth for our data by reading data frames and matching data to it's corresponding GT'''

df_test = pd.read_csv("image_labels_test.txt", sep=',', header=None, names=['path','count','colC','colD','colE'], engine='python', dtype={'path': object})
df_test = df_test.drop(columns=['colC', 'colD', 'colE'])

directory = 'test'
test_list = []
for filename in os.scandir(directory):
    test_list.append(filename.path[-8:-4])
print(test_list)

df_test = df_test[df_test['path'].isin(test_list)]

print(df_test)

df_test.to_csv('gt_test.csv', header=False, index=False)


df_train = pd.read_csv("image_labels_train.txt", sep=',', header=None, names=['path','count','colC','colD','colE'], engine='python', dtype={'path': object})
df_train = df_train.drop(columns=['colC', 'colD', 'colE'])

directory = 'train'
train_list = []
for filename in os.scandir(directory):
    train_list.append(filename.path[-8:-4])
print(train_list)

df_train = df_train[df_train['path'].isin(train_list)]

print(df_train)

df_train.to_csv('gt_train.csv', header=False, index=False)

df_val = pd.read_csv("image_labels_val.txt", sep=',', header=None, names=['path','count','colC','colD','colE'], engine='python', dtype={'path': object})
df_val = df_val.drop(columns=['colC', 'colD', 'colE'])

directory = 'val'
val_list = []
for filename in os.scandir(directory):
    val_list.append(filename.path[-8:-4])
print(val_list)

df_val = df_val[df_val['path'].isin(val_list)]

print(df_val)

df_val.to_csv('gt_val.csv', header=False, index=False)