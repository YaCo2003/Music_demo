'''
description:这里是爬取用户最喜爱的top100音乐板块
'''
import requests
from bs4 import BeautifulSoup
import csv

# 构造函数获取作者的所有热门歌曲，注意最多只有50，可能不到50
# P.S.那些小众作者好烦啊，经常出bug
def get_top100(url,artist_id):
    r = requests.get(url)
    soup = r.json()
    print(soup)
    filename = f'Plate_2/data/artist_music/artist_{artist_id}.csv'
    try:
        with open(filename, 'a', encoding='utf-8-sig', newline='') as csvfile:    # 文件存储的位置
            writer = csv.writer(csvfile)
            for song in soup['hotSongs']:
                song_id = song['id']
                song_name = song['name']
                # 使用 .get() 方法以避免 'al' 字段不存在导致的异常
                album_info = song.get('al', {})
                song_url = album_info.get('picUrl', 'Unknown')  # 使用 'Unknown' 或其他默认值
                try:
                    writer.writerow((song_id,song_name,song_url))
                except Exception as msg:
                    print(msg)
    except Exception as e:
        print(f"Error occurred: {e}")

#主操作函数，只是迎来控制爬取url的循环
def main(artist_id):
    print(f"获取了music{artist_id}")
    filename = f'Plate_2/data/artist_music/artist_{artist_id}.csv'
    # 创建新文件
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('song_id', 'song_name', 'song_url'))

    url = 'http://localhost:3000/artists?id=' + str(artist_id)
    # 开始获取数据
    print('enter:', url)
    get_top100(url, artist_id)
