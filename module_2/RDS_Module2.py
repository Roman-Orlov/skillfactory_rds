import pandas as pd
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
    print('25-й перцентиль: {},'.format(perc25), '75-й перцентиль: {},'.format(perc75),
          "IQR: {}, ".format(IQR), "Границы выбросов: [{f}, {l}].".format(f=perc25 - 1.5*IQR, l=perc75 + 1.5*IQR))
    students[column].loc[students[column].between(perc25 - 1.5*IQR, perc75 + 1.5*IQR)].hist(bins=n, range=(students[column].min(), students[column].max()),
                                                                                            label='IQR')
    students[column].loc[(students[column] >= perc75 + 1.5*IQR) | (students[column] <= perc25 - 1.5*IQR)].hist(alpha=0.5, bins=16, range=(students[column].min(), students[column].max()),
                                                                                                               label='Выбросы')
    plt.legend()

# функция удаления выбросов
def del_outlier(column):
    median = students[column].median()
    IQR = students[column].quantile(0.75) - students[column].quantile(0.25)
    perc25 = students[column].quantile(0.25)
    perc75 = students[column].quantile(0.75)
    return students.loc[students[column].between(perc25 - 1.5*IQR, perc75 + 1.5*IQR)]

# столбец age
get_stat_number('age',8)

# уберем выбросы
students = del_outlier('age')

# столбец studytime, granular
get_stat_number('studytime, granular',4)

# уберем выбросы
students = del_outlier('studytime, granular')

# столбец score
get_stat_number('score',10)

# уберем выбросы
students = del_outlier('score')

# функция перевода текстовоый формат
def transform_number_to_text(x):
    return str(x)


for c in ('Medu', 'Fedu', 'traveltime', 'studytime', 'freetime', 'goout', 'health'):
    students[c]=students[c].apply(transform_number_to_text)

# посмотрим на категориальные данные
for c in ('school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic','Medu', 'Fedu', 'traveltime', 'studytime', 'freetime', 'goout', 'health'):
    print(display(students[c].value_counts(dropna=False)), students.loc[:, [c]].info())

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

fig, ax = plt.subplots(figsize=(14, 4))
sns.boxplot(x='address', y='score',
            data=students.loc[students.loc[:, 'address'].isin(
                students.loc[:, 'address'].value_counts().index[:10])],
            ax=ax)
plt.xticks(rotation=45)
ax.set_title('Boxplot for address')
plt.show()


def get_boxplot(column):
    fig, ax = plt.subplots(figsize=(14, 4))
    sns.boxplot(x=column, y='score',
                data=students.loc[students.loc[:, column].isin(
                    students.loc[:, column].value_counts().index[:10])],
                ax=ax)
    plt.xticks(rotation=45)
    ax.set_title('Boxplot for ' + column)
    plt.show()


for col in ['Medu', 'Fedu', 'studytime', 'goout', 'sex', 'address', 'Fjob', 'schoolsup']:
    get_boxplot(col)


students.corr()


sns.pairplot(students, kind = 'reg')

