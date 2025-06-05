import os
import pandas as pd

# USER INPUT
workspace = input("define workspace: ")
filename = input("define filename (without .csv): ")

# CHANGE WORKSPACE
os.chdir(workspace)

# READ FILE
df = pd.read_csv(filename + ".csv")

# WRITE FILE
df.to_excel(filename + ".xlsx", index=None, header=True)
