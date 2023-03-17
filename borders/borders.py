import os

def main():

    col = frame(["Enter a colour"], window="in")
    os.system("clear")
    
    try:
        col = int(col)
    except:
        pass

    menu_list = [
        ("\t\t  This is border.py","Bright Cyan"),
        "",
        ("This is an original module created by","Bright Cyan"),
        "",
        ("\t\t   Simon Calvaruso","Bright Cyan"),
        ]

    frame(menu_list, colour=col)


def frame(menu_list, colour=37, text_background=0, frame_colour=None, frame_background=None, spacing=1, min_width=8, max_width=70, window="print"):
    """
    This function create a frame around the content of a list.
    Any item of the list is considered a new line.
    Items allowed are strings or tuples containing a string and one or two numeric values for the colour of the same line.
    
    Parameters:
        colour: allows to change the colour of the text.
            default value = 37
        text_background: allows to change the background colour of the text.
            default value = 0 
        frame_colour: allows to change the colour of the frame.
            default value = None, if not specified get the same colour value of the text.
        frame_background: allows to change the background colour of the frame.
            default value = None, if not specified get the same value of text_background.
        spacing: allows to increase or decrease the space between the frame and the text.
            default value = 1
        min_width: allows to set the minimum width inside the frame.
            default value = 8
        max_width: allows to set the max length of text on a line.
            default value = 70
        window: allows the function to behave as input.
            default value = 'print'

    Returns:
        Print a frame around the output or the input prompt.
    """
    # Check validity of the colours.
        
    colour = _valid_colour(colour)
    text_background = _valid_colour(text_background, "back")
    
    if frame_colour:
        frame_colour = _valid_colour(frame_colour)
    else:
        frame_colour = colour

    if frame_background:
        frame_background = _valid_colour(frame_background, "back")
    else:
        frame_background = text_background

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

    # Check the lenght of every line and split them if too long.
    menu_list = _split_line(menu_list, max_width, colour, text_background)

    # Create the frame.
    max_width = max([(len(i[0].rstrip(" "))) for i in menu_list])

    if max_width > (menu_width-(border_space*2)):
        menu_width = max_width + (border_space*2)

    or_line = "═" * menu_width
    filling = " " * menu_width
    display_menu = f"\033[{frame_background};{frame_colour}m" + "╔" + or_line + "╗" + "\033[0m\n"

    for _ in range(spacing):
        display_menu += f"\033[{frame_background};{frame_colour}m" + "║" + f"\033[{text_background}m" + filling + f"\033[0m" + f"\033[{frame_background};{frame_colour}m" + "║" +"\033[0m\n"

    for item in menu_list:
        item_width = len(item[0]+(side_space*2))
        filling = " " * (menu_width - item_width)
        display_menu += f"\033[{frame_background};{frame_colour}m" + "║" + f"\033[{item[2]}m" + side_space + f"\033[{item[1]}m" + item[0] + side_space + filling + f"\033[0m" + f"\033[{frame_background};{frame_colour}m" + "║" +"\033[0m\n"

    filling = " " * menu_width

    for _ in range(spacing):
        display_menu += f"\033[{frame_background};{frame_colour}m" + "║" + f"\033[{text_background}m" + filling + f"\033[0m" + f"\033[{frame_background};{frame_colour}m" + "║" + "\033[0m\n"

    display_menu += f"\033[{frame_background};{frame_colour}m" + "╚" + or_line + "╝" + "\033[0m\n"

    # Change the behaviour of the function from 'print' to 'input'.
    if window=="in" or window=="input":
        return input(display_menu)
    else:
        print(display_menu)


# This function check the validity of the colour value.
def _valid_colour(col, body="body"):
    
    if body == "back":
        ansi_colours = {
    "Black": 40, "Red": 41, "Green": 42, "Yellow": 43, "Blue": 44, "Magenta": 45, "Cyan": 46, "White": 47,
    "Bright Black": 100, "Bright Red": 101, "Bright Green": 102, "Bright Yellow": 103, "Bright Blue": 104, "Bright Magenta": 105, "Bright Cyan": 106, "Bright White": 107,
    "Reset": 0,
    }
    else:
        ansi_colours = {
    "Black": 30, "Red": 31, "Green": 32, "Yellow": 33, "Blue": 34, "Magenta": 35, "Cyan": 36, "White": 37,
    "Bright Black": 90, "Bright Red": 91, "Bright Green": 92, "Bright Yellow": 93, "Bright Blue": 94, "Bright Magenta": 95, "Bright Cyan": 96, "Bright White": 97,
    "Reset": 0,
    }
   
    try:
        col = int(col)
    except:
        col = col.title().replace("Light","Bright")
    
    if col in ansi_colours.values():
        out_col = col
    elif col in ansi_colours.keys():
        out_col = ansi_colours[col]
    else:
        out_col = "0"

    return out_col


# This function return a list of every line to print with its colour attributes.
def _split_line(menu_list, max_width, t_colour, t_background):
    new_list = []
    
    for item in menu_list:
        line = ""

        # Check if item is a tuple.
        if isinstance(item, tuple):
            """
            If True:
            item[0] is the string
            item[1] is the colour of the text
            item[2] is the backgroud colour of the text.
            """
            words = item[0].split(" ")
            if item[1] != "":
                text_colour = _valid_colour(item[1])
            else:
                text_colour = t_colour    
            try:
                text_background = _valid_colour(item[2], "back")
            except:
                text_background = t_background
                pass
        else:
            words = item.split(" ")
            text_colour = t_colour
            text_background = t_background

        space = " "

        # Split the lines if they are longer than the max length characters.
        for word in words:
            word = word.replace("\t", "    ")
            
            if len(word) >= max_width:
                line = word[:max_width]
                new_list.append((line.rstrip(" "), text_colour, text_background))
                line = word[max_width:] + space
            elif len(line+word) < (max_width+1):
                line += word + space
            else:
                new_list.append((line.rstrip(" "), text_colour, text_background))
                line = word + space

        new_list.append((line.rstrip(" "), text_colour, text_background))

    return new_list


if __name__ == "__main__":
    main()