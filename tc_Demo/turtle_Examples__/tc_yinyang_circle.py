#!/usr/bin/python
"""       turtle-example-suite:

         tdemo_yinyang_circle.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the circle
command.

"""

from turtle_tc import *

def 陰(半徑, 顏色1, 顏色2):
    筆寬(3)
    顏色(顏色1)
    開始填()
    畫圓(半徑/2., 180)
    畫圓(半徑, 180)
    左轉(180)
    畫圓(-半徑/2., 180)
    結束填()
    顏色(顏色2)
    左轉(90)
    提筆()
    前進(半徑*0.375)
    右轉(90)
    下筆()
    開始填()
    畫圓(半徑*0.125)
    結束填()
    左轉(90)
    提筆()
    後退(半徑*0.375)
    下筆()
    左轉(90)

def 主函數():
    重設()
    陰(200, 紅, 綠)
    陰(200, 綠, 紅)
    藏龜()
    return "Done!"

if __name__ == '__main__':
    主函數()
    主迴圈()
