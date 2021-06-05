import requests
import bs4
# fetching from given sites
def get_all_song_link(url):
    resp=requests.get(url)
# print(resp.content)
# Parsing all
    ret=[]
    soup=bs4.BeautifulSoup(resp.content,features="html.parser")
# print(soup)

# find all title
    title=soup.find_all("title")  
# print(title)

#find all thing which has tag
    link =soup.find_all("a",attrs={"class":"title"})
    for i in link:
        ret.append(i['href'])  #Only link got printed
    return ret

def get_song_lyrics(url):
    lyrics=[]
    resp=requests.get(url)
    soup=bs4.BeautifulSoup(resp.content,features="html.parser")
    lyrics_link=soup.find_all("p",attrs={"class":"verse"})
    for i in lyrics_link:
        lyrics.append(i.get_text())
    return "\n".join(lyrics)
def get_file_name(url):
    return url.split("/")[-1].replace(".html",".txt")


def main():
    link=get_all_song_link("https://www.metrolyrics.com/grateful-dead-lyrics.html")
    for i in link:
        file_name=get_file_name(i)
        f=open(file_name,'w')
        lyrics=get_song_lyrics(i)
        f.write(lyrics)
        f.close()
if __name__=="__main__":
    main()
else:
    print("I am being imported")