
import os
CUR_PATH = os.path.dirname(os.path.realpath(__file__))

def get_all_info():
    return {
        "source_file": os.path.join(CUR_PATH, "examples/Shravan.jpg"),
        "target_file": os.path.join(CUR_PATH, "results/output.png"),
        "to": "png",
    }
