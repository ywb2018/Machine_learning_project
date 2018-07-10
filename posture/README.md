坐姿检测项目
===
### 数据来源：
   实验室的嵌入式项目，在坐垫上布置10个压力传感器，然后将传感器的数据保存下来，进行坐姿检测
   实验人数为3人，分别是
   名字：
      `name_dict= {'cwb':1,
                  'tsy':2,
                  'wlj':3}`
                  
   以及每个数据的文件名对应标签：

   `lab_dict ={'tuobei':1,
              'youbian':2,
               youpian':2,
              'zuobian':3,
              'zuopian':3,
              'zuozhi' :4}`
              
  下面是文件的截图：
  ![image](https://user-images.githubusercontent.com/40688203/42500236-4296c6c0-8463-11e8-94f7-98c2abe93853.png)
  
  每个文件里面的数据的形式，还有缺失值：
  ![image](https://user-images.githubusercontent.com/40688203/42500402-c487dc32-8463-11e8-9838-1db68a1b27e7.png)
  
  多测试数据都是存在不同的文件里面的，要进行提取，根据文件名重新构造数据，最后构造的数据是这样：
  ![image](https://user-images.githubusercontent.com/40688203/42500494-0d58410e-8464-11e8-9c0a-f6f1daaf4c44.png)
  
  最后使用svm进行分类，发现数据还是比较优质的，可分性很好，虽然没有经过复杂的模型选择和调参让我有点`小失落`，不过最后的分类效果还是非常好的，
  稍微调参之后，准确率可以到100%。

  
  





