while True:
    meme_dict = {
                "КРИНЖ": "Что-то очень странное или стыдное",
                "ЛОЛ": "Что-то очень смешное",
                'РОФЛ': 'шутка',
                'ЩИЩ': 'одобрение или восторг',
                'КРИПОВЫЙ': 'страшный, пугающий',
                'АГРИТЬСЯ': 'злиться'
                }
    word = input("Введите непонятное слово только большими буквами")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("хз что это чел вообще ты кринж ботяра")
