#！/user/bin/env python3
# -*- coding:utf-8 -*-
from io import StringIO
# write to StringIO
f= StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())
# read to StringIO:
f=StringIO('水面细分生，\n楞个慢慢升')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())
