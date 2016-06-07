# -*- coding: utf-8 -*-
from scrapy import log
from scrapy.spider import BaseSpider
from blog_ipc.items import BlogIpcItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
import scrapy



class IpcSpider(scrapy.Spider):
	name = 'ipc.me'
	allowed_domains = ['ipc.me']
	start_urls = [
	'http://www.ipc.me',
	]
	headers = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2,fa;q=0.2',
		'Cache-Control': 'max-age=0',
		'Connection': 'keep-alive',
		'Host': 'www.ipc.me',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
	}
	
	
	def parse(self, response):
		if response.status == 200:
			blog_titles = response.xpath("//div/h2[@class='entry-title']/a/text()").extract()
			blog_urls = response.xpath("//div/h2[@class='entry-title']/a/@href").extract()
			for i in range(len(blog_urls)):
				item = BlogIpcItem()
				item['blog_title'] = blog_titles[i]
				item['blog_url'] = blog_urls[i]
				yield item



			next_page_url = response.xpath("//div[@class='prev-next']/a/@href").extract()
			print('===========================================================\n',next_page_url)
			print('___________________________________________________________')
			for url in next_page_url:
				yield Request(url, callback=self.parse)
			
			