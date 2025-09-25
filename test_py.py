


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, num):
        self.queue.insert(0, num)

    def get(self):
        if len(self.queue) > 0:
            num = self.queue[-1]
            del self.queue[-1]
            return num
        else:
            
            raise Exception
        
            


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("ERRRRRRRRRRRReda")