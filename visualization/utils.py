import matplotlib.pyplot as plt


def get_label(str, length):
    """returns label with spaces replaced by \n if is too long"""
    if len(str) <= length:
        return str

    label = str[:length].rsplit(" ", 1)
    label = '\n'.join(label) + get_label(str[length:], length)
    return label


def press(event):
    """Close matplotlib plot when Escape key is pressed"""
    if event.key == "escape":
        plt.close()


def get_numerical_data(data):
    """returns dataset with only numerical data columns"""
    num_data = data.select_dtypes(include=['number'])
    if "Index" in num_data.columns:
        num_data = num_data.drop("Index", axis='columns')
    if "Hogwarts House" in num_data.columns:
        num_data = num_data.drop("Hogwarts House", axis='columns')
    return num_data


def init_subplots(n_plots, nrows, ncols):
    """
        Creates a subplot with parameters passed as arguments
        Doesn't display empty diagrams
        Displays in fullscreen size
        Links to Escape key
        Returns the axes
    """
    fig, axes = plt.subplots(
        nrows=nrows,
        ncols=ncols,
        figsize=(10, 10)
    )

    # make invisible the last diagrams that are empty
    for i in range(nrows * ncols - n_plots):
        axes[nrows - 1, ncols - 1 - i].set_visible(False)

    # display fullscreen
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()

    # link escape key to close the window
    fig.canvas.mpl_connect('key_press_event', press)

    return axes
