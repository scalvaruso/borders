import os
from textlinebreaker import split_line
from polychromy import colorate


def _demo():

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
        "one or two values (integers or strings) for foreground and background colors of the text,",
        "one string value for the alignment of the line."
        ]
    menu_2 = [
        ("Parameters:","","Bright Red","centre"),"",
        ("colour:","Bright Red","centre"), "allows to change the color of the text.",
        "default value = 37",
        "allowed values: most color names",
        "RGB values [0-255];[0-255];[0-255]",
        "Hex values #[00-FF][00-FF][00-FF]",
        "xterm color number in the format x[0-255]",
        "and ANSI codes 0, [30-37], [90-97]",
        ("text_background:","Bright Red","centre"), "allows to change the background color of the text.",
        "default value = 0",
        "allowed values: most color names",
        "RGB values [0-255];[0-255];[0-255]",
        "Hex values #[00-FF][00-FF][00-FF]",
        "xterm color number in the format x[0-255]",
        "and ANSI codes 0, [40-47], [100-107]",
        ("frame_colour:","Bright Red","centre"), "allows to change the color of the frame.",
        "default value = None",("(if not specified get the same color value of the text)","right"),
        "allowed values: most color names",
        "RGB values [0-255];[0-255];[0-255]",
        "Hex values #[00-FF][00-FF][00-FF]",
        "xterm color number in the format x[0-255]",
        "and ANSI codes 0, [30-37], [90-97]",
        ("frame_background:","Bright Red","centre"), "allows to change the background color of the frame.",
        "default value = None",("(if not specified get the same value of text_background).","right"),
        "allowed values: most color names",
        "RGB values [0-255];[0-255];[0-255]",
        "Hex values #[00-FF][00-FF][00-FF]",
        "xterm color number in the format x[0-255]",
        "and ANSI codes 0, [40-47], [100-107]",
        ("frame_style:","Bright Red","centre"), "allows to change the style of the frame",
        "default value = 'double'",
        "allowed values: 'single', 'double', 'double horizontal', 'double vertical', 'dots', None",
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


# Importable function.
def frame(menu_list, colour=37, text_background=0, frame_colour=None, frame_background=None, frame_style="double", alignment="left", display="left", spacing=1, min_width=42, max_width=70, window="print"):
    """
    This function create a frame around the content of a list.
    Any item of the list is considered a new line.
    Items allowed are strings or tuples containing:
    a string with text to print,
    one or two values (integers or strings) for foreground and background colors of the text,
    one string value for the alignment of the line.
    
    Parameters:
        colour: allows to change the color of the text.
            default value = 37
            allowed values: "allowed values: most color names"
                            "RGB values [0-255];[0-255];[0-255]"
                            "Hex values #[00-FF][00-FF][00-FF]"
                            "xterm color number in the format x[0-255]"
                            "and ANSI codes 0, [30-37], [90-97]"
        text_background: allows to change the background color of the text.
            default value = 0
            allowed values: "allowed values: most color names,"
                            "RGB values [0-255];[0-255];[0-255],"
                            "Hex values #[00-FF][00-FF][00-FF],"
                            "xterm color number in the format x[0-255],"
                            "and ANSI codes 0, [40-47], [100-107]."
        frame_colour: allows to change the color of the frame.
            default value = None (if not specified get the same color value of the text).
            allowed values: "allowed values: most color names"
                            "RGB values [0-255];[0-255];[0-255]"
                            "Hex values #[00-FF][00-FF][00-FF]"
                            "xterm color number in the format x[0-255]"
                            "and ANSI codes 0, [30-37], [90-97]"
        frame_background: allows to change the background color of the frame.
            default value = None (if not specified get the same value of text_background).
            allowed values: "allowed values: most color names,"
                            "RGB values [0-255];[0-255];[0-255],"
                            "Hex values #[00-FF][00-FF][00-FF],"
                            "xterm color number in the format x[0-255],"
                            "and ANSI codes 0, [40-47], [100-107]."
        frame_style: allows to change the style of the frame
            default value = "double"
            allowed values: "single", "double", "double horizontal", "double vertical", "dots", None
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
    # Set generic colors for the frame and text elements.
    color = colour
    
    if frame_colour:
        frame_color = frame_colour
    else:
        frame_color = color

    if frame_background:
        pass
    else:
        frame_background = text_background

    t_color = color
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
    if isinstance(menu_list, list):
        for item in menu_list:
            if isinstance(item, tuple):
                new_length = len(item[0])
            else:
                new_length = len(item)
            
            if new_length > max_length:
                max_length = new_length
    else:
        new_length = len(menu_list)
        if new_length > max_length:
                max_length = new_length

    # Check if lines are longer than "max_width"
    if max_length > max_width:
        max_length = max_width

    # Modify input text to fit in the frame.
    new_list = []

    if isinstance(menu_list, list):

        for item in menu_list:
            
            words, t_color, t_background, line_alignment = _get_settings(item, color, text_background, alignment)

            # The function split_line is applied to every element in "menu_list"
            for line in split_line(words, max_length, line_alignment):
                # Then the colors attributes for foreground, and background are applied
                new_list.append((line,t_color,t_background))
    
    else:
        # The function split_line is applied directly to "menu_list"
        for line in split_line(menu_list, max_length, line_alignment):
            # Then the colors attributes for foreground, and background are applied
            new_list.append((line,t_color,t_background))

    # Create the frame. <--Continue from this point-->
    max_width = max([(len(i[0])) for i in new_list])

    if max_width > (menu_width-(border_space*2)):
        menu_width = max_width + (border_space*2)

    # Defining the elements of the frame:
    # Top Left Corner, Horizontal line (single element), Top Right Corner, Vertical line, Bottom Left Corner, Bottom Right Corner.
    tl_corner, h_line, tr_corner, v_line, bl_corner, br_corner = _elements(frame_style)
    # Horizontal Line (Full length)
    hor_line = h_line * menu_width
    # Empty line
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
    display_menu = adjustment + colorate(tl_corner + hor_line + tr_corner, frame_color, frame_background) + "\n"
   
    for _ in range(round(spacing)):
        display_menu += adjustment + colorate(v_line, frame_color, frame_background) + colorate(filling, 0, text_background) + colorate(v_line, frame_color, frame_background) + "\n"
       
    for item in new_list:
        display_menu += adjustment + colorate(v_line, frame_color, frame_background) + colorate(side_space+ item[0] + side_space, item[1], item[2]) + colorate(v_line, frame_color, frame_background) +"\n"
        
    for _ in range(round(spacing)):
        display_menu += adjustment + colorate(v_line, frame_color, frame_background) + colorate(filling, 0, text_background) + colorate(v_line, frame_color, frame_background) + "\n"
        
    display_menu += adjustment + colorate(bl_corner + hor_line + br_corner, frame_color, frame_background) + "\n"
   
    # Change the behaviour of the function from 'print' to 'input'.
    if window=="in" or window=="input":
        return input(display_menu)
    else:
        print(display_menu)


# Defining the elements of the frame
def _elements(style):
    # According to the given style value, the function returns:
    # Top Left Corner, Horizontal line (single element), Top Right Corner, Vertical line, Bottom Left Corner, Bottom Right Corner.

    if style == "single":
        return "┌", "─", "┐", "│", "└", "┘" # tl_corner, h_line, tr_corner, v_line, bl_corner, br_corner

    elif style == "double horizontal":
        return "╒", "═", "╕", "│", "╘", "╛" # tl_corner, h_line, tr_corner, v_line, bl_corner, br_corner
   
    elif style == "double vertical":
        return "╓", "─", "╖", "║", "╙", "╜" # tl_corner, h_line, tr_corner, v_line, bl_corner, br_corner

    elif style == "double":
        return "╔", "═", "╗", "║", "╚", "╝" # tl_corner, h_line, tr_corner, v_line, bl_corner, br_corner
    
    elif style == "dots":
        return "·", "·", "·", ":", "·", "·" # tl_corner, h_line, tr_corner, v_line, bl_corner, br_corner

    else:
        return (6 * " ")    # tl_corner, h_line, tr_corner, v_line, bl_corner, br_corner


# This function return list of words of the given string and their color and alignment.
def _get_settings(item, color, text_background, alignment):

    # Check if item is a tuple, and get values for foreground, background colors, and alignment (t_color, t_background, line_alignment).
    if isinstance(item, tuple):
        parameters = len(item)
        
        """
        If True:
        item[0] is the string.
        item[1] can be the color of the text or line alignment.
        item[2] is optional and could be the backgroud color or line alignment.
        item[3] is optional and is the line alignment.
        """
        
        if item[0] != "":
            words = item[0].split(" ")
        else:
            words = item[0]

        if parameters == 2:
            # Check if first item after string is the text color or the alignment.
            if str(item[1]).lower() in ("left","center","centre","right"):
                line_alignment = item[1]
                t_color = color
            else:
                if item[1] != "":
                    t_color = item[1]
                else:
                    t_color = color
                line_alignment = alignment
            t_background = text_background

        elif parameters == 3:
            # Get text color from item[1].
            if item[1] != "":
                t_color = item[1]
            else:
                t_color = color
            # Check if second item after string is the background color or the alignment.
            if str(item[2]).lower() in ("left","center","centre","right"):
                line_alignment = item[2]
                t_background = text_background
            else:
                if item[2] != "":
                    t_background = item[2]
                else:
                    t_background = text_background
                line_alignment = alignment

        else:
            # Get text color from item[1].
            if item[1] != "":
                t_color = item[1]
            else:
                t_color = color
            # Get background color from item[2].
            if item[2] != "":
                t_background = item[2]
            else:
                t_background = text_background
            # Get alignment from item[3].
            if str(item[3]).lower() in ("left","center","centre","right"):
                line_alignment = item[3]
            else:
                line_alignment = alignment
        
    # If item is not a tuple, default colors are assigned to the lines.
    else:
        if item != "":
            words = item.split(" ")
        else:
            words = item

        t_color = color
        t_background = text_background
        line_alignment = alignment

    return words, t_color, t_background, line_alignment


if __name__ == "__main__":
    _demo()