meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "OMG": "Aman Tanrım Yani Oh My God Anlamına Gelir"
    "BRO": "Arkadaş Manasına Gelir"
}

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print("Kelimenin Anlamı:", meme_dict[word])
else:
    print("Bu kelime sözlükte bulunmuyor.")
