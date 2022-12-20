import tweepy

client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAKtmkgEAAAAAusOc1vGWdEkty7wWwb%2B38ptDyJ8%3DVZbI8u3nuz1pAod4YwyzEK4F2LVt0UgpWvtXuBlaM8rYe0Bjnb")

#print(public_tweets)

people = {
    'elon musk' : 'elonmusk',
    'Joe Rogan' : 'joerogan',
    'Lex Fridman': 'lexfridman',
    'Andrew Huberman': 'hubermanlab',
    'David Goggins': 'davidgoggins'
}

user_name = input("Enter a @handle or pick from list(enter: people): ")
choice = ''
if(user_name[:1] == '@'):
    user_name = user_name[1:]

if(user_name == 'people'): 
    while(user_name != choice):
        temp = 0
        x = people.keys()
        print(x)
        choice = input('Enter name from index: ')
        for i in people:
            if(choice == i):
                temp = 0
                user_name = people[i]
                choice = user_name
                break
            else: temp = 1
        if(temp == 1):
            print("Enter a valid person")



#print("Twitter handle is: " + user_name)
information = client.get_user(username=user_name)

#print(information) #prints the raw response information
about = information[0]

id_person = about.get('id')
more_info = client.get_users_tweets(id_person, exclude='replies')

for i,j in about.items():
    print(i,":",j)
print("")
print("Their most recent tweets: ")
more_info = more_info[0]
temp = 1
for twt in more_info:
    print(temp,"",twt)
    print("")
    temp = temp + 1
