import pandas as pd

'''df1 = pd.read_csv('outputs/can/test.txt', sep=' ',  header=None, names=['path','count'], engine='python', dtype={'path': object})
df1['sort'] = df1['path'].astype(int)
df1.sort_values('sort',inplace=True)
df1 = df1.drop('sort', axis=1)
df1.to_csv('outputs/can/test.csv', header=False, index=False)

df2 = pd.read_csv('outputs/can/train.txt', sep=' ',  header=None, names=['path','count'], engine='python', dtype={'path': object})
df2['sort'] = df2['path'].astype(int)
df2.sort_values('sort',inplace=True)
df2 = df2.drop('sort', axis=1)
df2.to_csv('outputs/can/train.csv', header=False, index=False)

df3 = pd.read_csv('outputs/can/val.txt', sep=' ',  header=None, names=['path','count'], engine='python', dtype={'path': object})
df3['sort'] = df3['path'].astype(int)
df3.sort_values('sort',inplace=True)
df3 = df3.drop('sort', axis=1)
df3.to_csv('outputs/can/val.csv', header=False, index=False)'''

df4 = pd.read_csv('outputs/p2p/test.txt', sep=',',  header=None, names=['path','count'], engine='python', dtype={'path': object})
df4['sort'] = df4['path'].astype(int)
df4.sort_values('sort',inplace=True)
df4 = df4.drop('sort', axis=1)
df4.to_csv('outputs/p2p/test.csv', header=False, index=False)

df5 = pd.read_csv('outputs/p2p/train.txt', sep=',',  header=None, names=['path','count'], engine='python', dtype={'path': object})
df5['sort'] = df5['path'].astype(int)
df5.sort_values('sort',inplace=True)
df5 = df5.drop('sort', axis=1)
df5.to_csv('outputs/p2p/train.csv', header=False, index=False)

df6 = pd.read_csv('outputs/p2p/val.txt', sep=',',  header=None, names=['path','count'], engine='python', dtype={'path': object})
df6['sort'] = df6['path'].astype(int)
df6.sort_values('sort',inplace=True)
df = df6.drop('sort', axis=1)
df6.to_csv('outputs/p2p/val.csv', header=False, index=False)


df7 = pd.read_csv('outputs/msfanet/test.txt', sep=' ',  header=None, names=['path','count'], engine='python', dtype={'path': object})
df7.to_csv('outputs/msfanet/test.csv', header=False, index=False)

df8 = pd.read_csv('outputs/msfanet/train.txt', sep=' ',  header=None, names=['path','count'], engine='python', dtype={'path': object})
df8.to_csv('outputs/msfanet/train.csv', header=False, index=False)

df9 = pd.read_csv('outputs/msfanet/val.txt', sep=' ',  header=None, names=['path','count'], engine='python', dtype={'path': object})
df9.to_csv('outputs/msfanet/val.csv', header=False, index=False)
