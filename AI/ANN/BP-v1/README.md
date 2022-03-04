# MNIST Tensorflow1

使用 Tensorflow 1 的 MNIST 手写数字识别

## 介绍

本项目使用 tensorflow 1 编写的 mnist 手写数字识别项目，可以做到模型训练、保存、加载、推理等

## 文件结构

```paintext
logs                             # tensorboard 用的 log，训练时自动写入
mnist
  |- t10k-images-idx3-ubyte.gz   # mnist 测试图片数据集 10k条数据
  |- t10k-labels-idx1-ubyte.gz   # mnist 测试标签数据集 10k条数据
  |- train-images-idx3-ubyte.gz  # mnist 训练图片数据集 60k条数据
  |- train-labels-idx1-ubyte.gz  # mnist 训练标签数据集 60k条数据
save                 # 保存的网络模型
  |- checkpoint      
  |- model.ckpt.data-00000-of-00001 
  |- model.ckpt.index
  |- model.ckpt.meta
dataset.py           # 用于加载mnist数据集的类文件
infer.py             # 推理测试数据预览(matplotlib显示图片)
network.py           # 网络模型构造类
readme.md            # 本说明文件
requirements.txt     # 依赖
starttensorboard.ps1 # 启动tensorboard(powershell脚本)
train.py             # 训练模型
```

## 网络结构

### 三层全连接层

* 第一层 32 神经元，采用 relu 激活函数
* 第二层 16 神经元，同样采用 relu
* 第三层也是输出层，10 个神经元，激活函数采用 softmax

网络输入的图片格式为 `[? * 784]`，默认一批大小128， 输入的标签格式为 [?, 10]，内容使用 one_hot, 9个0，1个1 构成的数组，1所在索引表示图片中数字

### 损失函数为交叉熵损失

### 优化器采用 Adam

## 运行平台

在 Windows 10 pro AMD64 平台开发和测试，python版本为 3.6.8. tensorflow 和 matplotlib 版本参考 `requirements.txt`

## 注意

训练时可以执行 `starttensorboard` 脚本启动 `tensorboard`

tensorflow 1.15.x 要求 python 3.7 或 3.6 ，python 3.8 及以上请使用tensorflow 2
