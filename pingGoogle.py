from django.contrib.sitemaps import Sitemap 
from django.contrib.sitemaps import ping_google
from models import Post 
from django.conf import settings 
from datetime import datetime 

class PostSite(Sitemap): 
	changefrep = "daily"
	priority = .5 

	def items(self): 
		return Post.objects.all()

	def lastmod(self, obj): 
		return datetime.now()

def ping_search_engines(sitemap_url='http://'+settings.SITE_URL+'/sitemap.xml'):
	SEARCH_ENGINE_PING_URLS = (
		('google', 'http://www.google.com/webmasters/tools/ping')
	)
	successfully_pinged = []
	for (site, url) in SEARCH_ENGINE_PING_URLS:
		try: 
			ping_google(sitemap_url=sitemap_url, ping_url=url)
			ping = True
		except:
			pinged = False
		if pinged: 
			successfully_pinged.append(site)
	return successfully_pinged