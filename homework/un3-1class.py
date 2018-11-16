
# coding: utf-8

# In[1]:


name = input("請輸入姓名")
chinese_grade = input("請輸入國⽂成績")
english_grade = input("請輸入英⽂成績")
print("{0:8}{1:>5}{2:>5}" .format("姓名","國⽂","英⽂"))
print("{0:<10}{1:>6}{2:>6}" .format(name,chinese_grade,english_grade))


# In[4]:


8 / 7.0
8 + (8 + 7j)
"---"
type(8 / 7.0)
type(8 + (8 + 7j))
type("---")


# In[5]:


'I am loving it!'
'I\'m loving it!'
'I don\'t think you\'ll ever be just "anybody".'
"I don't think you'll ever be just \"anybody\"."


# In[6]:


str1 = "Hello!" + "How Are You?"
print(str1)


# In[7]:


str2 = "Hello!" * 3
print(str2)


# In[8]:


str3 = "Hello!\nHow Are You?"
print(str3)


# In[10]:


print("I'm" + " loving" + " it!")


# In[11]:


print ("I'm loving it" + "!" * 3)


# In[12]:


str = "ABCDEFGHIJK"
print(str[0])
print(str[-2])


# In[13]:


print(str[:7:2])


# In[14]:


print(str[:2:2])


# In[15]:


str1 = "Do \none \nthing \nat a time!"
print(str1.split())
print(str1.split( ' ', 2 ))


# In[16]:


str = "The first wealth is health! Health is important!"
print ("{},長度是{}" .format(str, len(str)))
print(str.upper())
print(str.lower())
print("health".capitalize())
str.islower()
str.count("health")
str.strip("h!")
str.replace("important", "重要")


# In[24]:


from datetime import date
sys_date = date.today()
print(sys_date)
print (type(sys_date))


# In[23]:


from datetime import date
start_of_2017 = date(2017, 1, 1)
end_of_2017 = date(2017, 12, 31)
start_of_2017
end_of_2017


# In[25]:


from datetime import date
start_of_2017 = date(2017, 1, 1)
start_of_2018 = start_of_2017.replace(year = 2018)
start_of_2018


# In[26]:


from datetime import date
start_of_2017 = date(2017, 1, 1)
end_of_2017 = start_of_2017.replace(month = 12, day = 31)
days_dff = end_of_2017 - start_of_2017
days_dff.days


# In[27]:


from datetime import time
sleep_time = time(23, 0, 0)
sleep_time
type(sleep_time)


# In[28]:


from datetime import time
sleep_time = time(23, 0, 0)
wake_up_time = sleep_time.replace(hour = 7)
wake_up_time


# In[29]:


from datetime import datetime
sys_datetime = datetime.now()
sys_datetime
type(sys_datetime)


# In[30]:


from datetime import datetime
start_of_2017 = datetime(2017, 1, 1, 0, 0, 0)
start_of_2017


# In[31]:


from datetime import datetime
start_of_2017 = datetime(2017, 1, 1, 0, 0, 1)
end_of_2017 = start_of_2017.replace(month = 12, day = 31, hour = 23, minute = 59, second = 59)
end_of_2017


# In[32]:


from datetime import datetime
start_of_2017 = datetime(2017, 1, 1, 0, 0, 1)
end_of_2017 = start_of_2017.replace(month = 12, day = 31, hour = 23, minute = 59, second = 59)
date_time_diff = end_of_2017 - start_of_2017
date_time_diff.days
date_time_diff.seconds


# In[34]:


print (48.195 * 0.62137)


# In[36]:


my_height = 160
print (my_height)


# In[38]:


my_weight = 60
print (my_weight)


# In[42]:


my_height = 160
my_weight = 60
bmi = my_weight / (my_height / 100)**2
print(bmi)


# In[1]:


starring_1 = "Jennifer Aniston"
starring_2 = "Courteney Cox"
starring_3 = "Lisa Kudrow"
starring_4 = "Matt LeBlanc"
starring_5 = "Matthew Perry"
starring_6 = "David Schwimmer" 


# In[2]:


starrings = ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
starrings


# In[3]:


genre = "sitcom"
no_of_episodes = 236
still_airing = False
friends = [genre, no_of_episodes, still_airing]
friends
type(friends)


# In[5]:


team_name = "Chicago Bulls"
wins = 72
losses = 10
win_percentage = wins / (wins + losses)
is_champion = True
chicago_bulls = [team_name, wins, losses, win_percentage, is_champion]
chicago_bulls


# In[18]:


fruitlist =["Apple","Orange","Lemon"]
print(len(fruitlist))
fruitlist[1] ="Kiwi"
fruitlist.append("Mongo")


# In[19]:


fruitlist.append("Mongo")


# In[25]:


fruitlist.insert(1, "banana")


# In[26]:


fruitlist.remove("Apple")


# In[29]:


fruitlist.pop(1)
fruitlist.sort()
fruitlist


# In[30]:


starrings = ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
starrings[0]
starrings[-1]
starrings[:3]
starrings[3:]


# In[31]:


genre = "sitcom"
no_of_episodes = 236
still_airing = False
friends = [genre, no_of_episodes, still_airing]
type(friends[0])
type(friends[1])
type(friends[2])


# In[33]:


team_name = "Chicago Bulls"
wins = 72
losses = 10
win_percentage = wins / (wins + losses)
is_champion = True
chicago_bulls_list = [team_name, wins, losses, win_percentage, is_champion]
chicago_bulls_tuple = (team_name, wins, losses, win_percentage, is_champion)
chicago_bulls


# In[34]:


starrings_list = ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
starrings_tuple = tuple(starrings_list)
starrings_tuple
type(starrings_tuple)


# In[35]:


starrings_tuple = ("Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer")
starrings_tuple
type(starrings_tuple)


# In[37]:


gender_list = ["female", "female", "female", "male", "male", "male"]
gender_set = set(gender_list)
gender_set
type(gender_set)

gender_set = {"female", "female", "female", "male", "male", "male"}
gender_set
type(gender_set)


# In[38]:


animal = {"bird" , "cat" , "dog" }
animal.add("fish")
print(animal)


# In[39]:


animal.remove("cat")
print(animal)


# In[40]:


animal.update({"bird", "monkey"})
print(animal)


# In[42]:


print("fish" in animal)
print("monkey" in animal)


# In[44]:


gender_set = {"female", "female", "female", "male", "male", "male"}
gender_set


# In[47]:


friends_dict = {
 "genre": "sitcom",
 "seasons": 10,
 "episodes": 236,
 "starrings": ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
}
type(friends_dict)


# In[49]:


dic = {"name": "Andy", "age":18, "city":"台北"}
dic.clear()
print(dic)


# In[50]:


dicA = {"name": "Andy", "age":18, "city":"⾼雄"}
dic = dicA.copy()
print(dic)


# In[51]:


dic.get("age")
dic.pop("city")
dic.update(dicA)
print(dic)


# In[52]:


print(dic.items())
print(dic.keys())
print(dic.values())


# In[54]:


chicago_bulls_list = [team_name, wins, losses, win_percentage, is_champion]
print(chicago_bulls_list)

