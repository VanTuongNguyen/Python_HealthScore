import pandas as pd


df = pd.read_csv('../TrainModel/out.csv')
df_y = df.truncate()
df_ = df.drop(columns=['Day1_Hs', 'Day1_D','Day2_Hs', 'Day2_D','Day3_Hs', 'Day3_D'])
df_train = df_.truncate()
# df_train
# df_train.head()
X_train = df_train.to_numpy()[:-1100]
X_test = df_train.to_numpy()[-1100:]
# print(len(df_train.to_numpy()))


