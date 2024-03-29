# Borders

[<img src="https://img.shields.io/badge/borders-py-blue?style=flat&logo=python&logoWidth=20.svg/"></a>](https://github.com/scalvaruso/borders/)
[![PyPI - Version](https://img.shields.io/pypi/v/borders?logo=pypi&logoColor=white&color=blue)](https://pypi.org/project/borders/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/borders?logo=python)](https://pypi.org/project/borders/)
[![Downloads](https://static.pepy.tech/badge/borders)](https://pepy.tech/project/borders)
[![PyPI - License](https://img.shields.io/pypi/l/borders?color=blue)](https://github.com/scalvaruso/borders/blob/main/LICENSE.md)

<!---
[![PyPI - status](https://img.shields.io/pypi/status/:borders)](https://pypi.org/project/borders/)
[![Documentation Status](https://readthedocs.org/projects/borders/badge/?version=latest)](https://borders.readthedocs.io/en/latest/?badge=latest)
-->

## Description

[![PyPI - Version](https://img.shields.io/pypi/v/borders?label=Borders&labelColor=white&color=white&style=flat-square)](#borders) is an updated version of **borders**: it enhances the functionality of creating frames around text output adding new features, and improving existing ones. Borders creates a frame around a string or a list of strings where any item is considered a new line.

## Features

* [Input Functionality](#input): Provides an option to use the `frame()` function in place of `input()` to create a framed prompt for user input.
* [Spacing Control](#alignment): Customisable alignment for the frame and the text within the frame.
* [Width Customization](#minimum-width):** Customisable width of frame and text lines.

## Latest Version 1.2.0

* **Now supporting single string input.**
* [Colour Support](#text-and-frame-colours): Expanded colour options now accept most color names, ***sRGB*** values **[0-255];[0-255];[0-255]**, ***Hex*** values **#[00-FF][00-FF][00-FF]**, ***xterm*** color number in the format **x[0-255]**, and ***ANSI codes* 0, [40-47], [100-107]**.
* [Frame styles](#frame-style): Six different frame styles now available.

## Table of Contents

* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Parameters](#parameters)
  * [Examples](#examples)
    * [Default settings](#default-settings)
    * [Text and Frame Colours](#text-and-frame-colours)
    * [Tuples](#tuples)
    * [Alignment](#alignment)
    * [Display](#display)
    * [Spacing](#spacing)
    * [Minimum Width](#minimum-width)
    * [Maximum Width](#maximum-width)
    * [Input](#input)
* [Contributing](#contributing)
* [License](#license)

## Getting Started

### Prerequisites

Borders relies on the Python standard library, [textlinebreaker](https://pypi.org/project/textlinebreaker/) and [polychromy](https://pypi.org/project/polychromy/) libraries, and if your system is ```Windows``` in addition it might require```colorama``` to fix color compatibility.

### Installation

* Install the package

```bash
    pip install borders
```

* or upgrade it to the latest version

```bash
    pip install --upgrade borders
```

* Import the package in your program

```python
  from borders import frame
```

## Usage

Add the following line in your code to import the module

```python
from borders import frame
```

Simply use the function ```frame()``` instead of ```print()``` to print a frame around your output.  
Alternatively set the parameter ```window = "input"``` to use ```frame()``` in place of ```input()```.

The text to be printed can be a mixed list of:

* strings
* tuples containing a string with the text to print and at least one of the following parameters:
  * Optional value (integers or strings) for the colour of the text
  * Optional value (integers or strings) for the background colour of the text
  * Optional value (string) for the alignment of the line

### Parameters

* [colour](#text-and-frame-colours): set the text colour.  
  * allowed values: most color names, RGB values [0-255];[0-255];[0-255], Hex values #[00-FF][00-FF][00-FF], xterm color number in the format x[0-255], and ANSI codes 0, [30-37], [90-97].
  * default value = `37`.  
* [text_background](#text-and-frame-colours): set the background colour of the text.  
  * allowed values: most color names, RGB values [0-255];[0-255];[0-255], Hex values #[00-FF][00-FF][00-FF], xterm color number in the format x[0-255], and ANSI codes 0, [40-47], [100-107].
  * default value = `0`.  
* [frame_colour](#text-and-frame-colours): set the frame colour.  
  * allowed values: most color names, RGB values [0-255];[0-255];[0-255], Hex values #[00-FF][00-FF][00-FF], xterm color number in the format x[0-255], and ANSI codes 0, [30-37], [90-97].
  * default value = `37`.  
* [frame_background](#text-and-frame-colours): set the background colour of the frame.  
  * allowed values: most color names, RGB values [0-255];[0-255];[0-255], Hex values #[00-FF][00-FF][00-FF], xterm color number in the format x[0-255], and ANSI codes 0, [40-47], [100-107].
  * default value = `0`.  
* [frame_style](#frame-style): allows to change the style of the frame
  * allowed values: ```'single'```, ```'double'```, ```'double horizontal'```, ```'double vertical'```, ```'dots'```, ```None```  
  * default value = ```'double'```  
* [alignment](#alignment): set the alignment of the text inside the frame.  
  * allowed values: ```'left'```, ```'centre'```, ```'center'```, ```'right'```  
  * default value = ```'left'```  
* [display](#display): set the position of the frame inside the terminal.  
  * allowed values: ```'left'```, ```'centre'```, ```'center'```, ```'right'```  
  * default value = ```'left'```  
* [spacing](#spacing): set the space between the frame and the text.  
  * allowed values: from `0 to 3`  
  * default value = `1`  
* [min_width](#minimum-width): set the min length of text in a line.  
  * allowed values: integers above `8`, ```'max'```(this value assign to the frame the width of the terminal)  
  * default value = `42`  
* [max_width](#maximum-width): set the max length of text in a line.  
  * allowed values: integers above `8`, ```'max'```(this value assign to the frame the width of the terminal)  
  * default value = `70`  
* [window](#input): Set the behaviour of the function, to output or input.  
  * allowed values: ```'print'```, ```'input'```  
  * default value = ```'print'```  

### Examples

Here are some examples of how to use the frame() function with different parameters.

<!--- Example 01 --->
#### Default settings

Simply using ```frame()``` will print a frame around a given output.

```python
from borders import frame

# Example 1: Default settings
output = ["Hello,", "World!"]
frame(output)
```

##### Output 1

![example01](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example01.png)

<!--- Example 02 --->
#### Text and Frame Colours

We can set a colour for the text (e.g. 34 for Blue) and one for the frame (e.g. 31 for Red)

```python
from borders import frame

# Example 2: Setting text and frame colours
output = ["Hello,", "World!"]
frame(output, colour="34", frame_colour="31")
```

##### Output 2

![example02](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example02.png)

<!--- Example 03 --->
#### Tuples

Using a **tuple** we can set different colours for each line, let's try setting blue, and red as general colours for the text and the frame.  
Then let's set one line with yellow text, one with green, and highlight one in white.

```python
from borders import frame

# Example 3: Using tuple to set different colours for each line
output = [
    "This text's color is Blue (System Color)",
    ("This text's color is Aquamarine", "Aquamarine"),
    ("This text's color is Coral","255;127;80"),
    ("This text's color is Cosmic Latte","#FFF8E7"),
    ("This text is highlighted in Yellow", "", "x226"),
    ("Frame's color is Red (System Color)", 31),
    "This text's color is back to Blue (System Color)"
]

frame(output, colour=34, frame_colour=31)
```

##### Output 3

![example03](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example03.png)

<!--- Example 04 --->
#### Frame Style

```python
from borders import frame

# Example 4: Setting a different styles for the frame
styles = ["single", "double", "double horizontal", "double vertical", "dots", None]

for s in styles:
    # Print out the name of the style in a frame of that style.
    frame(f"{s}", frame_colour="Red", frame_background="Gainsboro", alignment="centre", frame_style=s)
```

##### Output 4

![example04](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example04.png)

<!--- Example 05 --->
#### Alignment

The parameter```alignment```allows you to change the alignment of the text inside the frame.  
With```alignment="right"```will allign the text to the right of the frame.

```python
from borders import frame

# Example 5: Setting lines width equal to 60,
# the general alignment of the text to the right,
# and the alignment of the second line to the left
output = ["There are only 10 kinds of people in this world:", ("Those who know binary and Those who don't.","left"), "Anonymous"]
frame(output, min_width=60, alignment="right")
```

##### Output 5

![example05](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example05.png)

<!--- Example 06 --->
#### Display

The parameter```display``` allows you to change the position of the frame inside the terminal.

```python
from borders import frame

# Example 6: Setting the position of the frame in the centre of the terminal
# and the alignment of the text to the right 
output = ["There are only 10 kinds of people in this world:", "Those who know binary and Those who don't.", "Anonymous"]
frame(output, alignment="right", display="centre")
```

##### Output 6

![example06](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example06.png)

#### Spacing

Specifying different values for the parameter```spacing```, you can increase or decrease the space between text and frame.  

<!--- Example 07 --->
##### spacing=2

With```spacing=2```it will leave **2** blank lines at the top and the bottom, and **8** blank spaces before and after the text.

```python
from borders import frame  

# Example 7: Setting the spacing between the text and the frame equal to 2
output = ["Hello,", "World!"]
frame(output, spacing=2)
```

##### Output 7

![example07](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example07.png)

<!--- Example 08 --->
##### Spacing = 0

With```spacing=0```it will create the frame around the text with no spaces.

```python
from borders import frame  

# Example 8: Setting the spacing between the text and the frame equal to 0
output = ["Hello,", "World!"]
frame(output, spacing=0)
```

##### Output 8

![example08](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example08.png)

<!--- Example 09 --->
#### Minimum Width

The parameter ```min_width``` set the minimum width inside the frame.  
With```min_width=30```the output frame will have a wider space on the left.

```python
from borders import frame  

# Example 9:
output = ["Hello,", "World!"]
frame(output, min_width=30)
```

##### Output 9

![example09](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example09.png)  

#### Maximum Width

The parameter ```max_width``` set the max length of text on a line.  
Let's see what happens to the following string: *"There are only 10 kinds of people in this world: Those who know binary and Those who don’t."*

<!--- Example 10 --->
##### max_width=100

```python
from borders import frame  

# Example 10:
output = ["There are only 10 kinds of people in this world: Those who know binary and Those who don't."]
frame(output, max_width=100)
```

##### Output 10

![example10](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example10.png)

<!--- Example 11 --->
##### max_width=50

```python
from borders import frame  

# Example 11:
output = ["There are only 10 kinds of people in this world: Those who know binary and Those who don't."]
frame(output, max_width=50)
```

##### Output 11

![example11](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example11.png)

<!--- Example 12 --->
##### max_width=25

```python
from borders import frame

# Example 12:
output = ["There are only 10 kinds of people in this world: Those who know binary and Those who don't."]
frame(output, max_width=25)
```

##### Output 12

![example12](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example12.png)

<!--- Example 13 --->
#### Input

You can use the function ```frame()``` in place of ```input()``` to create a frame around the prompt and get the input from the user.

```python
from borders import frame

# Example 13: Using frame() in place of input()
num1 = int(frame(["Please,", "enter a number"], window="input"))
num2 = num1 * 2
output = [f"The double of {num1}",f"is {num2}"]
frame(output)
```

##### Output 13

![example13](https://raw.githubusercontent.com/scalvaruso/borders/main/images/example13.png)

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Clone the fork to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them.
5. Push the changes to your fork on GitHub.
6. Create a pull request to the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/scalvaruso/borders/blob/main/LICENSE.md) file for details.
