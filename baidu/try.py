# -*- coding: utf-8 -*-
"""
Created on Mon May  7 20:59:16 2018

@author: asus
"""

from aip import AipSpeech
import os
""" 你的 APPID AK SK """
APP_ID = '11037665'
API_KEY = 'h3KGlvCyAR4uGo42gr2GGCUm'
SECRET_KEY = '0cca61727702fe14f0a62cf4e9cb1d9e'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
filePath='test.wav'

# 识别本地文件
def getword(filePath):
    word=client.asr(get_file_content(filePath), 'wav', 16000, {
    'dev_pid': '1536',
})
    if word['err_no'] == 0: # 错误值为0（即正确）
            print(word['result'][0]) # 返回 1 与 文本信息
    else:
            print(word['err_no']) # 否则返回 0 与 错误内容

while(True):
    os.system('arecord -r 16000 -f S16_LE -D "plughw:1,0" -d 4 test.wav')
    getword(filePath)
