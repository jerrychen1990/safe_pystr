> 💡 安全的python print/format字符串的包，彻底避免encode/decode错误，兼容python3/python2💡

[English doc](https://raw.githubusercontent.com/jerrychen1990/safe_pystr/master/README.md)
## Background
每个用python的人一定都碰到过关于编码／解码的错误。

编码错误：
![encoding error](https://github.com/jerrychen1990/safe_pystr/blob/master/screenshots/encodeError.png?raw=true)
解码错误：
![decoding error](https://github.com/jerrychen1990/safe_pystr/blob/master/screenshots/decodeError.png?raw=true)
太令人厌烦了！😡有时候，仅仅是在程序里添加了个print来输出进程的信息，或者只是打印一条日志，一运行，惊喜的发现：你的程序已经挂了😂！很遗憾，你的信息里包含了一些特殊字符，不能被ASCII编码，或者有一些二进制编码不能被ASCII解码。。。 都什么年代了，还在用ASCII的编码方式！

作为一个天朝码农，工作中接触到大量中文字符串是不可避免的，我也深受python的编码／解码错误之害。我也google了很多关于unicode、bytes以及编码字符集的知识：[unicode 之痛](http://pycoders-weekly-chinese.readthedocs.io/en/latest/issue5/unipain.html#python-3)这篇讲的就很不错。稳重提到一个unicode汉堡的概念——程序处理的时候用unicode，做IO的时候再根据相应的字符集转化成bytes

无奈理论知识是了解了，但是时常还是会一步小心写错。于是乎，想要自己造一个轮子，在假设输入输出的byte都是用UTF8编码的情况下（如果不是，可以约束上下游使用UTF8）自动做需要的encode/decode


## Safestr
基于输入输出编码都用utf8的前提下，我开发了一个python模块`safestr`，它提供两个函数：
  - `safe_print` 用来向标准输出打印python变量
  - `safe_format` 用来格式化字符串（毕竟大量的python2 的解码错误都是由于字符串格式化的时候的隐式转化造成的）
  
值得一提的是python的编码字符集问题之所以恶心，很大部分是由于python3和python2对于str的定义不同造成的， 这经常让人蒙圈了。`safestr`会自动检测当前python解释器的版本，运行相应的函数，使用是完全不用关心将来代码会用python2执行还是python3执行

## install
### install with pip
```
pip install safestr
```
### install with source code
```
git clone https://github.com/jerrychen1990/safe_pystr.git
cd safe_pystr/
python setup.py install
```

## test
```
pytest test.py
```

## example
### python2 example
![python2 example](https://github.com/jerrychen1990/safe_pystr/blob/master/screenshots/example-py2.png?raw=true)
### python3 example
![python3 example](https://github.com/jerrychen1990/safe_pystr/blob/master/screenshots/example-py3.png?raw=true)
