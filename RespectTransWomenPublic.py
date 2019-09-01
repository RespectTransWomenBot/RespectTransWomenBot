import praw #you probably know what this is
import base64 #encoded passwords
r = praw.Reddit(user_agent='Transphobia Notifier by /u/RespectTransWomenBot',
                         client_id='YOURIDHERE', client_secret="YOURSECRETHERE",
                         username='RespectTransWomenBot', password=base64.b64decode(b"YOURPASSWORDHERE").decode("utf-8", "ignore"))
r.read_only = False #False by default but better to keep as is incase it changes in the future
subreddit = r.subreddit("ShrellexBotTesting") #get the subreddit. "all" for all comments
f = open("D:\Reddit Bots\Respect Trans Women\repliedto.txt", "r+")

#blockedsubbreddits.txt formatting:
#subredditname\n (no \n on last line)
#e.g.
#traa
#gaysoundsshitposts
blocked_subreddits = [] #Initialize it so the bot doesn't crash if we can't open the file
with open("D:\Reddit Bots\Respect Trans Women\blockedsubreddits.txt", "r") as fs: #Path to .txt containing subs we don't post in
    blocked_subreddits = fs.read().lower().split('\n')

#triggerwords.txt formatting:
#triggerword\n (no \n on last line)
#e.g.
#shemale
#ladyboy
trigger_words = ["shemale", "ladyboy", "tranny", "trannie", "she-man", "transvestite", "chick with dick", "chicks with dicks", "dickgirl", "men with tits", "heshe", "he-she"] #Initialize it so the bot doesn't crash if we can't open the file
with open("D:\Reddit Bots\Respect Trans Women\triggerwords.txt", "r") as fs: #Path to .txt containing words we look for
    trigger_words = fs.read().lower().split('\n')

comments = subreddit.stream.comments() # get the comment stream
x = 1 #for the counter
for comment in comments: #for each comment in the comments stream. the current comment being processed is called "comment"
    print("found new comment! processing... (" + str(x) + ")") #the str(x) thing is printing the number of the comment being proccesed
    x += 1 #add 1 to the number
    if str(comment.subreddit).lower() in blocked_subreddits: #Check if we have the subreddit blacklisted since filtering subreddits with PRAW only works on submissions and not comments
        continue
    text = str(comment.body).lower() # Fetch body
    try:
        author = str(comment.author) # Fetch author
    except AttributeError: #check if the author has been deleted
        print("Author has been deleted")
        #author was deleted
        continue
    print(text) #DEBUGGING, REMOVE WHEN WORKING
    print(author) #SAME
    if author.lower() == "RespectTransWomenBot".lower(): #Don't reply to yourself
        #myself
        print("Comment is by myself")
        continue

    caught_words = []
    for i in trigger_words:
        if (i in text) and not (i in caught_words): #Check if the comment contains a word we're looking for. not (i in caught_words) is technically redundant but prevents the word being mentioned by the bot multiple times if it's repeated in trigger_words
            caught_words.append(i)
    message = "Please do not use "
    caught_len = len(caught_words)
    caught_iter = 1
    if caught_len > 2:
        for i in caught_words:
            if caught_len - caught_iter > 0: #Format the message in the form of "Please do not use a, b, or c. It is..."
                message += i + ", "
            else:
                message += "or " + i
            caught_iter += 1
    elif caught_len == 2:
        for i in caught_words:
            if caught_len - caught_iter > 0: #Format the message in the form of "Please do not use a or b. It is..."
                message += i
            else:
                message += " or " + i
            caught_iter += 1
    else:
        for i in caught_words:
            message += i #Format the message in the form of "Please do not use a. It is..."
    message += ". It is derogatory and a slur. Please use 'trans woman' instead.\n\n_____\n\n This is a bot."
    if caught_words:
        if comment.id in f.read(): #if the comment is already in the file, bot has replied to it.
            print("ALREADY IN FILE")
        else:
            # Generate a message
            print("Attempting Answer")
            try:
                comment.reply(message) #reply to comment
                print("Replied to comment by " + author)
            except praw.errors.Forbidden:
                print('403 error - is the bot banned from sub %s?' % "not impl")
            f.write(comment.id + "\n")#write comment id to file so it doesn't reply to it again
            if comment.id in f.read():
                print("Written Successfully!")
