from pytube import YouTube as yt
import asyncio as asy

adres = input("İndirilecek yer: ")

with open("indirilecekler.txt", "r") as f:
    dosya = f.readlines()
    temizliste = []
    for i in dosya:
        temizliste.append(i.replace("\n", ""))


for i in temizliste:
    try:
        yt(i).streams.get_by_itag("22").download(adres)
    except:
        continue
