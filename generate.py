import os,sys
import hashlib

def md5file(path):
    m=hashlib.md5()
    try:
        file=open(path,'rb')
        m.update(file.read())
        file.close()
    except Exception as e:
        print path,e
        return '*'*32
    return m.hexdigest()

def listallfiles(root,path):
    newroot=os.path.join(root,path)
    if os.path.isdir(newroot):
        list=[]
        ls=os.listdir(newroot)
        for i in ls:
            newpath=os.path.join(path,i)
            list+=listallfiles(root,newpath)
        return list
    if os.path.isfile(newroot):
        return [path];

def main():
    if len(sys.argv)!=2:
        print 'arg error'
        return
    root=sys.argv[1]

    # list all files
    list=listallfiles(root,'')

    # gen md5 for those files
    f=open('checksum.md5','w')
    lenlist=len(list)
    print '*'*25
    count=0
    x=0
    for i in list:
        x+=1
        if x*25/lenlist>count:
            sys.stdout.write('*'*(x*25/lenlist-count))
            sys.stdout.flush()
            count=x*25/lenlist
        f.write(md5file(os.path.join(root,i))+' '+i+'\n')
    f.close()
    print ''
    return

if __name__=='__main__':
    main()