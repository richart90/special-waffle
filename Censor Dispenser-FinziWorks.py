#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Project Goals
#You’ve recently gotten a job working in the IT department at one of Silicon Valley’s hottest new startups, AirWeb. 
#The company is developing a state-of-the-art artificial intelligence engine designed to help provide a new 
#perspective on the world’s problems. Interestingly, very few people know the details of AirWeb ‘s work 
#and the company is very secretive about its technology, even to its own investors.
#You report directly to the Head of Product, a person named Mr. Cloudy, and 
#he has a very important task for you. You see, every month, the head researchers 
#down in the lab send an email to the board of investors to tell them about the status of the project. 
#Cloudy wants you to intercept these emails and censor any “proprietary information” included in them.


# In[1]:


# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


# In[4]:


print(email_one)


# In[5]:


print(email_two)


# In[6]:


print(email_three)


# In[7]:


print(email_four)


# # Write a function that can censor a specific word or phrase from a body of text, and then return the text.
# #Mr. Cloudy has asked you to use the function to censor all instances of the phrase #learning algorithms# 
# #from the first email, #email_one#. Mr. Cloudy doesn’t care how you censor it, he just wants it done.

# In[64]:


new_email_one = email_one.split()
#print(new_email_one[1])

print(new_email_one)

    


# In[5]:


new_email_one = ['Good', 'Morning,', 'Board', 'of', 'Investors,', 'Progress', 'is', 'going', 'great!', 'We', 'have', 'made', 'great', 'strides', 'in', 'the', 'last', 'month', 'improving', 'the', 'learning', 'algorithms', 'that', 'the', 'system', 'has', 'been', 'using', 'to', 'acquire', 'information.', 'Now,', 'the', 'system', 'is', 'learning', 'faster', 'than', 'ever', 'and', 'we', 'are', 'hard', 'pressed', 'to', 'continue', 'to', 'find', 'new', 'information', 'to', 'feed', 'it', 'and', 'sustain', 'its', 'growth.', 'Soon,', "we'll", 'expand', 'the', 'scope', 'of', 'the', 'learning', 'algorithms', 'and', 'connect', 'the', 'system', 'with', 'the', 'internet.', 'This', 'will', 'allow', 'it', 'to', 'find', 'and', 'determine', 'the', 'information', 'it', 'needs', 'to', 'continue', 'growing.', 'Every', 'month', 'we', 'come', 'closer', 'to', 'achieving', 'our', 'goal', 'of', 'making', 'the', 'world', 'a', 'better', 'place.', 'Famine,', 'plague,', 'war,', 'and', 'poverty', 'are', 'all', 'conquerable', 'with', 'the', 'power', 'of', 'our', 'system!', 'Till', 'next', 'month,', 'Francine,', 'Head', 'Scientist']

def new_email_one_censor(new_email_one):
    
    for x, y in enumerate(new_email_one[:-1]):
        if new_email_one[x+1] == "algorithms" and new_email_one[x] == "learning":
            new_email_one[x] = "xxxxx" 
            new_email_one[x+1] = "xxxxxx"
        
        
new_email_one_censor(new_email_one)
#print(new_email_one)
text_new_email_one_censored = " ".join(new_email_one)
print(text_new_email_one_censored)


# # Write a function that can censor not just a specific word or phrase from a body of text, but a whole list of words and phrases, and then return the text.
# 
# Mr. Cloudy has asked that you censor all words and phrases from the following list in email_two.
# 
# proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

# In[17]:


email_two = open("email_two.txt", "r").read()
new_email_two = email_two.split()
#print(new_email_two)

def new_email_two_censor(new_email_two):
    
    for x, y,  in enumerate(new_email_two[:-2]):
        if new_email_two[x+1] == "algorithms" and new_email_two[x] == "learning":
            new_email_two[x] = "xxxxx" 
            new_email_two[x+1] = "xxxxxx"
        elif new_email_two[x+1] == "matrix" and new_email_two[x] == "personality":
            new_email_two[x] = "xxxxx" 
            new_email_two[x+1] = "xxxxxx"
        elif new_email_two[x+2] == "self" and new_email_two[x+1] == "of" and new_email_two[x] == "sense" :
            new_email_two[x] = "xxxxx" 
            new_email_two[x+1] = "xxxxxx"
            new_email_two[x+2] = "xxxxxx"
        elif new_email_two[x] == "she" or new_email_two[x] == "She" :
            new_email_two[x] = "xxxxx"
        elif new_email_two[x] == "self-preservation":
            new_email_two[x] = "xxxxx"
        elif new_email_two[x] == "her" or new_email_two[x] == "Her":
            new_email_two[x] = "xxxxx"
        elif new_email_two[x] == "herself" or new_email_two[x] == "Herself" :
            new_email_two[x] = "xxxxx"
            
new_email_two_censor(new_email_two)
#print(new_email_two)
text_new_email_two_censored = " ".join(new_email_two)
print(text_new_email_two_censored)


# # The most recent email update has concerned Mr. Cloudy, but not for the reasons you might think. He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the negative language and remove unnecessary instances of ‘negative words.’”
# 
# Write a function that can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three.
# 
# negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

# In[71]:


email_three = open("email_three.txt", "r").read()
new_email_three = email_three.split()
#print(new_email_three)
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def new_email_three_censor(new_email_three, negative_words):
    
    for x, y  in enumerate(new_email_three[:-3]):
        if new_email_three[x+1] == "algorithms" and new_email_three[x] == "learning":
            new_email_three[x] = "xxxxx" 
            new_email_three[x+1] = "xxxxxx"
        elif new_email_three[x+1] == "matrix" and new_email_three[x] == "personality":
            new_email_three[x] = "xxxxx" 
            new_email_three[x+1] = "xxxxxx"
        elif new_email_three[x+2] == "self" and new_email_three[x+1] == "of" and new_email_three[x] == "sense" :
            new_email_three[x] = "xxxxx" 
            new_email_three[x+1] = "xxxxxx"
            new_email_three[x+2] = "xxxxxx"
        elif new_email_three[x] == "she" or new_email_three[x] == "She" or new_email_three[x] == "(she" :
            new_email_three[x] = "xxxxx"
        elif new_email_three[x] == "self-preservation":
            new_email_three[x] = "xxxxx"
        elif new_email_three[x] == "her" or new_email_three[x] == "Her":
            new_email_three[x] = "xxxxx"
        elif new_email_three[x] == "herself" or new_email_three[x] == "Herself" :
            new_email_three[x] = "xxxxx"
        
            
    for i, x in enumerate(new_email_three):
        for y in negative_words:
            if y[:1] == x[:1] and negative_words.count(y[:1])>1:
                new_email_three[i] = "XXX"
                
            break
        
            
new_email_three_censor(new_email_three, negative_words)
#print(new_email_three)
text_new_email_three_censored = " ".join(new_email_three)
print(text_new_email_three_censored)     
            


# # This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He tells you, “our company would be ruined! Censor it! Censor it all!”
# 
# Write a function that censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words in email_four that come before AND after a term from those two lists.

# In[60]:


email_four = open("email_four.txt", "r").read()
#print(email_four)
new_email_four = email_four.split()
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]


    
for x, y  in enumerate(new_email_four[:-3]):
    if new_email_four[x+1] == "algorithms" and new_email_four[x] == "learning":
        new_email_four[x] = "xxxx" 
        new_email_four[x+1] = "xxxx"
        new_email_four[x+2] = "xxx"
        new_email_four[x-1] = "xxx"
    elif new_email_four[x] == "her" or new_email_four[x] == "Her" or new_email_four[x] == "her." :
        new_email_four[x] = "xxxxx"
    elif new_email_four[x] == "HELP!":
        new_email_four[x] = "xxxxx"
    
    
for i, x in enumerate(new_email_four):
    for y in negative_words:
        if y[:3] == x[:3]:
            new_email_four[i] = "XXX"
            new_email_four[i+1] = "XXX"
            new_email_four[i-1] = "XXX"
            break
            
for l, g in enumerate(new_email_four):
    for z in proprietary_terms:
        if z[:3] == g[:3]:
            new_email_four[l] = "XX"
            new_email_four[l+1] = "XX"
            new_email_four[l-1] = "XX"
            break

               
#print(new_email_four)  
text_new_email_four_censored = " ".join(new_email_four)
print(text_new_email_four_censored)         


# In[ ]:




