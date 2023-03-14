# Borders

## Description

This module creates a frame when printing a list of strings.  
It considers any item of the list as a new line.  
The function frame can be also used in place of 'input()'.

### Parameters

```colour```: accept the following ANSI colour codes ```0, 30, 31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97```, and allows to set the colour of the text.
default value = ```37```  

```text_background```: accept the following ANSI colour codes ```0, 40, 41, 42, 43, 44, 45, 46, 47, 100, 101, 102, 103, 104, 105, 106, 107```, and allows to set the backgroud colour of the text.
default value = ```0```  

```frame_colour```: accept the following ANSI colour codes ```0, 30, 31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97```, and allows to set the colour of the frame.
default value = ```37```  

```frame_background```: accept the following ANSI colour codes ```0, 40, 41, 42, 43, 44, 45, 46, 47, 100, 101, 102, 103, 104, 105, 106, 107```, and allows to set the backgroud colour of the frame.
default value = ```0```

```spacing```: allows to set the space between the frame and the text.  
default value = ```1``` (vertical space = 1 line, horizontal space = 4 spaces)  

```min_width```: allows to set the minimum width inside the frame.  
default value = ```8```  

```max_width```: allows to set the max length of text on a line.  
default value = ```70```  

```window```: allows the function to behave as input.  
default value = ```'print'```

### Returns

Prints a frame around the output or around the input prompt.

## Usage

Add the following line in your code to import the module:  

```python
from borders import frame
```

### Standard use: 'print'

Simply use the function ```frame()``` instead of ```print()``` to print a frame around your output.  

The function accepts only lists of strings, tuples, or mix of them, and considers any element as a different line of the output.
Tuple accepted must contain a string and one or two numeric value: the string is what has to be printed, the numeric values are the values for the colour of the text and its background.

```python
from borders import frame

output = ["Hello,", "World!"]
frame(output)
```

Output:

![borders01](https://raw.githubusercontent.com/scalvaruso/borders/main/png/borders01.png)

We can set a colour for the text (e.g. 34 for Blue) and one for the frame (e.g. 31 for Red)

```python
from borders import frame

output = ["Hello,", "World!"]
frame(output, colour="34", frame_colour="31")
```

Output:

![borders02](https://raw.githubusercontent.com/scalvaruso/borders/main/png/borders02.png)

Using a ```Tuple``` we can set different colours for each line, we can set blue as general colour for the text, then we can set one line yellow, one green, and highlight one in white

```python
from borders import frame

output = [
    "Hello,",
    "World!",
    ("This line is yellow", 33),
    ("This line is green", 32),
    ("This line is highlighted in white","",47),
    "This line is back to the general colour"
    ]
frame(output, colour="34", frame_colour="31")
```

Output:

![borders02b](https://raw.githubusercontent.com/scalvaruso/borders/main/png/borders02b.png)

#### 'spacing'

Specifying a different value for the parameter ```spacing```, you can increase or decrease the space between text and frame.  

With value ```2``` it will leave two blank lines at the top and the bottom, and 8 blank spaces before and after the text.

```python
from borders import frame  

output = ["Hello,", "World!"]
frame(output, spacing=2)
```

Output:

![borders03](https://raw.githubusercontent.com/scalvaruso/borders/main/png/borders03.png)

With value ```0``` it will create the frame around the text with no spaces.

```python
from borders import frame  
  
output = ["Hello,", "World!"]
frame(output, spacing=0)
```

Output:

![borders04](https://raw.githubusercontent.com/scalvaruso/borders/main/png/borders04.png)

#### 'min_width' and 'max_width'

The parameter ```min_width``` set the minimum width inside the frame.  
For example with value of ```30``` the output frame will have a wider space on the left.

```python
from borders import frame  

output = ["Hello,", "World!"]
frame(output, min_width=30)
```

Output:

![borders05](https://raw.githubusercontent.com/scalvaruso/borders/main/png/borders05.png)  

The parameter ```max_width``` set the max length of text on a line.  
Let's see what happens to the following string:
```"There are only 10 kinds of people in this world: Those who know binary and Those who don’t."```, with value ```100```

```python
from borders import frame  

output = ["There are only 10 kinds of people in this world: Those who know binary and Those who don't."]
frame(output, max_width=100)
```

Output:

![borders06](https://raw.githubusercontent.com/scalvaruso/borders/main/png/borders06.png)

With value ```50```  

```python
from borders import frame  

output = ["There are only 10 kinds of people in this world: Those who know binary and Those who don't."]
frame(output, max_width=50)
```

Output:

![borders07](https://raw.githubusercontent.com/scalvaruso/borders/main/png/borders07.png)

With value ```25```  

```python
from borders import frame

output = ["There are only 10 kinds of people in this world: Those who know binary and Those who don't."]
frame(output, max_width=25)
```

Output:

![borders08](https://raw.githubusercontent.com/scalvaruso/borders/main/png/borders08.png)

### Alternative use: 'input'

You can use the function ```frame()``` in place of ```input()``` to create a frame around the prompt and get the input from the user.

```python
from borders import frame
 
num1 = int(frame(["Please,", "enter a number"], window="input"))
num2 = num1 * 2
output = [f"The double of {num1}",f"is {num2}"]
frame(output)
```

Output:

![borders09](https://raw.githubusercontent.com/scalvaruso/borders/main/png/borders09.png)
