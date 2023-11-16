import os
from textlinebreaker import split_line

def main():

    menu_1 = [
        ("This is border.py","Bright White","Bright Black","centre"),
        ("","","Cyan"),
        ("This is an original module created by","Bright Blue","White","centre"),
        ("","","Magenta"),
        ("Simon Calvaruso","Bright Red","Bright Yellow","right"),
        "",
        "Borders creates a frame around the content of a list.",
        "Any item of the list is considered a new line.",
        "Items allowed are strings or tuples containing:",
        "a string with text to print,",
        "one or two values (integers or strings) for foreground and background colours of the text,",
        "one string value for the alignment of the line."
        ]
    menu_2 = [
        ("Parameters:","","Bright Red","centre"),"",
        ("colour:","Bright Red","centre"), "allows to change the colour of the text.",
        "default value = 37",
        "allowed values:",
        "0, 30, 31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97,",
        "'Black', 'Red', 'Green', 'Yellow', 'Blue', 'Magenta', 'Cyan', 'White',",
        "'Bright Black', 'Bright Red', 'Bright Green', 'Bright Yellow', 'Bright Blue', 'Bright Magenta', 'Bright Cyan', 'Bright White'",
        ("text_background:","Bright Red","centre"), "allows to change the background colour of the text.",
        "default value = 0",
        "allowed values:",
        "0, 40, 41, 42, 43, 44, 45, 46, 47, 100, 101, 102, 103, 104, 105, 106, 107",
        "'Black', 'Red', 'Green', 'Yellow', 'Blue', 'Magenta', 'Cyan', 'White',",
        "'Bright Black', 'Bright Red', 'Bright Green', 'Bright Yellow', 'Bright Blue', 'Bright Magenta', 'Bright Cyan', 'Bright White'",
        ("frame_colour:","Bright Red","centre"), "allows to change the colour of the frame.",
        "default value = None",("(if not specified get the same colour value of the text)","right"),
        "allowed values:",
        "0, 30, 31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97",
        "'Black', 'Red', 'Green', 'Yellow', 'Blue', 'Magenta', 'Cyan', 'White',",
        "'Bright Black', 'Bright Red', 'Bright Green', 'Bright Yellow', 'Bright Blue', 'Bright Magenta', 'Bright Cyan', 'Bright White'",
        ("frame_background:","Bright Red","centre"), "allows to change the background colour of the frame.",
        "default value = None",("(if not specified get the same value of text_background).","right"),
        "allowed values:",
        "0, 40, 41, 42, 43, 44, 45, 46, 47, 100, 101, 102, 103, 104, 105, 106, 107",
        "'Black', 'Red', 'Green', 'Yellow', 'Blue', 'Magenta', 'Cyan', 'White',",
        "'Bright Black', 'Bright Red', 'Bright Green', 'Bright Yellow', 'Bright Blue', 'Bright Magenta', 'Bright Cyan', 'Bright White'",
        ("alignment:","Bright Red","centre"), "allows to change the alignment of the text inside the frame.",
        "default value = 'left'",
        "allowed values: 'left', 'centre', 'center', 'right'",
        ("display:","Bright Red","centre"), "allows to change the position of the frame inside the terminal.",
        "default value = 'left'",
        "allowed values: 'left', 'centre', 'center', 'right'",
        ("spacing:","Bright Red","centre"), "allows to increase or decrease the space between the frame and the text.",
        "default value = 1",
        "allowed values: from 0 to 3",
        ("min_width:","Bright Red","centre"), "allows to set the min length of text in a line.",
        "default value = 42",
        "allowed values: integers above 8, 'max'",("(this value assign to the frame the width of the terminal)","right"),
        ("max_width:","Bright Red","centre"), "allows to set the max length of text in a line.",
        "default value = 70",
        "allowed values: integers above 8, 'max'",("(this value assign to the frame the width of the terminal)","right"),
        ("window:","Bright Red","centre"), "allows the function to behave as input.",
        "default value = 'print'",
        "allowed values: 'print', 'input'",
        "",
        ("Returns:","","Bright Red","centre"),
        "Print a frame around the output or the input prompt."
        ]

    frame(menu_1, text_background=0, frame_colour="Blue", frame_background=0, max_width=75, display="centre", spacing=1)
    frame(menu_2, text_background=0, frame_colour="Blue", frame_background=0, min_width=75, display="centre", spacing=1)


def frame(menu_list, colour=37, text_background=0, frame_colour=None, frame_background=None, alignment="left", display="left", spacing=1, min_width=42, max_width=70, window="print"):
    """
    This function create a frame around the content of a list.
    Any item of the list is considered a new line.
    Items allowed are strings or tuples containing:
    a string with text to print,
    one or two values (integers or strings) for foreground and background colours of the text,
    one string value for the alignment of the line.
    
    Parameters:
        colour: allows to change the colour of the text.
            default value = 37
            allowed values: 0, 30, 31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97,
                            "Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White",
                            "Bright Black", "Bright Red", "Bright Green", "Bright Yellow", "Bright Blue", "Bright Magenta", "Bright Cyan", "Bright White"
        text_background: allows to change the background colour of the text.
            default value = 0
            allowed values: 0, 40, 41, 42, 43, 44, 45, 46, 47, 100, 101, 102, 103, 104, 105, 106, 107
                            "Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White",
                            "Bright Black", "Bright Red", "Bright Green", "Bright Yellow", "Bright Blue", "Bright Magenta", "Bright Cyan", "Bright White"
        frame_colour: allows to change the colour of the frame.
            default value = None (if not specified get the same colour value of the text).
            allowed values: 0, 30, 31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97
                            "Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White",
                            "Bright Black", "Bright Red", "Bright Green", "Bright Yellow", "Bright Blue", "Bright Magenta", "Bright Cyan", "Bright White"
        frame_background: allows to change the background colour of the frame.
            default value = None (if not specified get the same value of text_background).
            allowed values: 0, 40, 41, 42, 43, 44, 45, 46, 47, 100, 101, 102, 103, 104, 105, 106, 107
                            "Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White",
                            "Bright Black", "Bright Red", "Bright Green", "Bright Yellow", "Bright Blue", "Bright Magenta", "Bright Cyan", "Bright White"
        alignment: allows to change the alignment of the text inside the frame.
            default value = "left"
            allowed values: "left", "centre", "center", "right"
        display: allows to change the position of the frame inside the terminal.
            default value = "left"
            allowed values: "left", "centre", "center", "right"
        spacing: allows to increase or decrease the space between the frame and the text.
            default value = 1
            allowed values: from 0 to 3
        min_width: allows to set the min length of text in a line.
            default value = 42
            allowed values: integers above 8, "max" (this value assign to the frame the width of the terminal)
        max_width: allows to set the max length of text in a line.
            default value = 70
            allowed values: integers above 8, "max" (this value assign to the frame the width of the terminal)
        window: allows the function to behave as input.
            default value = "print"
            allowed values: "print", "input"

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

    t_colour = colour
    t_background = text_background

    # Retrieve terminal width
    terminal_width = os.get_terminal_size().columns

    # Set default text alignment
    line_alignment = alignment

    # Check the menu spacing and width.

    if spacing < 0:
        spacing = 0
    elif spacing > 3:
        spacing = 3

    border_space = int(spacing * 4)

    if str(min_width).lower() == "max":
        min_width = terminal_width - (2*border_space+2)
    if min_width > (terminal_width - (2*border_space+2)):
        min_width = terminal_width - (2*border_space+2)
    elif min_width < 8:
        min_width = 8

    menu_width = min_width
    side_space = border_space * " "
    
    if str(max_width).lower() == "max":
        max_width = terminal_width - (2*border_space+2)
    if max_width > (terminal_width - (2*border_space+2)):
        max_width = terminal_width - (2*border_space+2)
    elif max_width < min_width:
        max_width = min_width
    
    # Check length of lines
    max_length = min_width
    for item in menu_list:
        if isinstance(item, tuple):
            new_length = len(item[0])
        else:
            new_length = len(item)
        
        if new_length > max_length:
            max_length = new_length

    # Check if lines are longer than "max_width"
    if max_length > max_width:
        max_length = max_width

    # Check the lenght of every line and split them if too long.

    # Modified function to split the lines
    # the function split_line is now a stand alone library 
    new_list = []

    for item in menu_list:
        
        # Check if item is a tuple, and get values for foreground, and background colours (t_colour, t_background)
        if isinstance(item, tuple):
            parameters = len(item)
            
            """
            If True:
            item[0] is the string.
            item[1] is the colour of the text.
            item[2] is the backgroud colour of the text.
            item[3] is the line alignment.
            """
            
            if item[0] != "":
                words = item[0].split(" ")
            else:
                words = item[0]

            if parameters == 2:
                if str(item[1]).lower() in ("left","center","centre","right"):
                    line_alignment = item[1]
                else:
                    if item[1] != "":
                        t_colour = _valid_colour(item[1])
                    else:
                        t_colour = colour
                    line_alignment = alignment

            elif parameters == 3:
                if item[1] != "":
                    t_colour = _valid_colour(item[1])
                else:
                    t_colour = colour
                if str(item[2]).lower() in ("left","center","centre","right"):
                    line_alignment = item[2]
                else:
                    if item[2] != "":
                        t_background = _valid_colour(item[2], "back")
                    else:
                        t_background = text_background
                    line_alignment = alignment

            else:
                if item[1] != "":
                    t_colour = _valid_colour(item[1])
                else:
                    t_colour = colour
                if item[2] != "":
                    t_background = _valid_colour(item[2], "back")
                else:
                    t_background = text_background
                if str(item[3]).lower() in ("left","center","centre","right"):
                    line_alignment = item[3]
                else:
                    line_alignment = alignment
            
        # If item is not a tuple, default colours are assigned.
        else:
            if item != "":
                words = item.split(" ")
            else:
                words = item
            #words = item.split(" ")
            t_colour = colour
            t_background = text_background
            line_alignment = alignment

        # The function split_line is applied to every element in "menu_list"
        for line in split_line(words, max_length, line_alignment):
            # Then the colours attributes for foreground, and background are applied
            new_list.append((line,t_colour,t_background))

    # Create the frame.
    max_width = max([(len(i[0])) for i in new_list])

    if max_width > (menu_width-(border_space*2)):
        menu_width = max_width + (border_space*2)

    or_line = "═" * menu_width
    filling = " " * menu_width

    # Check the frame positioning.

    if display.lower() == "right":
        positioning = terminal_width - (menu_width+2)
    elif display.lower()=="centre" or display.lower()=="center":
        positioning = int((terminal_width - (menu_width+2)) / 2)
    else:
        positioning = 0
    adjustment = " " * positioning

    # Create the frame
    display_menu = adjustment + f"\033[{frame_background};{frame_colour}m" + "╔" + or_line + "╗" + "\033[0m" + "\n"
   
    for _ in range(round(spacing)):
        display_menu += adjustment + f"\033[{frame_background};{frame_colour}m" + "║" + f"\033[{text_background}m" + filling + f"\033[0m" + f"\033[{frame_background};{frame_colour}m" + "║" +"\033[0m\n"
       
    for item in new_list:
        display_menu += adjustment + f"\033[{frame_background};{frame_colour}m" + "║" + f"\033[{item[2]}m" + side_space + f"\033[{item[1]}m" + item[0] + side_space + f"\033[0m" + f"\033[{frame_background};{frame_colour}m" + "║" +"\033[0m\n"
        
    for _ in range(round(spacing)):
        display_menu += adjustment + f"\033[{frame_background};{frame_colour}m" + "║" + f"\033[{text_background}m" + filling + f"\033[0m" + f"\033[{frame_background};{frame_colour}m" + "║" + "\033[0m\n"
        
    display_menu += adjustment + f"\033[{frame_background};{frame_colour}m" + "╚" + or_line + "╝" + "\033[0m\n"
   
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
    

if __name__ == "__main__":
    main()