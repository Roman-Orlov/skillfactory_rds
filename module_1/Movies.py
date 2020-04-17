#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from collections import Counter
#print(os.listdir("../input"))


# In[7]:


data = pd.read_csv('data.csv')
data.head(5)


# In[8]:


len(data)


# # Предобработка датасета

# In[9]:


answer_ls = [] # создадим список с ответами. сюда будем добавлять ответы по мере прохождения теста
# сюда можем вписать создание новых колонок в датасете


# # 1. У какого фильма из списка самый большой бюджет?
# Варианты ответов:
# 1. The Dark Knight Rises (tt1345836)
# 2. Spider-Man 3 (tt0413300)
# 3. Avengers: Age of Ultron (tt2395427)
# 4. The Warrior's Way	(tt1032751)
# 5. Pirates of the Caribbean: On Stranger Tides (tt1298650)

# In[10]:


data[data.budget==data.budget.max()]


# In[11]:


# тут вводим ваш ответ и добавлем в его список ответов (сейчас для примера стоит "1")
answer_ls.append(4)


# # 2. Какой из фильмов самый длительный (в минутах)
# 1. The Lord of the Rings: The Return of the King	(tt0167260)
# 2. Gods and Generals	(tt0279111)
# 3. King Kong	(tt0360717)
# 4. Pearl Harbor	(tt0213149)
# 5. Alexander	(tt0346491)

# In[7]:


data[data.runtime==data.runtime.max()]


# In[8]:


answer_ls.append(2)


# # 3. Какой из фильмов самый короткий (в минутах)
# Варианты ответов:
# 
# 1. Home on the Range	tt0299172
# 2. The Jungle Book 2	tt0283426
# 3. Winnie the Pooh	tt1449283
# 4. Corpse Bride	tt0121164
# 5. Hoodwinked!	tt0443536

# In[9]:


data[data.runtime==data.runtime.min()]


# In[10]:


answer_ls.append(3)


# # 4. Средняя длительность фильма?
# 
# Варианты ответов:
# 1. 115
# 2. 110
# 3. 105
# 4. 120
# 5. 100
# 

# In[11]:


data.runtime.mean()


# In[12]:


answer_ls.append(2)


# # 5. Средняя длительность фильма по медиане?
# Варианты ответов:
# 1. 106
# 2. 112
# 3. 101
# 4. 120
# 5. 115
# 
# 
# 

# In[13]:


data.runtime.median()


# In[14]:


answer_ls.append(1)


# # 6. Какой самый прибыльный фильм?
# Варианты ответов:
# 1. The Avengers	tt0848228
# 2. Minions	tt2293640
# 3. Star Wars: The Force Awakens	tt2488496
# 4. Furious 7	tt2820852
# 5. Avatar	tt0499549

# In[15]:


data['profit'] = data['revenue'] - data['budget']
data[data.profit==data.profit.max()]


# In[16]:


answer_ls.append(5)


# # 7. Какой фильм самый убыточный?
# Варианты ответов:
# 1. Supernova tt0134983
# 2. The Warrior's Way tt1032751
# 3. Flushed Away	tt0424095
# 4. The Adventures of Pluto Nash	tt0180052
# 5. The Lone Ranger	tt1210819

# In[17]:


data[data.profit==data.profit.min()]


# In[18]:


answer_ls.append(2)


# # 8. Сколько всего фильмов в прибыли?
# Варианты ответов:
# 1. 1478
# 2. 1520
# 3. 1241
# 4. 1135
# 5. 1398
# 

# In[19]:


data[data.profit>0].count()


# In[20]:


answer_ls.append(1)


# # 9. Самый прибыльный фильм в 2008 году?
# Варианты ответов:
# 1. Madagascar: Escape 2 Africa	tt0479952
# 2. Iron Man	tt0371746
# 3. Kung Fu Panda	tt0441773
# 4. The Dark Knight	tt0468569
# 5. Mamma Mia!	tt0795421

# In[21]:


year_08 = data[data.release_year==2008]
year_08[year_08.profit == year_08.profit.max()]


# In[22]:


answer_ls.append(4)


# # 10. Самый убыточный фильм за период с 2012 по 2014 (включительно)?
# Варианты ответов:
# 1. Winter's Tale	tt1837709
# 2. Stolen	tt1656186
# 3. Broken City	tt1235522
# 4. Upside Down	tt1374992
# 5. The Lone Ranger	tt1210819
# 

# In[23]:


year_02_14 = data[(data.release_year<=2014) & (data.release_year>=2012)]
year_02_14[year_02_14.profit == year_02_14.profit.min()]


# In[24]:


answer_ls.append(5)


# # 11. Какого жанра фильмов больше всего?
# Варианты ответов:
# 1. Action
# 2. Adventure
# 3. Drama
# 4. Comedy
# 5. Thriller

# In[25]:


Set = data.genres.unique()
set_genres = []
for i in Set:
    k = i.split('|')
    for l in k:
        if l not in set_genres:
            set_genres.append(l)
max_genres=pd.DataFrame([], columns = ['Qnt'], index = set_genres)

for a in set_genres:
    max_genres.at[a, 'Qnt'] = data[data.genres.str.contains(a, na=False)].imdb_id.count()    
max_genres[max_genres.Qnt == max_genres.Qnt.max()]    


# In[26]:


answer_ls.append(3)


# # 12. Какого жанра среди прибыльных фильмов больше всего?
# Варианты ответов:
# 1. Drama
# 2. Comedy
# 3. Action
# 4. Thriller
# 5. Adventure

# In[27]:


for a in set_genres:
    max_genres.at[a, 'Qnt'] = data[(data.genres.str.contains(a, na=False)) & (data.profit > 0)].imdb_id.count()    
max_genres[max_genres.Qnt == max_genres.Qnt.max()] 


# In[28]:


answer_ls.append(1)


# # 13. Кто из режиссеров снял больше всего фильмов?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Ridley Scott 
# 3. Steven Soderbergh
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[29]:


set_of_director =[]
for d in data.director.unique():
    for i in d.split('|'):
        if i not in set_of_director:
            set_of_director.append(i)
            
by_director = pd.DataFrame([], columns = ['Qnt'], index = set_of_director)

for a in set_of_director:
    by_director.at[a, 'Qnt'] = data[data.director.str.contains(a, na=False)].imdb_id.count()    
by_director[by_director.Qnt == by_director.Qnt.max()]  


# In[30]:


answer_ls.append(3)


# # 14. Кто из режиссеров снял больше всего Прибыльных фильмов?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Clint Eastwood
# 3. Steven Spielberg
# 4. Ridley Scott
# 5. Christopher Nolan

# In[31]:


for a in set_of_director:
    by_director.at[a, 'Qnt'] = data[(data.director.str.contains(a, na=False)) & (data.profit > 0)].imdb_id.count()    
by_director[by_director.Qnt == by_director.Qnt.max()]


# In[32]:


answer_ls.append(4)


# # 15. Кто из режиссеров принес больше всего прибыли?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Christopher Nolan
# 3. David Yates
# 4. James Cameron
# 5. Peter Jackson
# 

# In[33]:


for a in set_of_director:
    by_director.at[a, 'Sum'] = data[data.director.str.contains(a, na=False)].profit.sum()    
by_director[by_director.Sum == by_director.Sum.max()]


# In[34]:


answer_ls.append(5)


# # 16. Какой актер принес больше всего прибыли?
# Варианты ответов:
# 1. Emma Watson
# 2. Johnny Depp
# 3. Michelle Rodriguez
# 4. Orlando Bloom
# 5. Rupert Grint

# In[35]:


set_of_actors =[]
for d in data.cast.unique():
    for i in d.split('|'):
        if i not in set_of_actors:
            set_of_actors.append(i)
            
by_actors = pd.DataFrame([], columns = ['Sum_profit'], index = set_of_actors)

for a in set_of_actors:
    by_actors.at[a, 'Sum_profit'] = data[data.cast.str.contains(a, na=False)].profit.sum()    
by_actors[by_actors.Sum_profit == by_actors.Sum_profit.max()]  


# In[36]:


answer_ls.append(1)


# # 17. Какой актер принес меньше всего прибыли в 2012 году?
# Варианты ответов:
# 1. Nicolas Cage
# 2. Danny Huston
# 3. Kirsten Dunst
# 4. Jim Sturgess
# 5. Sami Gayle

# In[37]:


for a in set_of_actors:
    by_actors.at[a, 'Sum_profit'] = data[(data.cast.str.contains(a, na=False)) & (data.release_year == 2012)].profit.sum()    
by_actors[by_actors.Sum_profit == by_actors.Sum_profit.min()] 


# In[38]:


answer_ls.append(3)


# # 18. Какой актер снялся в большем количестве высокобюджетных фильмов? (в фильмах где бюджет выше среднего по данной выборке)
# Варианты ответов:
# 1. Tom Cruise
# 2. Mark Wahlberg 
# 3. Matt Damon
# 4. Angelina Jolie
# 5. Adam Sandler

# In[39]:


for a in set_of_actors:
    by_actors.at[a, 'Count'] = data[(data.cast.str.contains(a, na=False)) & (data.budget > data.budget.mean())].imdb_id.count()     
by_actors[by_actors.Count == by_actors.Count.max()]


# In[40]:


answer_ls.append(3)


# # 19. В фильмах какого жанра больше всего снимался Nicolas Cage?  
# Варианты ответа:
# 1. Drama
# 2. Action
# 3. Thriller
# 4. Adventure
# 5. Crime

# In[41]:


movie_Nic = data[data.cast.str.contains('Nicolas Cage', na=False)]
max_genres_Nic=pd.DataFrame([], columns = ['Qnt'], index = set_genres)
for a in set_genres:
    max_genres_Nic.at[a, 'Qnt'] = movie_Nic[movie_Nic.genres.str.contains(a, na=False)].imdb_id.count()    
max_genres_Nic[max_genres_Nic.Qnt == max_genres_Nic.Qnt.max()] 


# In[42]:


answer_ls.append(2)
max_genres_Nic.sort_values('Qnt', ascending=False)


# # 20. Какая студия сняла больше всего фильмов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[43]:


set_of_companies =[]
for d in data.production_companies.unique():
    for i in d.split('|'):
        if i not in set_of_companies:
            set_of_companies.append(i)
            
by_company = pd.DataFrame([], columns = ['Count'], index = set_of_companies)

for a in set_of_companies:
    by_company.at[a, 'Count'] = data[data.production_companies.str.contains(a, na=False)].imdb_id.count()    
by_company[by_company.Count == by_company.Count.max()] 


# In[44]:


answer_ls.append(1)
by_company.sort_values('Count', ascending=False)


# # 21. Какая студия сняла больше всего фильмов в 2015 году?
# Варианты ответа:
# 1. Universal Pictures
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[45]:


for a in set_of_companies:
    by_company.at[a, 'Count'] = data[(data.production_companies.str.contains(a, na=False)) & (data.release_year == 2015)].imdb_id.count()    
by_company[by_company.Count == by_company.Count.max()] 


# In[46]:


answer_ls.append(4)
by_company.sort_values('Count', ascending=False)


# # 22. Какая студия заработала больше всего денег в жанре комедий за все время?
# Варианты ответа:
# 1. Warner Bros
# 2. Universal Pictures (Universal)
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Walt Disney

# In[47]:


company_comedy = data[data.genres.str.contains('Comedy', na=False)]
prof_company_comedy = pd.DataFrame([], columns = ['Prof'], index = set_genres)
for a in set_of_companies:
    prof_company_comedy.at[a, 'Prof'] = company_comedy[company_comedy.production_companies.str.contains(a, na=False)].profit.sum()    
prof_company_comedy[prof_company_comedy.Prof == prof_company_comedy.Prof.max()] 


# In[48]:


answer_ls.append(2)
prof_company_comedy.sort_values('Prof', ascending=False)


# # 23. Какая студия заработала больше всего денег в 2012 году?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Lucasfilm

# In[123]:


prof_company = pd.DataFrame([], columns = ['Prof'])
for a in set_of_companies:
    prof_company.at[a, 'Prof'] = data[(data.production_companies.str.contains(a, na=False)) & (data.release_year == 2012)].profit.sum()    
prof_company[prof_company.Prof == prof_company.Prof.max()]


# In[122]:


answer_ls.append(3)


# # 24. Самый убыточный фильм от Paramount Pictures
# Варианты ответа:
# 
# 1. K-19: The Widowmaker tt0267626
# 2. Next tt0435705
# 3. Twisted tt0315297
# 4. The Love Guru tt0811138
# 5. The Fighter tt0964517

# In[51]:


company_par = data[data.production_companies.str.contains('Paramount Pictures', na=False)]
company_par[company_par.profit == company_par.profit.min()]


# In[52]:


answer_ls.append(1)


# # 25. Какой Самый прибыльный год (заработали больше всего)?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2002
# 5. 2015

# In[54]:


data.groupby(['release_year']).profit.sum().sort_values(ascending=False).head(1)


# In[55]:


answer_ls.append(5)


# # 26. Какой Самый прибыльный год для студии Warner Bros?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2010
# 5. 2015

# In[56]:


company_WB = data[data.production_companies.str.contains('Warner Bros', na=False)]
company_WB.groupby(['release_year']).profit.sum().sort_values(ascending=False).head(1)


# In[57]:


answer_ls.append(1)


# # 27. В каком месяце за все годы суммарно вышло больше всего фильмов?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[58]:


def month(x):
    m = x.split('/')
    return m[0]

data['month'] = data.release_date.apply(month)
data.groupby(['month']).imdb_id.count().sort_values(ascending=False).head(1)


# In[59]:


answer_ls.append(4)


# # 28. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)
# Варианты ответа:
# 1. 345
# 2. 450
# 3. 478
# 4. 523
# 5. 381

# In[60]:


def month(x):
    m = x.split('/')
    return int(m[0])

data['month'] = data.release_date.apply(month)
summer = data[(data.month > 5) & (data.month < 9)]
summer.imdb_id.count()


# In[61]:


answer_ls.append(2)


# # 29. Какой режисер выпускает (суммарно по годам) больше всего фильмов зимой?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Christopher Nolan
# 3. Clint Eastwood
# 4. Ridley Scott
# 5. Peter Jackson

# In[62]:


wint_director = pd.DataFrame([], columns = ['Qnt'], index = set_of_director)
for a in set_of_director:
    wint_director.at[a, 'Qnt'] = data[(data.director.str.contains(a, na=False)) & ((data.month == 12) | (data.month == 1) | (data.month == 2))].imdb_id.count()    
wint_director[wint_director.Qnt == wint_director.Qnt.max()]


# In[104]:


answer_ls.append(5)


# # 30. Какой месяц чаще всего по годам самый прибыльный?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[125]:


pivot = data.pivot_table(values='profit', index='release_year', columns='month', aggfunc='sum', fill_value=None, margins=False, dropna=True)
pivot.idxmax(axis = 1).value_counts()


# In[121]:


answer_ls.append(2)


# # 31. Названия фильмов какой студии в среднем самые длинные по количеству символов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[144]:


len_name_company = pd.DataFrame([], columns = ['Len'])
data['len_name'] = data.original_title.apply(lambda x: len(x))
for a in set_of_companies:
    len_name_company.at[a, 'Len'] = data[data.production_companies.str.contains(a, na=False)].len_name.mean()  
len_name_company[len_name_company.Len == len_name_company.Len.max()]


# In[148]:


answer_ls.append(5)


# # 32. Названия фильмов какой студии в среднем самые длинные по количеству слов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[153]:


qnt_words_company = pd.DataFrame([], columns = ['QntW'])
data['qt_words'] = data.original_title.apply(lambda x: len(x.split(' ')))
for a in set_of_companies:
    qnt_words_company.at[a, 'QntW'] = data[data.production_companies.str.contains(a, na=False)].qt_words.mean()  
qnt_words_company[qnt_words_company.QntW == qnt_words_company.QntW.max()]


# In[154]:


answer_ls.append(5)


# # 33. Сколько разных слов используется в названиях фильмов?(без учета регистра)
# Варианты ответа:
# 1. 6540
# 2. 1002
# 3. 2461
# 4. 28304
# 5. 3432

# In[17]:


words = []
for n in data.original_title:
    w = n.lower().replace('  ',' ').split() 
    for i in w:
        if i not in words:
            words.append(i)
len(words)


# In[14]:


answer_ls.append(3)


# # 34. Какие фильмы входят в 1 процент лучших по рейтингу?
# Варианты ответа:
# 1. Inside Out, Gone Girl, 12 Years a Slave
# 2. BloodRayne, The Adventures of Rocky & Bullwinkle
# 3. The Lord of the Rings: The Return of the King
# 4. 300, Lucky Number Slevin

# In[21]:


test = {
1:[['Inside Out', 'Gone Girl', '12 Years a Slave']],
2:[['BloodRayne', 'The Adventures of Rocky & Bullwinkle']],
3:[['The Lord of the Rings: The Return of the King','Upside Down']],
4:[['300', 'Lucky Number Slevin']],
5:[['Inside Out','The Lord of the Rings: The Return of the King','300', 'Upside Down']]
}


d = data[['vote_average', 'original_title']].sort_values(by=['vote_average'], ascending=False).reset_index()
d_1p = d.iloc[:len(data) // 100]

df = pd.DataFrame.from_dict(test, orient='index', columns=['movies'])
df['result'] = [ all([ any(d_1p.original_title == test_m) for test_m in test_ms]) for test_ms in df.movies]
df


# In[13]:


answer_ls.append(3)


# # 35. Какие актеры чаще всего снимаются в одном фильме вместе
# Варианты ответа:
# 1. Johnny Depp & Helena Bonham Carter
# 2. Hugh Jackman & Ian McKellen
# 3. Vin Diesel & Paul Walker
# 4. Adam Sandler & Kevin James
# 5. Daniel Radcliffe & Rupert Grint

# In[ ]:


answer_ls.append(1)


# # 36. У какого из режиссеров выше вероятность выпустить фильм в прибыли? (5 баллов)101
# Варианты ответа:
# 1. Quentin Tarantino
# 2. Steven Soderbergh
# 3. Robert Rodriguez
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[ ]:





# In[ ]:


answer_ls.append(1)


# # Submission

# In[6]:


len(answer_ls)


# In[5]:


pd.DataFrame({'Id':range(1,len(answer_ls)+1), 'Answer':answer_ls}, columns=['Id', 'Answer'])


# In[ ]:




