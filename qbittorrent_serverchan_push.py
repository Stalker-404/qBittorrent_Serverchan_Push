# -*- coding: utf-8 -*-
"""qBittorrent_Serverchan_Push.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fjzkVSjta7PR_1Uts_kz17g21m9l26-p
"""

import requests
import sys
import math
from urllib.parse import quote

# 获取参数
torrent_name = sys.argv[1] #torrent名称
torrent_dir = sys.argv[2] #torrent存储位置
filesize_Byte = int(sys.argv[3]) #文件大小，单位Byte，类型int
file_num = sys.argv[4] #文件个数
key = "**********************************" #填入通过Serverchan获取的sendkey

# 文件大小单位自适应转换
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

filesize_converted = convert_size(filesize_Byte) #将Byte转换为不同的单位，类型str

# 根据markdown语言规则，更改方括号的表达字符
torrent_name = torrent_name.replace("[", "\["); 
torrent_name = torrent_name.replace("]", "\]");
torrent_dir = torrent_dir.replace("[", "\[");
torrent_dir = torrent_dir.replace("]", "\]");

# 定义推送标题和内容
title = "qBittorrent下载完成" #标题
content = """
**种子名称：**{}\n
**保存位置：**{}\n
**文件大小：**{}\n
**文件个数：**{}
""".format(torrent_name,torrent_dir,filesize_converted,file_num)#信息内容

# 进行URL转义
content = quote(content, 'utf-8')

# 发送信息
requests.get("https://sc.ftqq.com/{}.send?text={}&desp={}".format(key,title,content))