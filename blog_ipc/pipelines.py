# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class BlogIpcPipeline(object):
	def __init__(self):
		self.conn = sqlite3.connect('blog_ipc.db')
		self.cursor = self.conn.cursor()
		self.cursor.execute("select count(*) from sqlite_master where type = 'table' and name = 'blogs'")
		if self.cursor.fetchone()[0]==0:
			self.cursor.execute('create table blogs (id integer primary key autoincrement, title varchar(255), url varchar(255))')
		# self.cursor.rowcount
		# self.cursor.close()
		# self.conn.commit()
		# self.conn.close()
		
	def process_item(self, item, spider):
		self.cursor.execute('insert into blogs (title, url) values(?, ?)', (item['blog_title'], item['blog_url']))
		self.conn.commit()

		return item
