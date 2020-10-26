#import anyconv as conv
from anyconv import Anyconv
from info import get_all_info


def main():
    ac = Anyconv(get_all_info())
    ac.convert()

if __name__ == "__main__":
    main()
