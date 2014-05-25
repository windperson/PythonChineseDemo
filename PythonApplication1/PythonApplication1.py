# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
first = file(sys.argv[1],'r')
second = file(sys.argv[2], 'w')
print u'輸入檔案為:'.encode('cp950'), '\'%s\''%sys.argv[1]
print '输入档案为:'.encode('gbk'), '\'%s\''%sys.argv[1]
print '\n'
print u"輸出檔案為:".encode("cp950"), "\"{}\"".format(sys.argv[2])
print "输出档案为:".encode("gbk"), "\"{}\"".format(sys.argv[2]) 
for line in first:
    second.write(line)
first.close()
second.close()
print 'press enter to continue'
raw_input()