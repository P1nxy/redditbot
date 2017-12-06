import praw
import time

r = praw.reddit(user_agent = "Schoolbot by Marek /u/Marki_Bot")#redditi useri nimi
print("Sisse logimine...")
r.login()#siia saab lisada logini, et ei peaks koguaeg sisse logima aga see ei ole turvaline kui programmi sheerida

words_to_match = ['tee siia list mis sõnadele, mida ta kontrollib!!']
cache = [] #siia storetakse kõik kommentid

def run_bot():
    print("sisenen subredditisse...")
    subreddit = r.get_subreddit("test/koolibot") #thredi nimi, vaata üle seda. testi.
    print("Vaatan komentaare...")
    comment = subreddit.get_comments(limit=25)#et bot ei overloadiks redditi serveri
    for comment in comments:
        comment_text = comment.body.lower()#Kui see matchi sõna on suuretähega kirjutatud siis ikkagi saaks aru sellest ja võtaks seda kui matchina
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in cache and isMatch:#et ta ei vastaks koguaeg samale komentaarile
            ("Match on leitud! komentaari ID:" + comment.id)
            comment.reply(' Siia komm mida bot vastab!!')
            print("Vastus õnnestus!")
            cache.append(comment.id)
    print("Üks loop tehtud aeg on magada..")
            

while true:
    run_bot()
    time.sleep(10)#cooldown time