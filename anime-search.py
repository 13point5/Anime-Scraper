from bs4 import BeautifulSoup
import requests
import operator


all_genres = {'Action': '1', 'Adventure': '2', 'Cars': '3', 'Comedy': '4', 'Dementia': '5', 'Demons': '6', 'Drama': '8', 'Ecchi': '9', 'Fantasy': '10', 'Game': '11', 'Harem': '35', 'Hentai': '12', 'Historical': '13', 'Horror': '14', 'Josei': '43', 'Kids': '15', 'Magic': '16', 'Martial_Arts': '17', 'Mecha': '18', 'Military': '38', 'Music': '19', 'Mystery': '7', 'Parody': '20', 'Police': '39','Psychological': '40', 'Romance': '22', 'Samurai': '21', 'School': '23', 'Sci-Fi': '24', 'Seinen': '42', 'Shoujo': '25', 'Shoujo_Ai': '26', 'Shounen': '27', 'Shounen_Ai': '28', 'Slice_of_Life': '36', 'Space': '29', 'Sports': '30', 'Super_Power': '31', 'Supernatural': '37', 'Thriller': '41', 'Vampire': '32', 'Yaoi': '33', 'Yuri': '34'}


animes={}

req_genres = list(input("Enter the genres space separated: ").split())
req_codes=[all_genres[i] for i in req_genres]
n_pages = int(input("Enter number of pages you wish to view(50 per page): "))
rating = float(input("Enter minimum rating of the animes you wish to view: "))

for i in range(1,n_pages+1):

    url = "https://myanimelist.net/anime/genre/"+all_genres[req_genres[0]] + "/" + req_genres[0]+"?page=" + str(i)
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html5lib")

    page_animes = soup.find_all('div', {'class': "seasonal-anime js-seasonal-anime"})

    for anime in page_animes:
        genres = anime["data-genre"].split(",")
        if len(set(req_codes) and set(genres))>=len(req_codes):
            anime_name = anime.find('a', {'class': 'link-title'}).text
            score = anime.find('span', {'class': 'score', 'title': 'Score'}).text
            if 'N/A' not in score:
                score = float(score.replace(" ",""))
                if(score>=rating):
                    animes[anime_name] = score
            else:
                print(anime_name, ' N/A')

sorted_animes = sorted(animes.items(), key=operator.itemgetter(1), reverse=True)


for k,v in sorted_animes:
    print(k, v)

    
