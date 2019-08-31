# RespectTransWomenBot
Reddit bot to combat transphobic slurs.

Sorry for my very limited development of this, I've only been working on it for a few hours, trying to understand praw and python.

#############################################################################################

Concern:

Line 31, I am unsure if I correctly enabled non case sensitivity. 

#############################################################################################
Concern:

Lines 37 to 40 confuse me; I was modeling off of this code https://pastebin.com/LfqKpTMp

  I added "commentbody = comment.body" to line 39, replacing what was:
  
                  parentbody = parbody.body #by /u/bboe, fetches the body of the parent comment
                          message = "http://lmgtfy.com/?q=" + quote(str(parentbody)
                          
  in the model. I need to dig more into PRAW, but I doubt I did that right.
