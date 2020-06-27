
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from scipy.stats import ttest_ind

pd.set_option('display.max_rows', 50)  # показывать больше строк
pd.set_option('display.max_columns', 50)  # показывать больше колонок

students = pd.read_csv('stud_math.csv')


# Первичный отсмотр данных
display(students.head(5))
students.info()


# анализируем числовые данные
def get_stat_number(column, n):
    median = students[column].median()
    IQR = students[column].quantile(0.75) - students[column].quantile(0.25)
    perc25 = students[column].quantile(0.25)
    perc75 = students[column].quantile(0.75)
    print('25-й перцентиль: {},'.format(perc25), 'медиана: {},'.format(median), '75-й перцентиль: {},'.format(perc75),
          "IQR: {}, ".format(IQR), "Границы выбросов: [{f}, {l}].".format(f=perc25 - 1.5*IQR, l=perc75 + 1.5*IQR))
    students[column].loc[students[column].between(perc25 - 1.5*IQR, perc75 + 1.5*IQR)].hist(bins=n, range=(students[column].min(), students[column].max()),
                                                                                            label='IQR')
    students[column].loc[(students[column] >= perc75 + 1.5*IQR) | (students[column] <= perc25 - 1.5*IQR)].hist(alpha=0.5, bins=n, range=(students[column].min(), students[column].max()),
                                                                                                               label='Выбросы')
    plt.legend()


# анализируем числовые данные
# анализируем score
display(students['score'].value_counts(dropna=False)
        ), students.loc[:, ['score']].info()


# уберем строке, где score отсутствует и изменим тип на integer
students = students.loc[students.score >= 0]
students['score'] = students.score.apply(lambda x: int(x))


# распределение score
get_stat_number('score',10)


# уберем лишний столбец studytime, granular
students.drop(['studytime, granular'], inplace = True, axis = 1)


# столбец age
get_stat_number('age',8)


# столбец absences
display(students['absences'].value_counts(dropna=False)), students.loc[:, ['absences']].info()


# заменим отсутствующие значения на 0
students['absences'] = students.absences.apply(lambda x: 0 if pd.isna(x) else int(x))
get_stat_number('absences',20)


# посмотрим на категориальные данные
for c in ('school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic','Medu', 'Fedu', 'traveltime', 'studytime', 'freetime', 'goout', 'health'):
    print(display(students[c].value_counts(dropna=False)), students.loc[:, [c]].info())


# Исправим ошибки в Fedu - 40 заменим на 4, NaN на 0
students['Fedu'] = students.apply(lambda x: str(
    "0.0") if x.Fedu == "nan" else str(x.Fedu), axis=1)
students['Fedu'] = students.apply(
    lambda x: "4.0" if x.Fedu == "40.0" else str(x.Fedu), axis=1)

# Исправим ошибки в Mjob NaN на other
students['Mjob'] = students.apply(
    lambda x: "other" if pd.isna(x.Mjob) else x.Mjob, axis=1)

# Исправим ошибки в Mjob NaN на other
students['Fjob'] = students.apply(
    lambda x: "other" if pd.isna(x.Fjob) else x.Fjob, axis=1)

# Исправим ошибки в reason NaN на other
students['reason'] = students.apply(
    lambda x: "other" if pd.isna(x.reason) else x.reason, axis=1)

# Исправим ошибки в reason NaN на other
students['guardian'] = students.apply(
    lambda x: "other" if pd.isna(x.guardian) else x.guardian, axis=1)

# Исправим ошибки в failures заменим NaN на 0
students['failures'] = students.failures.apply(
    lambda x: 0 if pd.isna(x) else int(x))

# Исправим ошибки в famrel: -1 заменим на 1, NaN на медиану
students['famrel'] = students.apply(
    lambda x: 4 if pd.isna(x.famrel) else int(x.famrel), axis=1)
students['famrel'] = students.apply(
    lambda x: 1 if x.famrel == -1 else int(x.famrel), axis=1)

# Исправим ошибки в Medu : заменим NaN на 0
students['Medu'] = students.apply(
    lambda x: '0.0' if x.Medu == 'nan' else str(x.Medu), axis=1)

# изменим тип traveltime  на строковый
students['traveltime'] = students.apply(lambda x: str(x))

# изменим тип studytime  на строковый
students['studytime'] = students.apply(lambda x: str(x))

# изменим тип famrel  на строковый
students['famrel'] = students.apply(lambda x: str(x))

# изменим тип freetime  на строковый
students['freetime'] = students.apply(lambda x: str(x))

# изменим тип goout  на строковый
students['goout'] = students.apply(lambda x: str(x))

# изменим тип health  на строковый
students['health'] = students.apply(lambda x: str(x))


def get_stat_dif(column):
    cols = students.loc[:, column].value_counts().index[:10]
    combinations_all = list(combinations(cols, 2))
    for comb in combinations_all:
        if ttest_ind(students.loc[students.loc[:, column] == comb[0], 'score'],
                     students.loc[students.loc[:, column] == comb[1], 'score']).pvalue \
                <= 0.05/len(combinations_all):  # Учли поправку Бонферони
            print('Найдены статистически значимые различия для колонки', column)
            break


for col in ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic','Medu', 'Fedu', 'traveltime', 'studytime', 'freetime', 'goout', 'health']:
    print(get_stat_dif(col))


def get_boxplot(column):
    fig, ax = plt.subplots(figsize=(14, 4))
    sns.boxplot(x=column, y='score',
                data=students.loc[students.loc[:, column].isin(
                    students.loc[:, column].value_counts().index[:10])],
                ax=ax)
    plt.xticks(rotation=45)
    ax.set_title('Boxplot for ' + column)
    plt.show()


for col in ['address', 'Mjob', 'higher', 'romantic', 'Medu']:
    get_boxplot(col)


students.corr()


students_for_model = students.loc[:, ['address', 'Mjob', 'higher', 'romantic', 'Medu', 'age', 'failures','score']]
students_for_model.head()
