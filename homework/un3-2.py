
# coding: utf-8

# In[4]:


import random
weathers = ["晴天", "下雨"]
weather = weathers[random.randint(0, 1)]
if weather == "晴天":
 print ("天氣是%s，去⼾外跑步" % weather)
else:
 print ("天氣是%s，去健⾝房" % weather)


# In[6]:


import random
weathers = ["晴天", "下雨", "暴風雨"]
weather = weathers[random.randint(0, 2)]
if weather == "晴天":
 print ("天氣是%s，去⼾外跑步" % weather)
elif weather == "下雨":
 print ("天氣是%s，去健⾝房" % weather)
else:
 print ("天氣是%s，睡回籠覺" % weather)


# In[12]:


starrings = ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
print (starrings[0])
print (starrings[1])
print (starrings[2])
print (starrings[3])
print (starrings[4])
print (starrings[5])


# In[23]:


starrings = ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
i = 0
while i < 6:
 print (starrings[i])
 i += 1


# In[24]:


for i in range(len(starrings)):
 print (starrings[i])


# In[25]:


starrings = ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
for (index, starring) in enumerate(starrings):
 print ("%i: %s" % (index, starring))


# In[26]:


characters = ["Rachel Green", "Monica Geller", "Phoebe Buffay", "Joey Tribbiani", "Chandler Bing", "Ross Geller"]
starrings = ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
for (character, star) in zip(characters, starrings):
 print (character + " 由 " + star + " 主演")


# In[27]:


starrings = ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
for starring in starrings:
 print (starring)


# In[28]:


#key：value
starrings = {
 "Rachel Green": "Jennifer Aniston",
 "Monica Geller": "Courteney Cox",
 "Phoebe Buffay": "Lisa Kudrow",
 "Joey Tribbiani": "Matt LeBlanc",
 "Chandler Bing": "Matthew Perry",
 "Ross Geller": "David Schwimmer"
}
for starring in starrings:
 print (starring)


# In[30]:


starrings = {
 "Rachel Green": "Jennifer Aniston",
 "Monica Geller": "Courteney Cox",
 "Phoebe Buffay": "Lisa Kudrow",
 "Joey Tribbiani": "Matt LeBlanc",
 "Chandler Bing": "Matthew Perry",
 "Ross Geller": "David Schwimmer"
}
for starring in starrings.keys():
 print (starring)
print("---")
for starring in starrings.values():
 print (starring)


# In[31]:


starrings = {
 "Rachel Green": "Jennifer Aniston",
 "Monica Geller": "Courteney Cox",
 "Phoebe Buffay": "Lisa Kudrow",
 "Joey Tribbiani": "Matt LeBlanc",
 "Chandler Bing": "Matthew Perry",
 "Ross Geller": "David Schwimmer"
}
for (key, value) in starrings.items():
 print ("%s 由 %s 演出" % (key, value))


# In[39]:


starrings = [
 ("Rachel Green", "Jennifer Aniston"),
 ("Monica Geller", "Courteney Cox"),
 ("Phoebe Buffay", "Lisa Kudrow"),
 ("Joey Tribbiani", "Matt LeBlanc"),
 ("Chandler Bing", "Matthew Perry"),
 ("Ross Geller", "David Schwimmer")
]
for (character, star) in starrings:
 print(character + "由" + star + "主演")


# In[41]:


import random
coin_flips = [] 
coin = ["Head", "Tail"]
while coin_flips.count("Head") < 3:
 coin_flips.append(coin[random.randint(0, 1)])
print (coin_flips) 
print (len(coin_flips))

