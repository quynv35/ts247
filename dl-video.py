# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import re
import os

def login(): # login
	global s
	urlLogin = "https://tuyensinh247.com/eAjax/login"
	data = {"username" : "sahy168", "password" : "nhanduyen37"}
	s = requests.Session() 
	s.post(urlLogin,data = data)
	# ---------------
	link = "https://tuyensinh247.com/luyen-thi-thptqg-mon-toan-thay-nguyen-quoc-chi-k836.html"
	text = s.get(link).text
	return(s,text)

def find_topic_code(text): # tim list id cac chuyen de
	match = '"openTopic(.*)" class='
	list_topic = re.findall(match,text)
	return(list_topic)

def topic(code): # load id cac bai giang trong tung chuyen de
	url = "https://tuyensinh247.com/eLessonOnline/loadTopicInfo"
	data = {"topicId":""}
	data["topicId"] = code
	text = s.post(url,data = data)
	return(text.json())

def name_video(code): # tim ten va url video 
	list_name = []
	list_url = []
	data = topic(code)["msg"]
	for i in data:
		list_name.append(i["alias"])
		list_url.append("https://tuyensinh247.com"+i["url"])
	return(list_name,list_url)


def getText(url): # get source cua bai giang
	sourceCode = s.get(url).text
	return(sourceCode)


s,text = login()[0],login()[1]
list_item_id = find_topic_code(text)

sourceCode = getText(link)
iv = iv()
key = key(sourceCode)
urlVideo = urlVideo(sourceCode)



