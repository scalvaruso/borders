
import os

def main():
    menu_list = ["",
    "\t\t   This is border.py",
    "",
    "This is an original module created by",
    "",
    "\t\t   Simone Calvaruso",
    "",
    ]

    col = frame(["Enter a colour"], window="in")
    os.system("clear")
    try:
        col = int(col)
    except:
        pass

    frame(menu_list, colour=col)


def frame(menu_list, colour=0, spacing=1, min_width=8, max_width=70, window="print"):
    """
    This function create a frame around the content of a list.
    Any item of the list is considered a new line.
    
    Parameters:
        colour: allows to change the colour of the window.
            default value = 'white'
        spacing: allows to increase or decrease the space between the frame and the text.
            default value = 1
        min_width: allows to set the minimum width inside the frame.
            default value = 8
        max_width: allows to set the max length of text on a line.
            default value = 70
        window: allows the function to behave as input.
            default value = 'print'

    Returns:
        Print a frame around the output or the input prompt
    """

    ansi_colours = [0,30,31,32,33,34,35,36,37,90,91,92,93,94,95,96,97,
    40,41,42,43,44,45,46,47,100,101,102,103,104,105,106,107]

    # Set the colour of the frame.
    if type(colour) == str:
        colour = colour.lower()
    
    if colour in ansi_colours:
        pass
    elif colour == "red":
        colour = "91"
    elif colour == "green":
        colour = "92"
    elif colour == "yellow":
        colour = "93"
    elif colour == "cyan":
        colour = "96"
    elif colour == "blue":
        colour = "94"
    elif colour == "pink":
        colour = "95"
    else:
        colour = "0"

    new_list = []

    # Check the menu spacing and width.
    if spacing < 1:
        border_space = 0
        menu_width = 0
    else:
        border_space = spacing * 4
        menu_width = min_width
    side_space = border_space * " "
    
    if max_width < min_width:
        max_width = min_width
    
    if max_width < 5:
        max_width = 5

    # Split the lines if they are longer than 70 characters.
    for item in menu_list:
        line = ""
        words = item.split(" ")
        space = " "
        for word in words:
            word = word.replace("\t", "    ")
            
            if len(word) >= max_width:
                line = word[:max_width]
                new_list.append(line.rstrip(" "))
                line = word[max_width:] + space
            elif len(line+word) < (max_width+1):
                line += word + space
            else:
                new_list.append(line.rstrip(" "))
                line = word + space

        new_list.append(line.rstrip(" "))

    menu_list = new_list

    # Create the frame.
    max_width = max([(len(i.rstrip(" "))) for i in menu_list])

    if max_width > (menu_width-(border_space*2)):
        menu_width = max_width + (border_space*2)

    or_line = "═" * menu_width
    filling = " " * menu_width
    display_menu = f"\033[{colour}m" + "╔" + or_line + "╗\n"

    for _ in range(spacing):
        display_menu += "║" + filling + "║\n"

    for item in menu_list:
        out_item = side_space + item + side_space
        item_width = len(out_item)
        filling = " " * (menu_width - item_width)
        display_menu += "║" + out_item + filling + "║\n"

    filling = " " * menu_width

    for _ in range(spacing):
        display_menu += "║" + filling + "║\n"

    display_menu += "╚" + or_line + "╝\033[0m\n"

    # Change the behaviour of the function from 'print' to 'input'.
    if window=="in" or window=="input":
        return input(display_menu)
    else:
        print(display_menu)


if __name__ == "__main__":
    main()