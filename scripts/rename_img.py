#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

my_path = "C:\\Users\\李谦\\Desktop\\网易云-验证码-点选\\new"
file_list = os.listdir(my_path)
file_list.sort()

base_num = 100000

for index, f in enumerate(file_list):
    before_file = os.path.join(my_path, f)
    after_file = os.path.join(my_path, "{}.jpg".format(base_num + index + 111))
    print("{} -> {}".format(before_file, after_file))
    os.rename(before_file, after_file)