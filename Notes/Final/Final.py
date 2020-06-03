import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("/Users/jamesgrove/PycharmProjects/P2_SP20/Notes/Final/mlbdata.csv", index_col=1)
df2 = pd.read_csv("/Users/jamesgrove/PycharmProjects/P2_SP20/Notes/Final/mlbdata.csv", index_col=0)

df1 = df1.sort_values('HR', ascending=False)
df2 = df2.sort_values('Elevation', ascending=False)

fig = plt.figure(figsize=(20, 5))

axis1 = fig.add_subplot(1, 2, 1)
axis2 = fig.add_subplot(1, 2, 2)

axis1.bar(df1.index, df1['HR'])
axis1.set_xticklabels(df1.index, rotation=60, horizontalalignment='right', fontsize='8')
axis1.set_title('Number of Home Runs by MLB Teams 2019', fontsize='16')
axis1.set_ylabel('# of Home Runs')

axis2.bar(df1.index, df2['Elevation'])
axis2.set_xticklabels(df2.index, rotation=60, horizontalalignment='right', fontsize='8')
axis2.set_title('Elevation by MLB Teams 2019', fontsize='16')
axis2.set_ylabel('Stadium Elevation (ft)')

plt.show()

df = pd.read_csv("/Users/jamesgrove/PycharmProjects/P2_SP20/Notes/Final/mlbdata.csv", index_col=1)

fig, axis = plt.subplots()
df = df.sort_values('Stadium HR', ascending=False)
axis.scatter(df.index, df['Stadium HR'])
axis.set_xticklabels(df.index, rotation=60, horizontalalignment='right', fontsize='8')
axis.set_title('Number of Home Runs in Different Ballparks', fontsize='16')
axis.set_ylabel('# of Home Runs')

plt.show()

df = pd.read_csv("/Users/jamesgrove/PycharmProjects/P2_SP20/Notes/Final/mlbdata.csv")

df.groupby('Elevation')['Stadium HR'].sum().plot.bar()
plt.title("Number of Home Runs Hit in Stadiums of Different Altitudes")
plt.ylabel("Number of Home Runs Hit in Stadium")
plt.show()
