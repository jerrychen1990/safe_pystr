> 💡 a safe python lib for string formatting/printing, both run well with python2 and python3 💡

## Background
everyone writes python has met error with string encoding/decoding.
just like this:
![encoding error](https://github.com/jerrychen1990/safe_pystr/blob/master/screenshots/encodeError.png?raw=true)
or like this:
![decoding error](https://github.com/jerrychen1990/safe_pystr/blob/master/screenshots/decodeError.png?raw=true)
that's quite annoying!
sometimes, you just want to print some information of your process, then, boom! your process crashed! sorry, your information contains characters that can't be encoded with ASCII or contains bytes that can't be decoded with ASCII!

As a Chinese programmer, I suffers this a lot! I googled and learned the different between unicode and bytes. [learn here](http://pycoders-weekly-chinese.readthedocs.io/en/latest/issue5/unipain.html#python-3).
this blog summarized 5 fact
  - I/O is always bytes
  - Need more than 256 symbol
  - Need both bytes and unicode
  - can't infer encodings
  - declared encoding can be wrong



## Safestr

Based on these facts, we know there is no perfect way to fix encoding/decoding problem. however, UTF8 is a very popular encoding way, we can assume all the types are encoded with UTF8 to simplify this problem.

With this assumption, there is a very very simple way to safely print/format string with python: import `safestr` module

safestr will automatically doing encode/decode with UTF8 when we need a byte/unicode. it provides:
  - a print function `safe_print`
  - a formatting function `safe_format`
  - can satisfy python2 or python3 automatically

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



