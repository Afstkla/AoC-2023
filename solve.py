from src.days import *

for day in range(1, 26):
    try:
        globals()[f"Day{day}Solver"]().solve_and_print()
    except FileNotFoundError:
        pass
