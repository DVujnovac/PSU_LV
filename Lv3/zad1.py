import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')

df = pd.DataFrame(mtcars)

sorted_df = df.sort_values(by='mpg')
print('5 automobila sa najvecom potrosnjom: ')
print(sorted_df.head(5))

print('3 automobila s 8 cilindara i najmanjom potrosnjom')
print(sorted_df[sorted_df.cyl==8].tail(3))

print('Srednja potrošnja automobila sa 6 cilindra: ')
print(mtcars[mtcars.cyl==6].mean)

print('Srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs')
print(mtcars[(mtcars.cyl==4)&(mtcars.wt*1000>2000)&(mtcars.wt*1000<2200)])

manual = mtcars[mtcars.am==1]
automatic = mtcars[mtcars.am==0]
print('Broj manualnih: ', len(manual))
print('Broj automatika: ', len(automatic))

automaticHp = mtcars[(mtcars.am==0)&(mtcars.hp>100)]
print('Broj automatika sa snagom preko 100hp: ', len(automaticHp))

mtcars['wtKg']= (mtcars.wt*1000)*0.453592
print(mtcars[['car','wtKg']])


print(mtcars.iloc[[1,29], :])
