#!/usr/bin/env python3
import os
import sys
import time
import signal

# ================= COLORS =================
BLUE = "\033[94m"
WHITE = "\033[97m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
PINK = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

# ================= GLOBAL FLAGS =================
stop_requested = False
current_out_file = None

# ================= CTRL+C HANDLER =================
def handle_ctrl_c(signum, frame):
    global stop_requested, current_out_file
    stop_requested = True
    print(f"\n{YELLOW}[!] Ctrl+C detected. Safely stopping...{RESET}")
    if current_out_file:
        try:
            current_out_file.close()
        except:
            pass

signal.signal(signal.SIGINT, handle_ctrl_c)

# ================= CLEAR =================
os.system("clear" if os.name == "posix" else "cls")

# ================= BANNER =================
banner = [
    " ███████╗██████╗ ██╗     ██╗████████╗████████╗███████╗██████╗ ",
    " ██╔════╝██╔══██╗██║     ██║╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗",
    " ███████╗██████╔╝██║     ██║   ██║      ██║   █████╗  ██████╔╝",
    " ╚════██║██╔═══╝ ██║     ██║   ██║      ██║   ██╔══╝  ██╔══██╗",
    " ███████║██║     ███████╗██║   ██║      ██║   ███████╗██║  ██║",
    " ╚══════╝╚═╝     ╚══════╝╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝"
]

for i, line in enumerate(banner):
    print(f"{BLUE if i % 2 == 0 else WHITE}{line}{RESET}")
    time.sleep(0.04)

# ================= VERSION =================
print(f"{YELLOW}                 Version: v1.1{RESET}")
time.sleep(0.2)

# ================= CREDIT =================
credit = "                 Coded By: SAD MAN"
for ch in credit:
    sys.stdout.write(f"{BOLD}{RED}{ch}{RESET}")
    sys.stdout.flush()
    time.sleep(0.004)
print()

# ================= CONTACT =================
print(f"{GREEN}                 Contact: https://t.me/Alwayssaddy{RESET}")

print(f"{YELLOW}{'='*70}{RESET}\n")

# ================= INPUT =================
input_file = input(f"{CYAN}Enter the path of domain list: {RESET}").strip()
if not os.path.isfile(input_file):
    print(f"{RED}[!] File not found!{RESET}")
    sys.exit(1)

try:
    split_amount = int(input(f"{CYAN}Enter the amount to split (e.g. 10, 100): {RESET}"))
    if split_amount <= 0:
        raise ValueError
except ValueError:
    print(f"{RED}[!] Invalid number!{RESET}")
    sys.exit(1)

output_dir = os.path.dirname(os.path.abspath(input_file)) or "."

# ================= HELPERS =================
def format_time(seconds):
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds}s"
    if seconds < 3600:
        return f"{seconds//60}m {seconds%60}s"
    return f"{seconds//3600}h {(seconds%3600)//60}m"

# ================= COUNTING WITH PROGRESS + ETA =================
file_size = os.path.getsize(input_file)
read_bytes = 0
total_lines = 0
start_time = time.time()

print(f"{CYAN}[*] Counting total lines...{RESET}")

with open(input_file, "rb") as f:
    for line in f:
        if stop_requested:
            break
        total_lines += 1
        read_bytes += len(line)

        if total_lines % 100000 == 0:
            elapsed = time.time() - start_time
            speed = read_bytes / elapsed if elapsed > 0 else 0
            remaining = (file_size - read_bytes) / speed if speed > 0 else 0
            percent = (read_bytes / file_size) * 100
            filled = int(30 * percent / 100)
            bar = f"{PINK}{'█'*filled}{RESET}{'░'*(30-filled)}"
            sys.stdout.write(
                f"\r[{bar}] {percent:5.1f}% | ETA: {format_time(remaining)}"
            )
            sys.stdout.flush()

print()
print(f"{CYAN}[*] Total lines: {total_lines}{RESET}")

if stop_requested:
    print(f"{YELLOW}⚠️ Stopped during counting.{RESET}")
    sys.exit(0)

# ================= SPLITTING WITH ETA =================
def split_progress(done, total, start_time):
    percent = done / total
    filled = int(35 * percent)
    elapsed = time.time() - start_time
    speed = done / elapsed if elapsed > 0 else 0
    remaining = (total - done) / speed if speed> 0 else 0
    bar = f"{PINK}{'█'*filled}{RESET}{'░'*(35-filled)}"
    sys.stdout.write(
        f"\r[{bar}] {int(percent*100)}% ({done}/{total}) | ETA: {format_time(remaining)}"
    )
    sys.stdout.flush()

batch_num = 1
line_count = 0
processed = 0
start_time = time.time()

current_out_file = open(
    os.path.join(output_dir, f"batch{batch_num}.txt"),
    "w",
    encoding="utf-8"
)

with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if stop_requested:
            break

        line = line.strip()
        if not line:
            continue

        current_out_file.write(line + "\n")
        processed += 1
        line_count += 1

        if line_count >= split_amount:
            current_out_file.close()
            batch_num += 1
            current_out_file = open(
                os.path.join(output_dir, f"batch{batch_num}.txt"),
                "w",
                encoding="utf-8"
            )
            line_count = 0

        if processed % 10000 == 0:
            split_progress(processed, total_lines, start_time)

if current_out_file:
    current_out_file.close()

split_progress(total_lines, total_lines, start_time)
print("\n")

# ================= FINAL STATUS =================
if stop_requested:
    print(f"{YELLOW}⚠️ Stopped by user. Progress saved safely.{RESET}")
    print(f"{CYAN}📄 Last batch written: batch{batch_num}.txt{RESET}")
else:
    print(f"{GREEN}✅ DONE SUCCESSFULLY{RESET}")
    print(f"{GREEN}📄 Output files: batch1.txt, batch2.txt, ...{RESET}")
    print(f"{GREEN}📂 Saved in same directory as input file{RESET}")

print(f"{YELLOW}{'='*70}{RESET}")