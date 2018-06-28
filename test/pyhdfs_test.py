#!/usr/bin/env python
import time
import pyhdfs

host = "default"
port = 0

TEST_ROOT="/user/ai_data/hzxiahouzuoxin/"

def main():
    print("connecting")
    fs = pyhdfs.connect(host, port)
    
    try:
        print("opening testfile.txt for writing") 
        f = pyhdfs.open(fs, TEST_ROOT+"testfile.txt", "w")
    
        print( "writing" )
        written = pyhdfs.write(fs, f, "hoho\0haha\nxixi")
        print( "written %d bytes" % (written) )
        
        print( "flushing" )
        pyhdfs.flush(fs, f)
    
        print( "closing file" )
        pyhdfs.close(fs, f)
    
        print( "checking existence" )
        if pyhdfs.exists(fs, TEST_ROOT+"testfile.txt"):
            print( "getting" )
            pyhdfs.get(fs, TEST_ROOT+"testfile.txt", "./testfile.txt")
	    
        print("putting")
        pyhdfs.put(fs, "pyhdfs_test.py", TEST_ROOT)
        
        print( "opening testfile.txt for reading" )
        f = pyhdfs.open(fs, TEST_ROOT+"testfile.txt", "r")
        
        print( "reading first 5 bytes" )
        s = pyhdfs.read(fs, f, 5)
        print( s, len(s) )
        
        print( "reading remaining" )
        s = pyhdfs.read(fs, f)
        print( s, len(s) )
        
        print( "telling" )
        print( pyhdfs.tell(fs, f) )
        
        print( "reading" )
        s = pyhdfs.read(fs, f)
        print( s, len(s) )
        
        print( "position reading from 5" )
        s = pyhdfs.pread(fs, f, 5)
        print( s, len(s) )
        
        print( "seeking" )
        pyhdfs.seek(fs, f, 1)
        
        print( "telling" )
        print( pyhdfs.tell(fs, f) )
        
        print( "closing file" )
        pyhdfs.close(fs, f)

        print( "updating file time" )
        pyhdfs.utime(fs, TEST_ROOT+"testfile.txt", int(time.time()), int(time.time()))        
        
        print( "stating file" )
        print( pyhdfs.stat(fs, TEST_ROOT+"testfile.txt") )
        
        print( "stating nosuchfile" )
        print( pyhdfs.stat(fs, "/test/nosuchfile") )

        print( "stating dir" )
        print( pyhdfs.stat(fs, "/test") )

        print( "mkdir dir testdir" )
        print( pyhdfs.mkdir(fs, TEST_ROOT+"testdir") )

        print( pyhdfs.stat(fs, TEST_ROOT+"testdir") )

        print( "listing directory" )
        l = pyhdfs.listdir(fs, TEST_ROOT+"")
        for i in l:
            print( i )

        print( "current working directory" )
        print( pyhdfs.getcwd(fs) )

        print( "changing to root directory" )
        print( pyhdfs.chdir(fs, '/'))

        print( "current working directory" )
        print( pyhdfs.getcwd(fs) )  
            
    finally:
        print( "disconnecting")
        pyhdfs.disconnect(fs)
    
if __name__ == "__main__":
    main()

