TRACK_TERMS = ["#haddad", "#agoraehaddad", "#haddadpresidente", "#haddad13", "#haddadmanu", "#haddademanu","#haddad2018", "#bolsonaro", "#bolsonaro2018", "#bolsonaro17", "#bolsonaropresidente", "#bolsonarosim", "#bolsonaronao", "#bolsonaropresidente2018", "#bolsonaropresidente17", "#EuVotoBolsonaro", "#bolsonaropresidentedobrasil", "#jairbolsonaro" ,"#haddadnao", "#elesim" ,"#elenao", "#elenunca", "#haddadelula",  ]
CONNECTION_STRING = "sqlite:///tweets_eleicao2018_2T.db"
CSV_NAME = "2018_08_tweets.csv"
TABLE_NAME = "Eleicoes"
TWITTER_APP_KEY = ''
TWITTER_APP_SECRET = ''
TWITTER_KEY = ''
TWITTER_SECRET = ''

try:
    from private import *
except Exception:
    pass


# "#haddad", 
# "#agoraehaddad", 
# "#haddadpresidente", 
# "#haddad13", 
# "#haddadmanu", 
# "#haddademanu",
# "#haddad2018", 
# "#haddadelula"

# "#bolsonaro", 
# "#bolsonaro2018", 
# "#bolsonaro17", 
# "#bolsonaropresidente", 
# "#bolsonarosim", 
# "#bolsonaronao", 
# "#bolsonaropresidente2018", 
# "#bolsonaropresidente17", 
# "#EuVotoBolsonaro", 
# "#bolsonaropresidentedobrasil", 
# "#jairbolsonaro" ,

# "#haddadnao", 
# "#elesim" ,
# "#elenao", 
# "elenunca", 
