# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:32:28 2018

@author: asus
"""

from aip import AipSpeech
#from .base import base64
""" 你的 APPID AK SK """
class Translation:
    
    APP_ID = '11037665'
    API_KEY = 'h3KGlvCyAR4uGo42gr2GGCUm'
    SECRET_KEY = '0cca61727702fe14f0a62cf4e9cb1d9e'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
             return fp.read()
    #F:\Magic-Mirror-Voice-Recognition\wav\iflytek02.wav   
    def get_word(self,filePath):
        word=self.client.asr(self.get_file_content(filePath), 'wav', 16000, {
    'dev_pid': '1536',
})
        if word['err_no'] == 0: # 错误值为0（即正确）
            return 1,word['result'][0] # 返回 1 与 文本信息
        else:
            return 0,word['err_no'] # 否则返回 0 与 错误内容
        
    def __init__(self):
        pass
   