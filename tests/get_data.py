import pandas as pd


df = pd.read_csv('../TrainModel/out.csv')
df_y = df.truncate(after = 999)
df_ = df.drop(columns=['Day1_Hs', 'Day1_D','Day2_Hs', 'Day2_D','Day3_Hs', 'Day3_D'])
df_train = df_.truncate(after = 999)
# df_train
# df_train.head()
X_train = df_train.to_numpy()[:-200]
X_test = df_train.to_numpy()[-200:]
# print(len(df_train.to_numpy()))


