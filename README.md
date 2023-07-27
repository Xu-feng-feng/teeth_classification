# 手势识别魔棒训练脚本

＃＃ 介绍

该目录中的脚本可用于训练 TensorFlow 模型
根据加速度计数据对手势进行分类。该代码使用Python 3.7和
TensorFlow 2.0。生成的模型大小小于 20KB。

以下文档包含有关使用脚本训练
模型，并捕获您自己的训练数据。
本项目的灵感来自于【手势识别魔棒】(https://github.com/jewang/gesture-demo)
詹妮弗·王的项目。

＃＃ 训练

### 数据集

选择了三种神奇手势，并从 7 个部位收集了数据
不同的人。收集并划分一些随机的长运动序列
分成更短的片段，这些片段与其他一些数据一起组成了“负”数据
自动生成随机数据。

数据集可以从以下网址下载：
[download.tensorflow.org/models/tflite/motion_detector/data.tar.gz](http://download.tensorflow.org/models/tflite/motion_detector/data.tar.gz)

### Colab 培训

以下[Google Colaboratory](https://colab.research.google.com)
笔记本演示了如何训练模型。这是最简单的获取方式
开始：

<table class =“tfo-notebook-buttons”align =“left”>
  <td>
<a target="_blank" href="https://colab.research.google.com/github/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/motion_detector/train/train_motion_detector_model.ipynb">< img src="https://www.tensorflow.org/images/colab_logo_32px.png" />在 Google Colab 中运行</a>
  </td>
  <td>
<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/motion_detector/train/train_motion_detector_model.ipynb"><img src="https: //www.tensorflow.org/images/GitHub-Mark-32px.png" />在 GitHub 上查看源代码</a>
  </td>
</表>

如果您希望在本地运行脚本，请使用以下说明。

### 运行脚本

使用以下命令安装所需的依赖项：

````外壳
pip install -r 要求.txt
````
训练模型有两种方法：

-随机数据分割，将不同人的数据随机混合在一起
  将它们分为训练集、验证集和测试集
-人员数据拆分，按人员拆分数据

#### 随机数据分割

使用随机分割比个人分割具有更高的训练精度，
但在新数据上的表现较差。

````外壳
$ python data_prepare.py

$ python data_split.py

$ python train.py --model CNN --person false
````

#### 人员数据分割
使用人员数据分割会导致训练精度较低，但效果更好
新数据上的表现。

````外壳
$ python data_prepare.py

$ python data_split_person.py

$ python train.py --model CNN --person true
````

#### 模型类型

在“--model”参数中，您可以提供“CNN”或“LSTM”。 CNN 模型有一个
更小的尺寸和更低的延迟。

## 收集新数据

使用以下方法获取新的训练数据
[SparkFun Edge开发板](https://sparkfun.com/products/15170)，您可以
修改[SparkFun Edge BSP](https://github.com/sparkfun/SparkFun_Edge_BSP)中的示例之一
并使用 Ambiq SDK 进行部署。

### 安装 Ambiq SDK 和 SparkFun Edge BSP

关注 SparkFun
[使用 SparkFun Edge Board 与 Ambiq Apollo3 SDK](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/all)
设置 Ambiq SDK 和 SparkFun Edge BSP 的指南。

####修改示例代码

首先，`cd`进入
`AmbiqSuite-Rel2.2.0/boards/SparkFun_Edge_BSP/examples/example1_edge_test`。

##### 修改 `src/tf_adc/tf_adc.c`

在第62行添加“true”作为函数的第二个参数
`am_hal_adc_samples_read`。

##### 修改 `src/main.c`

在 `int main(void)` 中的 `while(1)` 行之前添加以下行：

``抄送
am_util_stdio_printf("-,-,-\r\n");
````

更改 `while(1){...}` 中的以下行

``抄送
am_util_stdio_printf("Acc [mg] %04.2f x, %04.2f y, %04.2f z, 温度 [摄氏度] %04.2f, MIC0 [计数 /2^14] %d\r\n", Acceleration_mg[0], Acceleration_mg [1]、acceleration_mg[2]、温度_degC、(audioSample));
````

到：

``抄送
am_util_stdio_printf("%04.2f,%04.2f,%04.2f\r\n", Acceleration_mg[0], Acceleration_mg[1], Acceleration_mg[2]);
````

#### 闪存二进制文件

按照中的说明进行操作
[SparkFun 指南](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/all#example-applications)
将二进制文件闪存到设备。

#### 收集加速度计数据

首先，在新的终端窗口中，运行以下命令开始日志记录
输出到“output.txt”：

​````外壳
$脚本输出.txt
````

接下来，在同一窗口中，使用“screen”连接到设备：

````外壳
$ 屏幕 ${DEVICENAME} 115200
````
从加速度计传感器收集的输出信息将显示在
屏幕并保存在`output.txt`中，以每行“x,y,z”的格式。

按“RST”按钮开始捕获新手势，然后按按钮 14
当它结束时。新数据将以“-,-,-”行开始。

要退出“屏幕”，请按 +Ctrl\\+A+，然后立即按 +K+ 键，
然后按+Y+键。然后运行

````外壳
$ 退出
````

停止记录数据。数据将保存在“output.txt”中。为了兼容性
使用培训脚本，更改文件名以包含人员姓名和
手势名称，格式如下：

````
输出_{手势名称}_{人物名称}.txt
````

#### 编辑并运行脚本

编辑以下文件以包含新的手势名称（替换
“翼”、“环”和“斜坡”）

-`data_load.py`
-`data_prepare.py`
-`data_split.py`

编辑以下文件以包含您的新人名（替换“hyw”，
"shiyun", "tangsy", "dengyl", "jiangyh", "xunkai", "lsj", "pengxl", "liucx",
和“zhangxy”）：

-`data_prepare.py`
-`data_split_person.py`

最后，运行前面描述的命令来训练新模型。