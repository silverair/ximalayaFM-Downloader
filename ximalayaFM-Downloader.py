# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 03:27:36 2018

@author: RRR
"""

import requests


def getTracksList(albumId,page):
    
    trackList=[]
    headers = {'user-agent': 'my-app/0.0.1'}
    
    albumIdUrl='https://www.ximalaya.com/revision/album/getTracksList?albumId=' + str(albumId) + '&pageNum=' + str(page)

    result=requests.get(albumIdUrl,headers = headers)
    result=result.json()
    tracks = result['data']['tracks']
    
    for track in tracks:
        trackList.append({'index':track['index'],'trackId':track['trackId'],'title':track['title']})
        
        
    return trackList
    

def getTrack(trackId):
    headers = {'user-agent': 'my-app/0.0.1'}
    TrackUrl='https://www.ximalaya.com/revision/play/tracks?trackIds=' + str(trackId)
    result=requests.get(TrackUrl,headers = headers)
    result=result.json()
    
    src=result['data']['tracksForAudioPlay'][0]['src']
    
    return src
    
    
    
def download(src,filename):
    headers = {'user-agent': 'my-app/0.0.1'}
    result=requests.get(src,headers = headers,stream=True)
    
    with open(filename,'wb') as f:
        for chunk in result.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
        


albumId=input("請輸入專輯ID:")
page=int(input("請輸入起始頁數:"))
pageEnd=int(input("請輸入結束頁數:"))+1

for i in range(page,pageEnd):
    
    TracksList=getTracksList(albumId,i)
    for Tracks in TracksList:
        src=getTrack(Tracks['trackId'])
        
        if src:
            print("正在下載"+Tracks['title'])
            filename=str(int(Tracks['index'])-1)+'.m4a'
            download(src,filename)
            print("完成下載"+Tracks['title'])
        
print("全部下載完成")

