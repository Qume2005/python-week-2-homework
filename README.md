# python程序设计第二周学生作业



**土木工程-24-李芊墨**

## 使用指南



### 确保pipx&poetry已经安装

1. ***[安装pipx](https://pipx.pypa.io/stable/)***

2. 安装poetry：

   ```bash
   pipx install poetry
   ```


### 克隆本仓库&更改目录

```
git clone https://github.com/Qume2005/python-week-2-homework.git
cd ./python-week-2-homework
```

### 首次需初始化依赖&虚拟环境

```
poetry install
```

### 启动虚拟环境

```
poetry shell
```

### 学生作业

#### 练习 1

##### 运行

```bash
poetry run exercise1
```

##### 描述

以下有多名学生的成绩信息，请计算总分、平均分与及格率，并将它们在交互窗口打印出来。

5171768146 6758

#### 练习 2

##### 运行

```bash
poetry run exercise2
```

##### 描述

已知目前美元、英镑、欧元和澳元兑换人民币的汇率依次为7.00、8.55、7.78、4.24。

假设有10000元人民币，请分别计算并打印兑换后的美元、英镑、欧元和澳元的金额，结果保留整数。

#### 练习 3

##### 运行

```bash
poetry run exercise3
```

##### 描述

请编写一个python程序，其中除import语句外只包含一行代码，运行后可以在 cos（365）和 sin（365）二者中选取数值较大的一个，输出到屏幕上。

#### 练习 4

##### 运行

```bash
poetry run exercise4
```

##### 描述

请编写程序计算一元二次方程的解。方程：x2

-2X-8=0

a=1,b=-2，C=-8，方程的求根公式为：X=（-b士/b2-4ac） -2a

提示：开方运算使用 math 模块的 sqrt 函数。

#### 练习 5

##### 运行

```bash
poetry run exercise5
```

##### 描述

我国个税计算的公式为：应纳税额=（工资-起征点）*税率-速算扣除数

假设工资收入为6000元，起征点为3500元，对应税率10%，速算扣除数105元。请编程计算应纳税额。