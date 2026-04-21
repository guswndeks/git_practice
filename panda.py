import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# x = np.linspace(0, 2 * np.pi)
# ysin = np.sin(x)
# ycos = np.cos(x)

# fig, ax = plt.subplots(2, 1)

# ax[0].plot(x,ysin,'r--', label='sin')
# ax[0].set_title("Sin Function")
# ax[0].grid(True)
# ax[0].legend(loc='upper right')
# ax[0].set_xlabel("x")
# ax[0].set_ylabel("y")

# ax[1].plot(x,ycos,'b-', label='cos')
# ax[1].set_title("Cos Function")
# ax[1].grid(True)
# ax[1].legend(loc='lower left')
# ax[1].set_xlabel("x")
# ax[1].set_ylabel("y")

# plt.tight_layout()
# fig.savefig("Sin Cos Function")
# plt.show()

# ddf = pd.DataFrame(
#     data=[[10,20,30,40],[50,60,70,80]],
#     columns=['A','B','C','D']
# )
# new_ddf = ddf.drop('B',axis=1, inplace=False)
# print(ddf)
# print(new_ddf)
# print(ddf.loc[1])


# path = "https://github.com/dongupak/DataML/raw/main/csv/"
# weather_file = path + "weather.csv"

# weather = pd.read_csv(weather_file, encoding='CP949')
# weather['일시'] = pd.to_datetime(weather['일시'])

# weather['year'] = weather['일시'].dt.year

# monthly = [ None for x in range(12) ]
# monthly_wind = [ 0 for x in range(12) ]
# for i in range(12):
#     monthly[i] = weather[ weather['month'] == i + 1 ]
#     monthly_wind[i] = monthly[i]['평균기온'].mean()

# months = np.arange(1,13)
# plt.bar(months,monthly_wind,color='green')

# yearly_temp = weather.groupby('year')['평균기온'].mean()
# plt.bar(yearly_temp.index,yearly_temp,color='green')
# plt.xlabel('Year')
# plt.ylabel('Temperature')

# plt.show()

# df = pd.DataFrame({'score': [70, 80, 90, 85, 75]})
# print(df['score'].max(), df['score'].sum(), df['score'].mean())

dataA = {
    '학번': [1001,1002,1003,1004],
    '이름': ['김철수','이영희','박지수','최민준']
}
dataB = {
    '학번': [1001,1002,1003],
    '국어': [85,92,78],
    '영어': [90,88,82],
    '수학': [80,75,95]
}


dfA = pd.DataFrame(dataA)
dfB = pd.DataFrame(dataB)
merge_df = pd.merge(dfA,dfB,on='학번',how='left')

merge_df = merge_df.fillna(0)

merge_df['총점'] = merge_df['국어'] + merge_df['영어'] + merge_df['수학']

avg_total = merge_df['총점'].mean()
filtered_df = merge_df[merge_df['총점'] >= avg_total]

result = filtered_df.sort_values(by='이름', ascending=True)

print(result)
