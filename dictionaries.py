# coding: utf-8
#dictionaries {}
empty_dict = {}
dict1 = grades{ "saj":77 , "neets":99 , "shivani":100}
grades = { "saj":77 , "neets":99 , "shivani":100}
grades.get("saj")
grades.get("No One")
grades.get("ss",0)
grades["saj"] = 88
grades.get("saj")
tweet = {
"user" : "mbc",
"text" : "Promotion of coll"
"retweet_count" : 12
"hastags" : ["reunion", "nostalgia", "kuttikanam", "alcohol"]
}
tweet = {
"user" : "mbc",
"text" : "Promotion of coll",
"retweet_count" : 12,
"hastags" : ["reunion", "nostalgia", "kuttikanam", "alcohol"]
}
tweet_keys= tweet.keys()
print (tweek_keys)
print (tweet_keys)
print (tweet.values())
print (tweet.items())
user in tweet.keys
user in tweet.keys()
"user" in tweet.keys()
"user" in tweet
document = "This is as good as it gets for for the this is good drama. drama is not goot for netflix ..who said is is is pi pi pi pi pi pi haha hah haha ha ha "
new_dict = {}
# for every word in a dccument , scan the whole dccument. The count value is inCREMENTED based on the prescence. 
for word in document:
    prev_count = new_dict.get(word ,0)
    new_dict[word] = prev_count + 1
    # assign value to a key  
   
print (new_dict)
