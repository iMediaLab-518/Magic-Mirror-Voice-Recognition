# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 23:13:54 2018

@author: asus
"""

from wav import WWAV
from AipSpeech import Translation

w = WWAV()
x = Translation()
count = 0

while count <= 10 : # 录制测试次数
    w.my_record() # 开始录制，无参数传入，则为默认TIME为60，INTERVAL为5
    
    count+=1
    condition, word = x.get_word("01.wav") # 得到转换后的信息
    print("\n")

    if condition == 1:
        print("转换内容为：" + word) # 有效转换则返回转换后的文本
    else:
        print("等待语音录入")
        
    