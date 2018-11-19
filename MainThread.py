#!/usr/bin/env python3

import time
import random
from threading import Thread, Condition
from ExtractFrames import *
from ConvertToGrayscale import *
from DisplayFrames import *

queue_list = [] #empty queue
MAX_BOUND = 10  #max frames
condition = Condition()

#producer class
class ProducerThread(Thread):
    def run(self):
        global queue_list
        count = 0

        while True:
            condition.acquire()
            if len(queue_list) == MAX_BOUND: #max number of frames in queue
                print ("Producer waiting") #producer waits for queue to be emptied
                condition.wait()
                print ("Consumer notified the producer")

            #threads start to extract-> convert-> display
            ExtractingThread().start()
            GrayscaleConvertThread().start()
            DisplayThread().start()

            queue_list.append(count)
            count = count + 1
            condition.notify()
            condition.release()
            time.sleep(random.random())

#consumer class
class ConsumerThread(Thread):
    def run(self):
        global queue_list