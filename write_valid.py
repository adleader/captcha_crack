#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

pwd = os.getcwd()
resources_path = "./products/trainval"
root_path = os.path.join(pwd, resources_path)
file_list = os.listdir(resources_path)

with open("./dataset/detector_valid/valid.list", "w") as f:
    for file in file_list:
        if file.endswith(".jpg"):
            file_path = os.path.join(root_path, file)
            f.write("{}\n".format(file_path))
