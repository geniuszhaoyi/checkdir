import os,sys

def checksum(path):
    mp={}
    f=open(path)
    ls=f.readlines()
    for i in ls:
        x=i[0:32]
        y=i[32:-1]
        mp[y]=x
    f.close()
    return mp

def main():
    if len(sys.argv)!=3:
        print 'arg error'
        return
    
    mp1=checksum(sys.argv[1])
    mp2=checksum(sys.argv[2])

    fcor=open('corrpted.txt','w')
    fcor.write('file1\tfile2\tkey')
    for key,val in mp1.items():
        if key in mp2:
            if val!=mp2[key]:
                fcor.write(val+'\t'+mp2[key]+'\t'+key+'\n')
            del mp1[key]
            del mp2[key]
    fcor.close()

    fm1=open('FileMiss_1','w')
    fm1.write('This list show the file(s) which are in file1 but ont in file2. \n\n')
    for key,val in mp1.items():
        fm1.write(val+' '+key+'\n')
    fm1.close()

    fm2=open('FileMiss_2','w')
    fm2.write('This list show the file(s) which are in file2 but ont in file1. \n\n')
    for key,val in mp1.items():
        fm2.write(val+' '+key+'\n')
    fm2.close()
    return

if __name__=='__main__':
    main()