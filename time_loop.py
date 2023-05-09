import time

from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()

@tl.job(interval=timedelta(seconds=30))
def train_model():
    print("call Dask cluster 300s job current time : {}".format(time.ctime()))