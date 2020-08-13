# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import os

def login():
	global s
	urlLogin = "https://tuyensinh247.com/eAjax/login"
	data = {"username" : "sahy168", "password" : "nhanduyen37"}
	s = requests.Session() 
	s.post(urlLogin,data = data)
	return(s)

def text(link):
	link = link
	text = requests.get(link).text
	return(text)

def find_topic_code(text):
	match = 'openTopic(.*)\" class'
	list_topic = re.findall(match,text)
	return(list_topic)

def topic(code):
	url = "https://tuyensinh247.com/eLessonOnline/loadTopicInfo"
	data = {"topicId":""}
	data["topicId"] = code
	sourceCode = s.post(url,data = data)
	return(sourceCode.json())

def download_pdf(item_id,name):
	err404 = "<h1>404</h1>"
	temp1  = "https://tuyensinh247.com/eExamOnline/downloadAttachFile/item_id/{0}/item_type/1".format(item_id)
	temp2  = "https://tuyensinh247.com/eExamOnline/downloadAttachFile/item_id/{0}/item_type/2".format(item_id)
	name = name.replace("\\)","").replace("\\(","").replace("/",":")+".pdf"
	f = open(name,"wb")
	content1 = s.get(temp1).text
	if err404 not in content1:
		content = s.get(temp1).content
	else:
		content = s.get(temp2).content
	f.write(content)
	f.close()
	return(name)



link = "https://tuyensinh247.com/luyen-thi-thptqg-mon-toan-thay-nguyen-quoc-chi-k836.html"

s = login()
text = text(link)
list_topic = find_topic_code(text)
# ['3033', '3035', '3034', '4306', '3046', '3036', '3038', '3037', '3708', '3039', '3045', '3040', '3042', '3041', '3043', '3044']

list_list_name = []
list_list_item_id = []

for code in list_topic:
	item_id = []
	name = []
	data = topic(code)["msg"]
	for i in data:
		item_id.append(i["item_id"])
		name.append(i["title"])
	list_list_item_id.append(item_id)
	list_list_name.append(name)

for i in range(len(list_list_item_id)):
	cmd = "mkdir {0}".format(i+1)
	os.system(cmd)
	list_item_id = list_list_item_id[i]
	list_name = list_list_name[i]
	for j in range(len(list_item_id)):
		item_id = list_item_id[j]
		name = list_name[j]
		download_pdf(item_id,name)
		print(name)
	cmd = "mv *.pdf {0}".format(i+1)
	os.system(cmd)
	print()