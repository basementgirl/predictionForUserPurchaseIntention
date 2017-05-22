from datetime import timedelta
from datetime import date
from ui_flag import get_ui_flag_each_time
import time
start_time=time.time()

#控制得到60次训练集flag的总循环
j = 1
firstDay = date(2016, 2, 1)
while j < 61:
    ui_flag = get_ui_flag_each_time(j,firstDay)
    firstDay = firstDay + timedelta(1)
    print('di %d ge training set is done!' % j)
    ui_flag.to_csv('ui_feature_and_flag/train_set_%d_ui_flag.csv' % j,index=False)
    j+=1
    print(time.time()-start_time)
