import feedparser
from datetime import datetime
import pathlib

URL = 'https://moyutime-hub.vercel.app/xiaoyuzhou/podcast/6161387b0a191aa6100b4656'
IMG_URL = 'https://moyutime-podcast.github.io/image/img.jpg'


feed = feedparser.parse(URL)
entries = feed['entries']

size = index = len(entries)

for entry in entries:
    title = entry['title']
    date = entry['published']
    date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT")
    date = date.strftime('%Y-%m-%d')

    detail = entry['title_detail']
    player = '{% aplayer ' + f'"{title}"' + ' moyu-time ' + ' ' + entry['links'][1]['href']  + ' ' + IMG_URL + ' %}'

    md_builder = \
    f'''---
title: "{title}"
date: {date}
---

{player}

**[Link]({entry['id']})**

## Summary
{entry['summary']}
    '''

    pathlib.Path(f'source/_posts/vol{index}.md').write_text(md_builder)
    print(f'generate md file for source/_posts/vol{index}.md')
    index -= 1