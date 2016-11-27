from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import feedparser
from pprint import pprint

def index(request):
    url = 'http://rss.rssad.jp/rss/itm/1.0/netlab.xml'
    feeder = feedparser.parse(url)

    for entry in feeder['entries']:
        title = entry['title']
        summary = entry['summary']
        link = entry['link']

        context = {
            'title':title,
            'summary': summary,
            'link': link,
        }

    return render(request, 'feeder/index.html', context)
