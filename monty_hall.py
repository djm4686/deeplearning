import random
import matplotlib.pylab as plt



def create_doors(doors=3):
    out = [0]*doors
    out[random.randint(0,doors-1)] = 1
    return out

def open_goats(choice, doors):
    prize = doors.index(1)
    goats = doors.count(0) - 1
    if doors[choice] == 0:
        goats -= 1
    out = ['?']*len(doors)
    count = 0
    out[choice] = "choice"
    for i, x in enumerate(out):
        if count >= len(doors) - 2:
            break
        if i == choice:
            continue
        if doors[i] == 0 and i != prize:
            out[i] = "goat"
            count += 1
        continue
    return out

def keep_or_swap(opened_doors, swap=True):
    if swap:
        choice = opened_doors.index("?")
    else:
        choice = opened_doors.index("choice")
    return choice

def is_winner(choice, doors):
    return doors[choice] == 1

def do_trials(trials_count=10000, num_doors=3, swap=True):
    wins = 0
    losses = 0
    for x in range(trials_count):
        choice = random.randint(0, num_doors-1)
        d = create_doors(num_doors)
        opened = open_goats(choice, d)
        print(opened)
        choice = keep_or_swap(opened, swap)
        if is_winner(choice, d):
            wins += 1
        else:
            losses += 1
    return wins, losses

if __name__ == "__main__":

    # swap
    wins, losses = do_trials()
    plt.bar(["swap_wins", "swap_losses"], [wins, losses])

    # Dont swap
    dwins, dlosses = do_trials(swap=False)
    plt.bar(["dont_swap_wins", "dont_swap_losses"], [dwins, dlosses])
    plt.show()

