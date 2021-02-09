"""
* @File: 02-链式调用.py
* @Author: CSY - 25809 
* @Date: 2020/5/27 - 15:43
* @Project: Python
"""
from pyecharts.charts import Bar

bar = (
    Bar()
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
)
bar.render()
