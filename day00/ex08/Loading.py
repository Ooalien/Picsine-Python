import sys
import time
import shutil
from time import sleep


def ft_tqdm(lst: range) -> None:
    """Custom tqdm-like progress bar for iterables."""
    total = len(lst)
    terminal_width, _ = shutil.get_terminal_size()
    bar_length = terminal_width - 40
    start_time = time.time()
    sleep(0.01)
    for i, item in enumerate(lst):
        progress = (i + 1) / total
        filled_length = int(progress * bar_length)
        empty_length = bar_length - filled_length
        bar = '|' + '█' * filled_length + ' ' * empty_length + '|'
        percent = int(progress * 100)
        elapsed_time = time.time() - start_time
        speed = total / elapsed_time if elapsed_time > 0 else 0
        sys.stdout.flush()
        output = f"\r{percent}%{bar} {i + 1}/{total} "
        output += f"[00:00<00:00, {speed:.2f}it/s]"
        sys.stdout.write(output)
        sys.stdout.flush()
        yield item
    sys.stdout.write("\n")
    sys.stdout.flush()
