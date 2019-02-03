import praw
import re
import random


temoc_appreciation = \
[
"Temoc is the most handsome mascot at North Texas. He's beatiful to look at, freakishly charismatic, and remarkably athletic.",
"Enarc is a tryhard, fake savior of UTD's students. Temoc is the one true God.",
"Temoc is the hottest mascot in the DFW area. Even if he's not, at least he's better than SMU's mascot. And that's what truly matters.",
"Temoc is always watching what you're saying on this sub. Please use respectful language when talking about him and refrain from giving Enarc any more attention than he deserves.",
"Temoc is the tallest mascot in Richardson. Enarc is taller but he is a fake mascot. And he's not even the tallest crane in Richardson, have you seen the crane next to Target?",
"Enarc is freakishly tall and lanky, while Temoc is magnificent.",
"Temoc loves people of all races, all sexes and all religions. Temoc doesn't discriminate.",
"Enarc only has his height going for him. He's the kinda guy who just puts his height on his tinder bio. Temoc, on the other hand, is handsome, fit, and has a great personality. Charisma is everything. ",
]

words = ['temoc', 'temette', 'meme', 'memes',  'mascot', 'mascots', 'bot', 'spam', 'beautiful', 'fit', 'attractive', 'awesome', 'best', 'proud', 'utd', 'sex', 'sexy', 'charismatic', 'sports', 'nerd', 'f', 'nice', 'respect']

reddit = praw.Reddit('bot2')

subreddit = reddit.subreddit("utdallas")

for comment in subreddit.stream.comments():
    print(comment.author)
    comm = comment.body;
    if(any(substring in comm.lower() for substring in words)):
        if(comment.author != 'RedditKarmaIsABitch'):
            reply = "I'm a bot. I'm here to remind you that " + random.choice(temoc_appreciation) + " If you agree with the thoughts expressed in this message, please reply F to pay your respect to Temoc, our lord, Father and savior."
            comment.reply(reply)
            print(reply)
            

