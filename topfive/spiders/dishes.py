from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from topfive.items import UrbanSpoonItem


class MySpider(BaseSpider):
	name = "top"
	allowed_domains = ["urbanspoon.com"]
	start_urls = ["http://www.urbanspoon.com/r/23/1581439/restaurant/Downtown-CBD/NOLA-on-the-square-Pittsburgh"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select('//div[@class="col-sm-12"]/ul/li/div/h3/a/text()')
		restaurant = hxs.select('//div[@class="container hidden-xs"]/ul/li/span/text()')
		items = []
		for titles in titles:
			item = UrbanSpoonItem()
			item["title"] = titles.extract()
			item["restaurant"] = restaurant.extract()
			# item["link"] = titles.select("a/@href").extract()
			items.append(item)
			#print items
		return items