
import sys,os,datetime
from pathlib import Path
_projectDir = Path(__file__).resolve().parents[2]
sys.path.append(os.path.join(_projectDir))
from MarketPlace.resources import Task, TaskByID

task = Task()
taskbyid=TaskByID()
#obj = task.get()

# Test Case.1 - Test the get and post requests
# To be done..when i get a chance this week.
