from NSController import Controller
ctr = Controller()
#先触发vs断网跳帧的bug，然后进入设置-->日期与时间，光标停留在日期和时间上
for i in range(1,7558):#示例：跳至7558帧
    if(i%200 == 0):#每跳200帧存档1次
        ctr.h()
        ctr.pause(2)
        ctr.A()
        ctr.pause(2)
        ctr.X()
        ctr.pause(2)
        ctr.R()
        ctr.pause(2)
        ctr.A()
        ctr.pause(5)
        ctr.h()
        ctr.pause(1)
        ctr.d()
        ctr.r()
        ctr.r()
        ctr.r()
        ctr.r()
        ctr.A()
        ctr.pause(1)
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.r()
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.d()
        ctr.A()
        ctr.d()
        ctr.d()
    else:
        #year+1
        ctr.A()
        ctr.l()
        ctr.l()
        ctr.l()
        ctr.l()
        ctr.l()
        ctr.u()
        ctr.r()
        ctr.r()
        ctr.r()
        ctr.r()
        ctr.r()
        ctr.A()
        #year-1
        ctr.A()
        ctr.l()
        ctr.l()
        ctr.l()
        ctr.l()
        ctr.l()
        ctr.d()
        ctr.r()
        ctr.r()
        ctr.r()
        ctr.r()
        ctr.r()
        ctr.A()
    print(i)

ctr.close()