from os import get_terminal_size


def get_progress_nbr(i, loop):
    '''get the current number of iteration over the total of iterations
       in str format
       ex : 507/755'''
    progress_nbr = "| "
    progress_nbr += str(i)
    progress_nbr += '/'
    progress_nbr += str(loop)
    return (progress_nbr)


def get_progress_visual(percent, loop, bar_length):
    '''get a visual representation of the progress bar in str format
    ex : "|████████        " for a 50% progress'''
    progress_visual = '|'
    i = 0
    while (int(i * 100 / bar_length) < percent):
        progress_visual += '█'
        i += 1
    while (i < bar_length):
        progress_visual += ' '
        i += 1
    return progress_visual


def print_current_progress(i, loop, length_bar, end_char):
    '''carriage return and print on the terminal the progress bar'''
    percent = int(i * 100 / loop)
    progress_nbr = get_progress_nbr(i, loop)
    progress_visual = get_progress_visual(
        percent, i, length_bar - len(progress_nbr) - 5)
    print(f"\r{percent:=3}%{progress_visual}{progress_nbr}", end=end_char)


def ft_tqdm(lst: range):
    '''Display a progress bar that actualise at each iteration
       Take an iterable'''
    loop = len(lst)
    length_bar = get_terminal_size()[0]
    i = 0
    for elem in lst:
        print_current_progress(i, loop, length_bar, '')
        i += 1
        yield
    print_current_progress(i, loop, length_bar, '\n')
    print("\033[F\033[2K", end='')


def main():
    for elem in ft_tqdm(range(30000)):
        pass


if (__name__ == "__main__"):
    main()
