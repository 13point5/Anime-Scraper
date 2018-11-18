s = ["/anime/genre/1/Action" 
,"/anime/genre/2/Adventure"
,"/anime/genre/3/Cars"
,"/anime/genre/4/Comedy"
,"/anime/genre/5/Dementia" 
,"/anime/genre/6/Demons"
,"/anime/genre/8/Drama"
,"/anime/genre/9/Ecchi"
,"/anime/genre/10/Fantasy"
,"/anime/genre/11/Game"
,"/anime/genre/35/Harem"
,"/anime/genre/12/Hentai"
,"/anime/genre/13/Historical"
,"/anime/genre/14/Horror"
,"/anime/genre/43/Josei"
,"/anime/genre/15/Kids"
,"/anime/genre/16/Magic"
,"/anime/genre/17/Martial_Arts"
,"/anime/genre/18/Mecha"
,"/anime/genre/38/Military"
,"/anime/genre/19/Music"
,"/anime/genre/7/Mystery"
,"/anime/genre/20/Parody"
,"/anime/genre/39/Police"
,"/anime/genre/40/Psychological"
,"/anime/genre/22/Romance"
,"/anime/genre/21/Samurai"
,"/anime/genre/23/School"
,"/anime/genre/24/Sci-Fi"
,"/anime/genre/42/Seinen"
,"/anime/genre/25/Shoujo"
,"/anime/genre/26/Shoujo_Ai"
,"/anime/genre/27/Shounen"
,"/anime/genre/28/Shounen_Ai"
,"/anime/genre/36/Slice_of_Life"
,"/anime/genre/29/Space"
,"/anime/genre/30/Sports"
,"/anime/genre/31/Super_Power"
,"/anime/genre/37/Supernatural"
,"/anime/genre/41/Thriller"
,"/anime/genre/32/Vampire"
,"/anime/genre/33/Yaoi"
,"/anime/genre/34/Yuri"]

import re

d={}

for i in s:
    ii=i.split("/")
    d[ii[-1]]=ii[-2]

print(d)