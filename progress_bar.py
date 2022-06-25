from time import time, sleep
from colorama import Fore
import sys
import os
import threading


class ProgressBar:
    progress = 0
    width = 50
    start_time = time()
    end_time = time()-1
    caption = "Progress"
    box_char = '█'
    empty_box_char = '░'
    string = ' |{filledboxes}{emptyboxes}| {progress:.2f}% time elapsed: {time:.2f}s '
    len_of_prev_string = 0
    is_complete =False
    def __init__(self, caption='Progress', width=50):
        self.start_time = time()
        self.caption = caption
        print(self.caption, end='')
        self.update(0)

    def update(self, p):
        self.progress = max(0, min(1, p))
        boxes = round(self.width * self.progress)

        string = self.string.format(filledboxes=self.box_char * round(self.width*self.progress), emptyboxes=self.empty_box_char*round(
            self.width*(1-self.progress)), progress=100*self.progress, time=time()-self.start_time)
        print('\b \b'*self.len_of_prev_string + string, end='')
        self.len_of_prev_string = len(string)
        if(self.progress == 1):
            print(Fore.GREEN + ' Complete', end='')
            print(Fore.WHITE + '')
        if self.progress == 1:
            is_complete = True
            return
        self.end_time = time()
    def isComplete(self):
        return self.is_complete
    def get_elapsed_time(self):
        return self.end_time - self.start_time


class FixedUpdateProgressBar:
    progress = 0.0
    updatePeriod = 0.2
    caption = "Progress"
    width = 50
    def __init__(self, _caption='Progress', update_period=0.1, _width=50):
        self.updatePeriod = update_period
        self.caption = _caption
        self.width = _width
        self._progressBar = ProgressBar(caption=self.caption, width=self.width)
        self.thread = threading.Thread(target=self.constant_updater)
    
    def constant_updater(self):
        while True:
            self._progressBar.update(self.progress)
            if self.progress == 1 or self._progressBar.isComplete():
                break
            sleep(self.updatePeriod)
    def start(self):
        self.thread.start()
    def end(self):
        self.update(1)
        self.thread.join()
    def update(self,_progress):
        self.progress = max(0, min(1, _progress))
