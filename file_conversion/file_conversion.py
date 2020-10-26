#import anyconv as conv
from anyconv import Anyconv
import  json


import os
CUR_PATH = os.path.dirname(os.path.realpath(__file__))

def get_all_info():
    with open(CUR_PATH+'/info.json') as json_file:
        info = json.load(json_file)
        return info #["source_file"], info["target_file"], info["to"]

def main():
    print("**1**")
    print(get_all_info())
    print("**2**")

    #ac = conv.Anyconv(get_all_info())
    ac = Anyconv(get_all_info())
    print("**3**")
    ac.convert()
    print("**4**")

if __name__ == "__main__":
    main()
