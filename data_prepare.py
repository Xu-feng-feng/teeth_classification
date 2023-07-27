# Lint as: python3
# coding=utf-8
# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Prepare data for further process.

Read data from "/slope", "/ring", "/wing", "/negative" and save them
in "/data/complete_data" in python dict format.

It will generate a new file with the following structure:
├── data
│└── complete_data
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import json
import os
import random

LABEL_NAME = "gesture"
DATA_NAME = "accel_ms2_xyz"
# folders = ["wing", "ring", "slope"]
folders = ['1', '2', '3', '4']
# folders = ['1', '7', '11']
# names = ["zhangxy"]
names = ['fjx', 'fqh', 'hly', 'hzq', 'jl', 'lj', 'lx', 'lzm', 'mr', 'msw', 'qyj', 'sj', 'wb', 'wyy', 'xwf', 'zw', 'zyy', 'zzc']
# names = ['zzc']





# 它的作用是读取文件中收集好的数据，并将其解析、添加到data列表中。


def prepare_original_data(folder, name, data, file_to_read):  # pylint: disable=redefined-outer-name
  """Read collected data from files."""
  if folder != "negative":
    with open(file_to_read, "r") as f:    # 这部分代码处理folder不等于"negative"的情况。它打开名为file_to_read的文件，并用csv.reader读取文件的每一行。
      lines = csv.reader(f)               # 然后，它创建一个新的字典data_new，并为它设置了LABEL_NAME、
      data_new = {}                       # DATA_NAME和"name"三个键的初始值。随后，开始循环遍历文件中的每一行。
      data_new[LABEL_NAME] = folder     
      data_new[DATA_NAME] = []           
      data_new["name"] = name            
      for idx, line in enumerate(lines):  # pylint: disable=unused-variable,redefined-outer-name  
        if len(line) == 3:                                 #  对于每一行，首先判断行的长度是否为3。如果是，继续执行下面的逻辑。如果不是，跳过当前行。
          if line[2] == "-" and data_new[DATA_NAME]:     #  如果第三个元素（line[2]）等于"-"，并且data_new[DATA_NAME]不为空，则表示已完成一个数据集，
            data.append(data_new)                       # 将data_new添加到data列表中，并重新创建一个新的data_new字典，并为其设置各项初始值。
            data_new = {}
            data_new[LABEL_NAME] = folder
            data_new[DATA_NAME] = []
            data_new["name"] = name
          elif line[2] != "-":                          # 如果第三个元素（line[2]）不等于"-"，则将前三个元素（line[0:3]）转换为浮点数，并追加到data_new[DATA_NAME]列表中。
            data_new[DATA_NAME].append([float(i) for i in line[0:3]])   # 最后，将data_new添加到data列表中。
      data.append(data_new)



  else:
    with open(file_to_read, "r") as f:
      lines = csv.reader(f)
      data_new = {}
      data_new[LABEL_NAME] = folder
      data_new[DATA_NAME] = []
      data_new["name"] = name
      for idx, line in enumerate(lines):
        if len(line) == 3 and line[2] != "-":
          if len(data_new[DATA_NAME]) == 120:
            data.append(data_new)
            data_new = {}
            data_new[LABEL_NAME] = folder
            data_new[DATA_NAME] = []
            data_new["name"] = name
          else:
            data_new[DATA_NAME].append([float(i) for i in line[0:3]])
      data.append(data_new)

"""
这部分代码处理folder等于"negative"的情况。它打开名为file_to_read的文件，并用csv.reader读取文件的每一行。然后，它创建一个新的字典data_new，并为它设置了LABEL_NAME、DATA_NAME和"name"三个键的初始值。随后，开始循环遍历文件中的每一行。

对于每一行，首先判断行的长度是否为3，并且第三个元素（line[2]）不是"-"。如果是，继续执行下面的逻辑。如果不是，跳过当前行。

如果data_new[DATA_NAME]列表的长度等于120，则表示已完成一个数据集，将data_new添加到data列表中，并重新创建一个新的data_new字典，并为其设置各项初始值。

否则，将前三个元素（line[0:3]）转换为浮点数，并追加到data_new[DATA_NAME]列表中。

最后，将data_new添加到data列表中。

以上就是这段代码的解释。它的作用是读取文件中收集好的数据，并将其解析、添加到data列表中。

"""




# 第一种类型是"Big movement -> around straight line"，
# 当i大于80时生成，其中字典dic的键值对包括"data"、"label"和"name"。start_x、start_y和start_z是随机生成的初始坐标，
# x_increase、y_increase和z_increase是随机增长量。
# 在128次循环中，通过在初始坐标上依次叠加增长量、随机浮动量来生成三维数据点，并将其添加到dic[DATA_NAME]中。


def generate_negative_data(data):  # pylint: disable=redefined-outer-name                         
  """Generate negative data labeled as 'negative6~8'.     """                  
  # Big movement -> around straight line  
  for i in range(100):
    if i > 80:
      dic = {DATA_NAME: [], LABEL_NAME: "negative", "name": "negative8"}
    elif i > 60:
      dic = {DATA_NAME: [], LABEL_NAME: "negative", "name": "negative7"}
    else:
      dic = {DATA_NAME: [], LABEL_NAME: "negative", "name": "negative6"}
    start_x = (random.random() - 0.5) * 2000
    start_y = (random.random() - 0.5) * 2000
    start_z = (random.random() - 0.5) * 2000
    x_increase = (random.random() - 0.5) * 10
    y_increase = (random.random() - 0.5) * 10
    z_increase = (random.random() - 0.5) * 10
    for j in range(128):
      dic[DATA_NAME].append([
          start_x + j * x_increase + (random.random() - 0.5) * 6,
          start_y + j * y_increase + (random.random() - 0.5) * 6,
          start_z + j * z_increase + (random.random() - 0.5) * 6
      ])
    data.append(dic)
  # Random
  for i in range(100):                                                        # 第二种类型是"Random"，当i大于60时生成。
    if i > 80:                                                                # 与第一种类型不同的是，该类型的数据点是随机生成的三维坐标，而没有依赖于初始坐标和增长量。
      dic = {DATA_NAME: [], LABEL_NAME: "negative", "name": "negative8"}      # 生成的数据点的数量也是128个。
    elif i > 60:
      dic = {DATA_NAME: [], LABEL_NAME: "negative", "name": "negative7"}
    else:
      dic = {DATA_NAME: [], LABEL_NAME: "negative", "name": "negative6"}
    for j in range(128):
      dic[DATA_NAME].append([(random.random() - 0.5) * 1000,
                             (random.random() - 0.5) * 1000,
                             (random.random() - 0.5) * 1000])
    data.append(dic)
  # Stay still                                                               # 第三种类型是"Stay still"，在每次循环中使用随机初始坐标和固定的浮动范围生成静止不动的三维数据点。
  for i in range(100):
    if i > 80:
      dic = {DATA_NAME: [], LABEL_NAME: "negative", "name": "negative8"}
    elif i > 60:
      dic = {DATA_NAME: [], LABEL_NAME: "negative", "name": "negative7"}
    else:
      dic = {DATA_NAME: [], LABEL_NAME: "negative", "name": "negative6"}
    start_x = (random.random() - 0.5) * 2000
    start_y = (random.random() - 0.5) * 2000
    start_z = (random.random() - 0.5) * 2000
    for j in range(128):
      dic[DATA_NAME].append([
          start_x + (random.random() - 0.5) * 40,
          start_y + (random.random() - 0.5) * 40,
          start_z + (random.random() - 0.5) * 40
      ])
    data.append(dic)


# Write data to file
def write_data(data_to_write, path):
  with open(path, "w") as f:
    for idx, item in enumerate(data_to_write):  # pylint: disable=unused-variable,redefined-outer-name
      dic = json.dumps(item, ensure_ascii=False)
      f.write(dic)
      f.write("\n")

"""
最后，通过循环将生成的数据字典添加到传入的data列表中。

另外，代码中还包括一个write_data函数，用于将data列表中的数据写入文件。每个数据字典通过json.dumps转换为JSON格式，并写入文件中。每个数据字典之间使用换行符分隔。
"""


if __name__ == "__main__":
  data = []  # pylint: disable=redefined-outer-name
  for idx1, folder in enumerate(folders):
    for idx2, name in enumerate(names):
      prepare_original_data(folder, name, data,
                            "C:\\dataset\\imu_demo\\trainv3\\data\\2023_7_20\\%s\\extracted_extracted_new_output_%s_%s.txt" % (folder, folder, name))
  # for idx in range(5):
  #   prepare_original_data("negative", "negative%d" % (idx + 1), data,
  #                         "./negative/output_negative_%d.txt" % (idx + 1))
  # generate_negative_data(data)
  print("data_length: " + str(len(data)))
  if not os.path.exists("./data"):
    os.makedirs("./data_7_26")
  write_data(data, "./data_7_26/complete_data")


