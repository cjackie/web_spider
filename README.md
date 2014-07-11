web spider
==========
a web crawler.<br>
run it with python 2.7:
```shell
python spider.py [url]
```
-----------------------

## algorithm:
given a url, open it and get all the href links. then do the some for new urls. world wide web is like a giant graph. I tried to traverse it using breadth first approach.

-----------------------
## current state:
it works a while then stops. I suspect it is because it quickly drains out memories.
