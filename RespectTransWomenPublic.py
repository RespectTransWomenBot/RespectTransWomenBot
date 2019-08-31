import praw #you probably know what this is 
import base64 #encoded passwords
r = praw.Reddit(user_agent='Transphobia Notifier by /u/RespectTransWomenBot',
                         client_id='YOURIDHERE', client_secret="YOURSECRETHERE",
                         username='RespectTransWomenBot', password=base64.b64decode(b"YOURPASSWORDHERE").decode("utf-8", "ignore"))
r.read_only = False #no idea if this is required. Kept it to be safe.
subreddit = r.subreddit("ShrellexBotTesting") #get the subreddit. "all" for all comments
f = open("D:\Reddit Bots\Respect Trans Women\repliedto.txt", "r+") 

    

comments = subreddit.stream.comments() # get the comment stream
x = 1 #for the counter
for comment in comments: #for each comment in the comments stream. the current comment being processed is called "comment"
    print("found new comment! processing... (" + str(x) + ")") #the str(x) thing is printing the number of the comment being proccesed
    x += 1 #add 1 to the number
    text = str(comment.body) # Fetch body
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

    if text.lower == "Shemale" or "Ladyboy" or "tranny" or "trannie" or "she-man" or "transvestite" or "chick with dick" or "chicks with dicks" or "dickgirl" or "men with tits" or "HeShe" or "He-She": #IDK if I implemented non case sensitivity right. its 3 am... ORIGINAL COMMENT HERE: check to see the comment is "!lmgtfy". use if text.lower() == "!lmgtfy".lower() to be non-case sensitive, use if "!lmgtfy" in text if you want the comment to be anywhere
        if comment.id in f.read(): #if the comment is already in the file, bot has replied to it
            print("ALREADY IN FILE")
        if comment.id not in f.read(): #^
            # Generate a message
            print("Attempting Answer")
            parid = comment.parent_id #by /u/bboe
            parbody = r.comment(comment.parent_id.rsplit('_', 1)[1])#by /u/bboe
            commentbody = comment.body #by /u/bboe, fetches the body of the parent comment
            message = "Please do not use" + (str(commentbody)) + "it is derogatory and a slur. Please use 'trans woman' instead." + "\n\n_____\n\n This is a bot." # ACTUAL COMMENT, idk really about the praw syntax, I'm pretty sure me just cramming commentbody in there will not work. Trying to quote the slur the user said
            try:
                comment.reply(message) #reply to comment

            except praw.errors.Forbidden:
                print('403 error - is the bot banned from sub %s?' % "not impl")
            print("Replied to comment by " + author)
            f.write(comment.id + "\n")#write comment id to file so it doesn't reply to it again
            if comment.id in f.read():
                print("Written Successfully!")