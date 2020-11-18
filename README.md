# VGG16-tensorflow
这是一个使用tensorflow1.13搭建的VGG-16。

## 运行程序
```
./run.sh
或
./run_batch_64_one_ce.sh
```

## To-do list
- [x] BatchNorm
- [x] L2 Regularization
- [ ] Pre-train model
- [x] parser 参数解释器
- [x] tensorboard
- [x] tensorflow 计算AUC
- [x] tensorflow 计算ACC
- [ ] 多卡并行训练
- [ ] tf.train.Saver 保存

##  各个文件的任务
- dataProcess.py   
> dataGenerator
- model.py       
> 模型结构定义
- train.py         
> 模型训练
- eval.py          
> 模型测试



## 遇到的问题
- 使用tensorflow计算auc时，需要使用tf.local.initializer()再次初始化。
- 在FC层后加relu会导致损失变为0.69315(-log(0.5))。
- L2正则化的两种添加方式
    - 在声明变量时添加
    - 最后添加





