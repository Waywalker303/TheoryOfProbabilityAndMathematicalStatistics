# 3 Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

import numpy as np
import scipy.stats as stats

heightDaughter = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
mediumDaughter = sum(heightDaughter) / len(heightDaughter)

heightMotherr = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
mediumMotherr = sum(heightMotherr) / len(heightMotherr)

# print (mediumDaughter, mediumMotherr)


arr=np.array([mediumDaughter, mediumMotherr])

print(f'Среднее выборочное: {np.mean(arr): .2f},\n'
      f'Размер выборки n={len(arr)},\n'
      f'Среднее квадратическое отклонение по выборке: {np.std(arr, ddof=1): .2f}.')


def t_from_table(confidens, len_array):
    alpha=(1-confidens)
    return stats.t.ppf(1-alpha/2, len_array-1)
print(f'Табличное значение t-критерия для 0,95-го доверительного интервала: {t_from_table(0.95, len(arr)): .3f}')


def confidens_int(arr, confidens):
    return round(np.mean(arr)-t_from_table(confidens,len(arr))*np.std(arr, ddof=1)/len(arr)**0.5,3), \
           round(np.mean(arr)+t_from_table(confidens,len(arr))*np.std(arr, ddof=1)/len(arr)**0.5,3)

print(f'значение с доверительной вероятностью 0,95 для истинного значения Х: {confidens_int(arr, 0.95)}.')