import threading
import time
import queue
import _thread
exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("Staring" + self.name)
        process_data(self.name,self.q)
        print("Exitint" + self.name)
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1
nameList = ['one','two','three','four','five']
threadlist=['thread-1','thread-2','thread-3']
def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("{}processing{}".format(threadName,data))
        else:
            queueLock.release()
        time.sleep(1)
for tName in threadlist:
    thread = myThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID +=1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()
while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()
print("END")