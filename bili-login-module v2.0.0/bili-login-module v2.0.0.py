# -*- coding:utf-8 -*-
from tkinter import *
from tkinter.ttk import *
import ctypes
import os
import requests
import io
from PIL import Image, ImageTk # 调用PIL模块以用来加载png或者jpg等图片
from MBPython import miniblink # 使用：https://github.com/weolar/miniblink49/releases/tag/2021.5.26
from threading import Thread
import time
import base64

TEMP = os.getenv ("TEMP") # 获取环境变量TEMP的值
true = True
false = False
null = None

# 创建窗口一个叫“main”的窗口
main = Tk()
main.title('哔哩哔哩登录模块')# 设定窗口标题
main.geometry('340x180')  # 设定窗口大小
main.resizable(False,False)#设定不允许改变窗口大小
icon = base64.b64decode("AAABAAEAMDAAAAEAIACoJQAAFgAAACgAAAAwAAAAYAAAAAEAIAAAAAAAgCUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACOZOYhjFzxWX5I8Jl7Q/TCeT/16nY79v9xM/f+bzD3/24u9v5uLvf/bi73/24u9v5uLvf/bi73/24u9v5uLvf/bi73/24u9v5uLvf/bi73/24u9v5uLvf/bi73/24u9v5uLvf/bi73/24u9/9uLvb+by/3/3Ez9/92Ovb+eD71531F9MJ+SPCZjV3xWI1h6CEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkGbnF4VS8ZhyNPn5cC/8/3Av/P5xMP3/cTD9/3Ew/f9wL/z+cTD9/3Av/P5xMP3/cTD9/3Av/P5xMP3/cTD9/3Av/P5xMP3/cTD9/3Av/P5xMP3/cTD9/3Av/P5xMP3/cTD9/3Av/P5xMP3/cTD9/3Ew/f9wL/z+cTD9/3Ew/f9wL/z+cTD9/3Ew/f9wL/z+cC/8/3I0+fqDUPGaj2TqFwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACJW+w7djv25nAv/P5wL/z+cC/8/nAv/P5wL/z+cC/8/nAv/P5wL/z+cC/8/nAv/P5wL/z+cC/8/nAv/P5wL/z+cC/8/nAv/P5wL/z+cC/8/nAv/P5wL/z+cC/8/nAv/P5wL/z+cC/8/nAv/P5wL/z+cC/8/nAv/P5wL/z+cC/8/nAv/P5wL/z+cC/8/nAv/P5wL/z+cC/8/nAv/P5wL/z+djr254la7T0AAAAAAAAAAAAAAAAAAAAAAAAAAIhX7jxzNfn0cTD9/3Ew/f5xMP3/cTD9/3Ew/f5xMP3/cTD9/3Ew/f9xMP3+cTD9/3Ew/f5xMP3/cTD9/3Ew/f5xMP3/cTD9/3Ew/f5xMP3/cTD9/3Ew/f5xMP3/cTD9/3Ew/f5xMP3/cTD9/3Ew/f5xMP3/cTD9/3Ew/f9xMP3+cTD9/3Ew/f9xMP3+cTD9/3Ew/f9xMP3+cTD9/3Ew/f9xMP3+cTD9/3Q2+fWJWO8+AAAAAAAAAAAAAAAAkGjkFHg99uZyMv7/cjL+/3Iy/f5yMv7/cjL+/3Iy/f5yMv7/cjL+/3Iy/v9yMv3+cjL+/3Iy/f5yMv7/cjL+/3Iy/f5yMv7/cjL+/3Iy/f5yMv7/cjL+/3Iy/f5yMv7/cjL+/3Iy/f5yMv7/cjL+/3Iy/f5yMv7/cjL+/3Iy/v9yMv3+cjL+/3Iy/v9yMv3+cjL+/3Iy/v9yMv3+cjL+/3Iy/v9yMv3+cjL+/3Iy/v93Pfbnk2rrFgAAAAAAAAAAgk7zm3Iz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+cjP9/nIz/f5yM/3+g0/znQAAAACWbuogdTj6+nM0/f5zNP7/czT+/3M0/f5zNP3/czT+/3M0/f5zNP7/czT9/3M0/f9zNP3+czT9/3M0/f5zNP3/czT9/3M0/f5zNP3/czT9/3M1/f5zNP3/czT9/3M0/f5zNP3/czT9/3M0/f5zNf3/czT9/3M0/f5zNP3/czT9/3M0/f9zNP3+czT9/3M0/f9zNP3+czT9/3M0/v9zNP3+czT+/3M0/v9zNP3+czT+/3M0/v9zNP3+dTf6+phv7iKKW/B3dTb+/3U2/f52N/7/djf+/3U2/f52Nv7/djf+/3U2/f52N/3/dzn8/3o9/P99Qf3+f0X8/4FI/P6ESvz/hkz9/4ZO/P6HUPz/h1D7/4hR+/6IUvz/iVL8/4lT/P6JU/z/iVP8/4lS/P6IUfz/iFH7/4dQ+/6GTvz/hUz8/4NK/P+BR/z+f0T9/31B/f96Pfz+dzj8/3Y2/f91Nv3+dTb9/3U2/f91Nv3+djf+/3Y3/v91Nv3+dTb9/4ZT8XZ+RveidTb9/nU2/f51Nv3+dTb9/nU2/f51Nv3+dTb9/nk9+/6JUfz+j1r+/pBa/v6QWv7+kFr+/pBa/f6QWv3+kFv9/pBa/f6QWv7+kFr+/pBa/v6QWv3+kFv9/pBb/f6QW/3+kFv9/pBa/v6QWv7+kFr+/pBa/v6QW/3+kFv+/pBb/f6QWv3+kFr+/pBa/f6QWv3+j1r9/ohR/P55PPv+dTX9/nU2/f51Nv3+dTb9/nU2/f51Nv3+dTb9/oBI+JuETvjCdjf+/3c4/v53OP7/djf9/3c4/v53OP3/fkP8/49a/v6RW/7/kVv//5Fb/v+QW/7+kVv//5Bb/v6QXP7/kFz+/5Bc/f6QXPz/kFz8/5Bc/f6QXPz/kFz8/5Bc/P6RXPz/kVz8/5Bc/f6QXP3/kFv9/5Bb/f6QW/7/kFz+/5Bc/v+QW/7+kVv//5Fb/v+QW/7+kVv//5Bb/v+PWv7+fkP8/3c4/v92N/7+djj9/3c4/v92N/3+djf+/4NN98Z+RvbleDv+/3g7/f55PP7/eDv+/3g7/f59Qf3/kFv9/5Bb/f6QW///kFv+/5Bb//+QW/7+kVz//5Fc/v6QXP3/kFr9/49a/P6PW/v/j1r8/45Z/f6OWf3/j1j+/45Z/f6OWf3/jln9/45Z/f6PWf3/j1v7/49a+/6PWvz/kFv9/5Bb/v+RXP7+kVz//5Bb//+QW/7+kFv//5Bb//+QXP3+kFv9/31B+/94Of7+eDv9/3k8/v94O/3+eDv+/31G9ex9Rff/eTz+/3g7/f55PP7/eTz+/3g6/f6KU/3/kl3+/5Jd/f6RXf3/jVj8/4NK/f9/RP3+fUL8/3w//v56Pv3/eT38/3k8/f55PP3/eTz9/3k7/f55O/7/eTv+/3k7/v55O/7/eTv+/3k7/f55PP7/eTz9/3k8/f55PPz/eT38/3s+/f98QP3+fUL8/39E/P+ES/z+jln9/5Fd/f+SXf7+kl3+/4lS/f94Ov7+eTv9/3k8/v94O/3+eTz+/31E9/56P/n+eTz+/nk8/v55PP7+ejz+/nxA/P6SX/3+k1/9/pJe/f6OWf3+ez79/no8/f56PP3+eTz+/no8/v56PP7+eTz+/nk8/v55PP7+eTz+/nk8/v55PP7+eTz+/nk8/v55PP7+eTz+/nk8/v55PP7+eTz+/nk8/v55PP7+eTz+/no8/v56PP7+ejz+/no8/f55O/7+ez78/o9a/f6TX/3+k1/9/pJd/f58P/z+eTz+/nk8/v55PP7+eTz+/nk++P56P/j/ez/+/3s//v57P/7/ez/+/4JI/f6TYfz/lGH+/5Ng/P6GTvz/ez7+/3s//v97P/7+ez///3s//v57P/7/ez/+/3s//v57P/7/ez/+/3s//v57P/7/ez/+/3s//v57P/7/ez/+/3s+/v57Pv7/ez/+/3s+/v57P/7/ez/+/3s//v97P/7+ez/+/3s//v97P/7+ez7+/4dP/f+UYf3+lGD+/5Ng/f+BR/3+ez/+/3s//v97P/7+ez/+/3k/+f55P/n+ez/+/ns//v57P/7+ez/9/oRM/P6TYPv+k2H8/pNg/P6ES/z+ez79/ns//v57P/7+ez/+/ns//v57P/7+ez/+/ns//v57P/7+ez/+/ns//v57P/7+ez/+/ns//v57P/7+ez/+/no++/56Pvv+ej/8/ns//f57QPz+ez/+/ns//v57P/7+ez/+/ns//v57P/7+ez/+/oRL/P6UYf3+lGL9/pNh/f6ETP3+ez/+/ns//v57P/7+ez/+/nk/+v56P/n/fUD//31A/v59QP//fED9/5lr+P7o3/r/6eH4/+fd+v7Uwff/sI74/4lU+P98QP7+fEH9/3xB/f58Qf3/fEH9/3xA/P59Qf3/fUH+/31B/v58Qf7/fUD+/3xB/f59Qf3/ez/9/9vM+P7l2/f/49j4/9nH9/66m/j/kF74/31B/f98Qf3+fUH+/3xB/v98QP3+fED9/4JI/P+UYv3+lGL9/5Ri/P+GT/z+fUH8/31B/f99Qf7+fUD//3o/+v57Qvn/fkP//31D/v5+Q///fUL+/6qC/P79/f3//v7+//39/f79/fz//fz6//n2/P/Rvfj+jFj4/35D/f59Q/r/1sT2/864+v59Q/n/fkT6/35D+/6edPn/7OX4/55x/P59Qvz/f0b5//b0/P7+/v7//fz8//38+v79/Pz/+/v7/+HU+v+Za/f+fUP7/31C/f+5m/X+4NL6/5Rj+v+UZPn+lGT5/5tt+P/r4/n+u573/31B/f99RP3+fkP//3tB+v57Qvj+fkT+/n1E/v59RP7+fUP+/rOP+/79/f3+/f39/vLt+/6hd/b+6eD3/v39/P79/fz+9fH6/qJ59v6DS/v++ff7/uXZ+/6JVPn+7ub5/reZ9P65mff+/f38/qN5/P5+Q/3+j172/vr5/P79/f3+/Pv6/p127v7Zyvf+/fz7/v37+/76+fr+uJn2/n5D/P7Wxff+/fz8/pJh9/7ay/T+2Mf4/qJ49/79/Pz+xKv3/n1D/v5+Q/7+fkT+/ntC+f58Q/j/f0X+/39F/v5/Rf7/fkT+/7qc+f79/f3//v7+/+HV+P6AR/z/hlD5/8659v/9/fv+/f37/+/o+f6bbvj//f37/93N+/6UZfj//f38/7uc+f7Fq/j//f39/62G/P6OW/v/qID7//39/f7+/v7//Pv8/4ZQ+v6ARvz/t5n0//z7/P/9/f3+/Pv8/5Zo+P/s5fj++vj7/4dQ+v/v6fn+2Mj6/6mC+//9/f3+xaz4/35E/v9/Rf7+f0X+/31D+v5+Rfn/gUf+/4FH/v6BR/7/gEf9/8Km+v79/f3//f39/9fF+/6HUfn/sI32/+Xb+P/9/Pv+/f38//Ls+/6tjPD//f39/8y2+P6lfPr//f38/6V9+f7Eqvv//f3+/7WS/P6XZ/3/p4H0//39/f7+/v7/9/P7/4pW9/6je/f/2cr3//z7+//9/f3+/f38/6WA8//8+vv+6+X3/4VR9P/69vz+z7v3/7KP+v/9/fz+xaz3/4BH/f+ARv7+gUf+/35G+f5/Rvr+gkj+/oJI/v6CSP7+gUj9/sy39f79/f3+/f39/vby/P749fv+/f37/v39+/79/Pv+6uL3/p509/7Ir/f+/f39/rmc9P65mfn+/fz8/phr9v7Oufj+/f39/rSR/f6QXfz+sY/1/v39/f79/f3++/n8/vXw+v79/fz+/f39/v39/P708Pj+r470/qZ/9/79/fz+3M75/pFh9/79/Pz+xKr5/ryf9/79/f3+xq34/oFH/f6BR/7+gUj+/n9G+f5/R/n/gkn9/4JJ/P6CSvz/gkn8/9/S9/79/f3/+/r9//z6/P759/z/7uf4/9G99/+kfPb+hE75/4JJ+v7j1vr//f38/6yH+f7Fq/v//Pr9/4tX+f7bzvX//f39/6d//P6DS/r/w6n5//39/f77+vz/+/n7//r4/P7y7fn/2sr4/6+M9f+JVPj+gkj9/8Km+f/9/fz+zLf1/6R7+P/9/f3+u5v9/8eu+P/9/fz+xq34/4JJ/P+CSfz+gkn8/39H+P6BSfn/hEv9/4RL/f6ES/3/g0v6//Dp+/79/fv/uJb7/6N1/f6LVvv/hEz6/4NL/f+FTfz+hk78/4pX+P769/v//fz7/5lt9P7ZyPf/+ff6/4VN+/7n3fj//f38/6d/+/6ES/z/1sb1//39/P7Bpfj/jln8/4xX/P6ETfr/hEz8/4RL/f+ES/3+hk38/9vL+f/9/Pz+up33/7eW+P/9/f3+uJb7/9C6+//9/fz+xq/3/4NL/P+ES/z+hEz9/4FK+P6CS/j+hU39/oVN/f6FTf3+iVb3/vr4+/79/P3+qoD6/pxq/v6FTfz+hU38/odQ/f6aaf7+m2v6/p1w+v7Rvfn+18j1/otW+v7o3vv+8u76/oRN+P7Gq/v+zrj8/ppr+/6FTfv+6d/8/v39+v6tiPr+hEz8/oVN/f6FTf3+hU78/o1Y/P6WY/3+m2v8/sas+P7Wxfb+onn2/sWs+f79/f3+tZD6/r+g+/7Vwvr+rYn3/oVN/P6FTf3+hU39/oJL+f6DTPj/hk/+/4ZP/f6GT/7/m237//39+/76+fz/oXH8/51t/f6HUPz/hk79/4xW/f+ebv3+nW38/66G+/7Dp/f/u5v4/5Vl9/718vv/7ef5/4ZR9f67nff/sY/3/5Jh+P6GTvz/9fH8//38/f6jevf/hk/8/4xW/P6TYf3/mmr9/5xt/v+ebf7+oHH8/8yy+/+ti/L+jlv5/9fF+f/9/f3+rYX8/7yd+v+7nPf+oHb2/4ZO/P+GTf3+hk3+/4NL+f6ETvj/h1D9/4ZQ/f6GUP3/q4b5//39+/729Pv/nm78/51u/f6IUfv/h1D9/4lR/f+UY/v+nG38/8iv9/7g0Pr/6d/6/6iA+v78/Pz/7eX7/5Vm9f7x6vr/38/6/59z+P6LVvr/+fj8//39/f6hdvf/m2v8/55t/f6dbv3/nG79/51u/f+dbv3+rYb5/+HT+P/r4/j+mGn6/9/R+//8+/z+pnv6/93O+//f0vX+u6Hx/4hQ/P+HT/3+hlD9/4RN+f6HUPj+ilL9/opS/f6JUv3+t5j4/v38/P7y7Pn+nm/8/p1v/f6KU/z+iVL9/olR/f6IUv3+i1X7/trJ+P7TwfT+49f6/q+J+f79/fz+5Nj2/qd++v7x6/r+4tT8/qF29/6cb/j+/fz8/v38/f6idfv+nXD9/p1v/f6db/3+nW7+/plp/P6SX/z+uZr1/s698P707vr+j1z2/uri9/769vz+oHT4/uTX+/7f0vT+vaLy/olS/P6KUv3+iVL9/oZQ+f6IUfn/i1P+/4pS/f6KU/3/x7D3//39/f7u5vn/n3L8/59y/f6NV/z/ilP+/4pT/v+KUv3+iVL7/6R6+v6gdPf/qoL6/62I+f79/fz/2Mf2/5Vj+/6shvn/qH77/5Fe+f6vivn//f39//z7/f6VY/z/nG79/5lp/P6TYPz/jlj9/4pT/P+KU/r+mmv6/59z9/+xi/v+jVj7//fz+//z7fz+n3L6/7iX+v+tiPb+m275/4pS/f+KU/3+i1P+/4dQ+f6HUvj/ilP+/4pT/f6KU/z/3c/4//39/f7q4Pv/oHP8/6Bz/f6PWvz/ilP9/4pU/f+KVP7+ilT8/4pT/f6KU/3/ilT8/7aU+f79/Pz/x636/4pU/P6KVPv/ilT8/4pU/f7Grff//f39//z7/f6OWvz/ilT8/4pU/f6KVP3/ilT9/4pU/f+KVP3+ilT8/4pU/P+KVPz+mGr2//38/f/p4fj+n3L8/6Bz/f+VY/3+ilP9/4pU/f+KVP3+ilT+/4dR+f6JVPj+jFX+/otV/P6MVvv+8+/7/v39/f7p3vz+oHT8/qBz/f6SX/3+jFX+/oxV/v6MVf7+jFX+/oxV/v6MVf7+jFX+/sat+P79/fz+up32/oxW/v6MVf7+jFX+/oxV/v7ay/b+/f39/vz7/f6PXPv+jFX+/oxV/v6MVf7+jFX+/oxV/v6MVf7+jFX+/oxV/v6MVf7+pn37/v39/P7g1Pf+oHP9/qF0/f6VY/3+jFX+/oxV/v6MVf7+jFX+/olT+v6LVvn/jlj//41X/f6abvX//Pv9//7+/f7p3/v/oXX8/6F0/f6VY/3/jlj+/45Y//+OWP7+jlj//45Y/v6OWP//jlj+/8et+f728vv/sI30/45Y/v6OWP//jlj//45Y/f7x7Pn//f38//z7/f6RXvv/jlf+/45Y/v6OWP//jlj//45Y//+OWP7+jlj//45Y//+OV/7+ron3//Pu+v/Xxfj+oXT9/6F1/f+UYv3+jlf//45Y//+OWP7+jlj//4tW+v6LVvj/j1n+/45Z/P6shPr/+/r8//39/f7s4/n/onb8/6J1/f6YaPz/jlj+/49Z/v+PWf7+j1n+/49Y/v6PWf7/j1n9/45Y/P6OWvr/j1v7/49Y/v6PWf7/j1n+/49a/P718Pr//fz9//z7+/6SX/z/j1j+/49Y/v6PWf7/j1n+/49Z/v+PWP7+j1n+/49Z/v+PWP7+jlj8/5ho+v+jevn+onf7/6J2/f+TYP3+jlj+/49Z/v+PWP7+j1n+/4xX+f6MV/j/kFn//49a/f6PWvv/nnH5/8Gk+P7dzfj/onf8/6N4/f6gdP3/kl/8/5Bb/v+QW/7+kFv+/5Bb/v6QW/7/kFv+/5Bb/f6QWv3/kFv9/5Bb/v6QW/7/kFv+/5Bb/v6UYfr/tpX4/9fF+P6WZfv/kFv+/5Bb/v6QW/7/kFv+/5Bb/v+QW/7+kFv+/5Ba//+QW/7+kl79/6B1/P+jd/3+o3f9/6J2/f+RXP3+kFr+/5BZ/v+QWf7+kFn//41Y+v6NWfj+kFv+/pBb/v6QW/7+kFz+/pBc/v6cbvz+pHn+/qN4/v6kef7+oXX9/ppr/P6Zaf3+l2b9/pZk/f6UYv3+k2D9/pJf/f6SX/3+kl78/pFd/P6RXfz+kV39/pFd/f6RXf3+kV39/pBc/P6RXfz+kl78/pJf/f6SX/3+k2D9/pRi/P6VY/z+l2b9/plo/f6aa/z+oXb9/qN4/v6keP7+pHn+/pxu/P6QW/7+kFz+/pBb/v6QW/7+kFv+/o1Z+v6PXPn/kl3+/5Jd/v6SXf7/kl3+/5Fd/f6UYv3/o3f+/6R4/v6keP7/pHn+/6R5/v+keP7+o3n9/6N5/v6kev3/pHr+/6R6/f6kef3/pHn9/6N4/v6jeP3/o3j9/6J4/f6jeP3/o3j9/6N4/f6jeP3/o3n9/6R6/f6kev7/pHr9/6R6/v+kef7+pHn+/6R5/v+kef7+pHj+/6N4/v+kef7+onf+/5Rh/P+RXf3+kl3+/5Jd/v+SXf7+kl3+/49c+P6RYPf/k1/9/5Nf/f6TX/3/k1/9/5Nf/f6TX/3/l2f8/6N5/P6kfP3/pHz9/6V8/v+le/7+pXz+/6V8/v6lfP7/pXz+/6V8/v6lfP7/pXz+/6V8/v6lfP7/pXz+/6V8/v6lfP7/pXz+/6V8/v6lfP7/pXz+/6V8/v6lfP7/pXz+/6V8/v+lfP7+pXz+/6V8/v+lfP7+pHz9/6V8/v+jef3+l2f8/5Nf/f+TX/3+k1/9/5Nf/f+TX/3+k1/9/5Ff+P6VZff+k2D9/pNg/f6TYP3+k2D9/pNg/f6TYP3+k1/9/pZk/f6fcv3+pXv9/qZ9/f6mfv3+pn79/qZ+/f6mfv3+pn39/qV9/f6lff3+pn79/qZ9/f6mff3+pn39/qV9/f6mfv3+pn79/qZ+/f6lff3+pX39/qZ+/f6mff3+pX39/qZ+/f6mfv3+pn79/qZ+/f6mff3+pXz9/p9z/P6VZPz+k2D9/pNg/f6TX/3+k1/9/pNf/f6TX/3+k1/9/pRk9/6XafXqlGH+/5Rh/f6UYf7/lGH+/5Rh/f6UYf3/lGH9/5Rh/f6UYf3/lGL9/5dl/f+Zafz+mmv8/5xu/P6dcPz/o3n8/6Z+/f6mfv3/pn39/6Z9/f6hdv3/oXb9/6F2/f6idv3/onf9/6J3/P6mfv3/pn7+/6Z+/f6nfv3/o3j8/55x/f+dcP3+m238/5lq/P+XZv3+lGL8/5Rh/f+UYf3+lGH9/5Rh/v+UYf3+lGH+/5Rh/v+UYf3+lGH+/5Zo9u2dcvfElWP9/5Vj/f6VY/3/lWP9/5Vj/f6VY/3/lWP9/5Vj/f6VY/3/lWP9/5Vj/f+VY/3+lWT8/5Vk/f6Yafz/p379/6h//f6of/7/p3/9/6B0/P6VY/3/lWT+/5Vj/f6VY/7/lWP+/5Vk/P6id/z/p3/+/6h//f6of/3/p379/5dn/P+VZPz+lWT8/5Vj/f+VZP3+lWT9/5Vk/f+VZP3+lWT9/5Vk/f+VZP3+lWT9/5Vk/f+VZP3+lWT9/5pv9sWZbPeilWT9/pVk/f6VZP3+lWT9/pVk/f6VZP3+lWT9/pVk/f6VZP3+lWT9/pVk/f6VZP3+lWT9/pZm/P6le/3+qID9/qh//f6of/3+pn39/pZm/f6VZP3+lWT9/pVk/f6VZP3+lWT9/pVk/f6XZ/z+p379/qh//f6of/3+qH/9/qR5/f6WZfz+lWT9/pVk/f6VZP3+lWT9/pVk/f6VZP3+lWT9/pVk/f6VZP3+lWT9/pVk/f6VZP3+lWT9/ptv95yedvB7lmX+/5Zl/v6WZf7/lmX+/5Zl/v6WZf7/lmX+/5Zl/v6WZf7/lmX+/5Zl/v+WZf7+lmX+/5tt/P6pgP7/qoH+/6qB/f6pgP3/nG77/5Zl/v6WZf7/lmX+/5Zl/v6WZf7/lmX+/5Zl/v6WZP7/nXD8/6mB/P6pgf3/qoH+/6mB/f+aa/3+lmX+/5Zl/v+WZf7+lmX+/5Zl/v+WZf7+lmX+/5Zl/v+WZf7+lmX+/5Zl/v+WZf7+lmX+/5lv8XeqiO0lmGj7+pdn/v6YZ///mGf//5dn/v6YZ///mGf//5dn/v6YZ///mGf//5hn//+XZ/7+l2b+/5pr/f6qgP7/q4H+/6qB/f6id/3/l2b+/5hn/v6XZv7/mGf//5dn/v6YZ///mGf//5dm/v6YZ///l2f+/6R5/f6qgf3/q4H9/6mA/f+Zav3+mGb//5hn//+XZ/7+mGf//5hn//+XZ/7+mGf//5hn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")
with open(TEMP + "\\icon.ico", "wb") as f:
    f.write(icon)
main.iconbitmap(TEMP + "\\icon.ico") # 更改窗口左上角的小图标

def 登录():
    def warn_text():
        warn_text = Label(登录模块, text="未成功登录!", font=('微软雅黑',10), foreground="red")
        warn_text.place(x=0, y=435,anchor="sw")
        time.sleep(2)
        warn_text.destroy()

    def check():
        if mb.wkeGetURL(webview).decode('utf-8') == "https://passport.bilibili.com/ajax/miniLogin/redirect":
            analyse(mb.wkeGetCookieW(webview))
        else:
            t = Thread(target=warn_text,daemon=None)
            t.start()

    def analyse(cookies):
        temp_list = cookies.split('; ') # 以'; '切割
        #创建空字典
        cookies_字典 = {}
        #遍历列表
        for data in temp_list:
            key = data.split('=', 1)[0] # 以'='切割，1为切割1次
            value = data.split('=', 1)[1]
            cookies_字典[key] = value

        SESSDATA=cookies_字典["SESSDATA"]
        bili_jct=cookies_字典["bili_jct"]
        已登录(SESSDATA,bili_jct)

    global 登录模块
    登录模块 = Toplevel()
    登录模块.geometry('420x435')#设置窗口尺寸
    登录模块.resizable(False,False)#设定不允许改变窗口大小
    登录模块.title('哔哩哔哩登录控件')# 设定窗口标题
    登录模块.wm_transient(main) # 将“登录模块”窗口设置为其父级（“main”窗口）的transient，使窗口管理器只显示main的任务栏图标
    登录模块.grab_set() # 设置用户只能与“登录模块“窗口进行交互
    button = Button(登录模块, text ="成功登录后点我", command = check)
    button.place(x=420,y=435,anchor="se")


    登录模块.update()#更新窗口状态和信息
    mbpython=miniblink.Miniblink
    mb=mbpython.init(os.path.abspath('.') + '\\miniblink_x64.dll')#操作核心
    wke=mbpython(mb)#得到wke控制权
    window=wke.window#miniblink的界面容器

    webview=window.wkeCreateWebWindow(_type=2,hwnd=登录模块.winfo_id(),x=0,y=0,width=420,height=405)#核心组件，大小与窗口尺寸一样
    mb.wkeLoadURLW(webview,'https://passport.bilibili.com/ajax/miniLogin/minilogin')#载入网页
    window.wkeShowWindow(webview)#显示组件

    登录模块.mainloop()

def 已登录(SESSDATA,bili_jct):
    def 退出登录():
        global 头像_标签,用户昵称_标签,登录按钮_控件,SESSDATA_标签,SESSDATA_Entry标签,bili_jct_标签,bili_jct_Entry标签,右键菜单_标签
        头像_标签.destroy()
        用户昵称_标签.destroy()
        UID标识_标签.destroy()
        UID_标签.destroy()
        退出登录按钮_控件.destroy()
        SESSDATA_标签.destroy()
        bili_jct_标签.destroy()
        SESSDATA_Entry标签.destroy()
        bili_jct_Entry标签.destroy()
        右键菜单_标签.destroy()
        
        未登录()

    global 头像_标签,用户昵称_标签,登录按钮_控件,SESSDATA_Entry标签,bili_jct_Entry标签
    登录模块.destroy()
    headers = {'Cookie':'SESSDATA=' + SESSDATA + '; bili_jct=' + bili_jct + '','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
    用户信息 = eval(requests.get('https://api.bilibili.com/x/web-interface/nav',headers=headers).text)
    用户昵称 = 用户信息.get("data").get("uname")
    头像 = requests.get(str(用户信息.get("data").get("face")) + "@60w_60h").content
    uid = 用户信息.get("data").get("mid")

    头像_标签.destroy()
    用户昵称_标签.destroy()
    登录按钮_控件.destroy()

    头像 = ImageTk.PhotoImage(file=io.BufferedReader(io.BytesIO(头像)))#file：转换为内存缓冲类型, # 用PIL模块的PhotoImage打开
    头像_标签 = Label(main, image=头像)#把图片整合到标签类中
    头像_标签.pack(anchor="nw")
    用户昵称_标签 = Label(main, text=用户昵称, font=('微软雅黑',12,'bold'))
    用户昵称_标签.place(x=70, y=5)
    UID标识_标签 = Label(main, text="UID", font=('微软雅黑',12,'bold'), foreground="blue")
    UID标识_标签.place(x=70, y=35)
    UID_标签 = Label(main, text=uid, font=('微软雅黑',12), foreground="gray")
    UID_标签.place(x=105, y=35)
    退出登录按钮_控件 = Button(main, text="退出登录", command = 退出登录, width = 8)
    退出登录按钮_控件.place(x=225, y=20)
    SESSDATA_Entry标签.config(state="normal") # 设置为可编辑
    SESSDATA_Entry标签.delete(0,END) # 删除所有值
    SESSDATA_Entry标签.insert(0,SESSDATA)
    SESSDATA_Entry标签.config(state="readonly") # 设置为可复制但不能编辑
    bili_jct_Entry标签.config(state="normal") # 设置为可复制但不能编辑
    bili_jct_Entry标签.delete(0,END) # 删除所有值
    bili_jct_Entry标签.insert(0,bili_jct)
    bili_jct_Entry标签.config(state="readonly") # 设置为可复制但不能编辑

    main.mainloop()

def 未登录():
    未登录头像 = Image.open(io.BytesIO(requests.get("https://static.hdslb.com/images/member/noface.gif").content))
    未登录头像 = 未登录头像.resize((60, 60)) # 裁剪图片为60*60
    未登录头像 = ImageTk.PhotoImage(未登录头像)
    global 头像_标签,用户昵称_标签,登录按钮_控件,SESSDATA_标签,SESSDATA_Entry标签,bili_jct_标签,bili_jct_Entry标签,右键菜单_标签
    头像_标签 = Label(main, image=未登录头像)#把图片整合到标签类中
    头像_标签.pack(anchor="nw")
    用户昵称_标签 = Label(main, text="请先登录", font=('微软雅黑',12,'bold'))
    用户昵称_标签.place(x=70, y=5)
    登录按钮_控件 = Button(main, text="登录", command = 登录, width = 8)
    登录按钮_控件.place(x=70, y=35)
    SESSDATA_标签 = Label(main, text="SESSDATA", font=('微软雅黑',10))
    SESSDATA_标签.place(x=10, y=80)
    SESSDATA_Entry标签 = Entry(main, state = "normal", width =34)
    SESSDATA_Entry标签.place(x=85, y=80)
    SESSDATA_Entry标签.insert(0,"登录后显示Cookie")
    SESSDATA_Entry标签.config(state="readonly") # 设置为可复制但不能编辑
    bili_jct_标签 = Label(main, text="bili_jct", font=('微软雅黑',10))
    bili_jct_标签.place(x=20, y=110)
    bili_jct_Entry标签 = Entry(main, state = "normal", width =34)
    bili_jct_Entry标签.place(x=85, y=110)
    bili_jct_Entry标签.insert(0,"登录后显示Cookie")
    bili_jct_Entry标签.config(state="readonly") # 设置为可复制但不能编辑
    def copy(editor, event=None):
        editor.event_generate("<<Copy>>")
    def rightKey(event, editor):
        右键菜单_标签.delete(0,END)
        右键菜单_标签.add_command(label='复制',command=lambda:copy(editor))
        右键菜单_标签.post(event.x_root,event.y_root)

    右键菜单_标签 = Menu(main,tearoff=False)#创建一个菜单
    SESSDATA_Entry标签.bind("<Button-3>", lambda x: rightKey(x, SESSDATA_Entry标签))#绑定右键鼠标事件
    bili_jct_Entry标签.bind("<Button-3>", lambda x: rightKey(x, SESSDATA_Entry标签))#绑定右键鼠标事件

    main.mainloop()

def 网络已连接 (): # 判断网络是否连接正常
    try: # 异常调试
        requests.get ("https://www.bilibili.com/")
    except: # 如果requests请求异常，执行except内的操作
        return False
    return True


if 网络已连接 () == True: # 如果网络已连接
    未登录()
else: # 网络未连接
    def 重新检测网络():
        if 网络已连接 () == True: # 网络是否连接正常
            网络未连接_标签.destroy()
            网络未连接提示_标签.destroy()
            重新加载按钮_控件.destroy()
            未登录()
    网络未连接_标签 = Label(main, text="网络未连接！", font=('微软雅黑',12,'bold'), foreground="red")
    网络未连接_标签.place(x=10, y=5)
    网络未连接提示_标签 = Label(main, text="请关闭网络代理，或检查网络！", font=('微软雅黑',10))
    网络未连接提示_标签.place(x=10, y=30)
    重新加载按钮_控件 = Button(main, text ="重新加载", command = 重新检测网络)
    重新加载按钮_控件.place(x=10, y=60)

    main.mainloop()