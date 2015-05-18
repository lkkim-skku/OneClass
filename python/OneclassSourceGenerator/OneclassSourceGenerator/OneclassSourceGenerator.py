import os

from osgpy import osgpy

if __name__ == "__main__" : 
    clist = []
    for dirname, dirnames, filenames in os.walk('.'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            os.path.join(dirname, subdirname)
            #print(os.path.join(dirname, subdirname))

        if 'data' in dirname :
            if filenames : 
                clsname = dirname.split('\\')
                osg = osgpy('_'.join(clsname[2:]))
                # print path to all filenames in subdirname.
                for filename in filenames:
                    if '.txt' in filename and not '%' in filename:
                        os.path.join(dirname, filename)
                        #print os.path.join(dirname, filename)
                        dlist = []
                        file = open(dirname + '\\' + filename, 'r')
                        file.readline(), file.readline(), file.readline()
                        lines = file.readlines()
                        for line in lines : 
                            dlist.append(line)
                        osg.appendData(dlist)
                osg.closeClass()
                #print data
                clist.append(osg)
                print 'append %s' % osg.getName()

    #feature-scaling
    setFeatureScaling(clist)
    #export Data
    with open('merge.csv', 'wb') as fm : 
        for c in clist : 
            with open(c.getName() + '.csv', 'wb') as f : 
                for data in c.getRawData() : 
                    f.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%(data[0], repr(data[1]), repr(data[2]), repr(data[3]), repr(data[4]), repr(data[5]), repr(data[6]), repr(data[7]), repr(data[8]), repr(data[9]), repr(data[10]), repr(data[11]), repr(data[12])))
                    fm.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%(data[0], repr(data[1]), repr(data[2]), repr(data[3]), repr(data[4]), repr(data[5]), repr(data[6]), repr(data[7]), repr(data[8]), repr(data[9]), repr(data[10]), repr(data[11]), repr(data[12])))
                    pass
                print 'file write : ' + c.getName() + '.csv'