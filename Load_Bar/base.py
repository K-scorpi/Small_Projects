import time
from tqdm import tqdm

m = [0] * 5


def line(n: int):
    for i in tqdm(range(n)):
        time.sleep(2)
    return True


line(len(m))
