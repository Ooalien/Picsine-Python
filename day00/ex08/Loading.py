import sys
import time
import shutil
from time import sleep


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    terminal_width, _ = shutil.get_terminal_size()
    bar_length = terminal_width - 40
    start_time = time.time()
    sleep(0.01)
    for i, item in enumerate(lst):
        progress = (i + 1) / total 
        bar = '|' + '█' * int(progress * bar_length) + ' ' * (bar_length - int(progress * bar_length)) + '|'
        percent = int(progress * 100)
        elapsed_time = time.time() - start_time
        speed = total / elapsed_time if elapsed_time > 0 else 0
        sys.stdout.flush()
        sys.stdout.write(f"\r{percent}%{bar} {i + 1}/{total} [00:00<00:00, {speed:.2f}it/s]")
        sys.stdout.flush()
        yield item
    sys.stdout.write("\n")
    sys.stdout.flush()
