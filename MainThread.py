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
