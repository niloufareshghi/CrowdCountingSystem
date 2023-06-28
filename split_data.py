import shutil, os
import pandas as pd

df = pd.read_excel("outputs/p2p/val.xlsx", header=None, skiprows=1, names=['path', 'cnt', 'gt', 'error', 'bin'])
df1 = df[df['bin'] == 1]
print(df1)
paths1 = list(df1['path'])
files1 = []
for p in paths1:
    f = (4 - len(str(p))) * "0" + str(p) + ".jpg"
    real_path = os.path.join("val", f)
    files1.append(real_path)

folder_path = os.path.join("outputs", "p2p", "val", "errorful")
for f in files1:
    shutil.copy(f, folder_path)

df2 = df[df['bin'] == 0]
paths2 = list(df2['path'])
files2 = []
for p in paths2:
    f = (4 - len(str(p))) * "0" + str(p) + ".jpg"
    real_path = os.path.join("val", f)
    files2.append(real_path)

folder_path = os.path.join("outputs", "p2p", "val", "errorless")
for f in files2:
    shutil.copy(f, folder_path)

