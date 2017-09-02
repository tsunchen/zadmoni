import os,sys

from core import main
from conf import setting


base_dir = os.path.dirname(os.path.dirname(__file__))
print base_dir
sys.path.append(base_dir)

if __name__=='__main__':
    client = main.MoniClient()
    client.start()
    #pass
