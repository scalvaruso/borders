# Borders
## Description:
This module creates a frame around the content of a list.  
It considers any item of the list as a new line.  
The function frame can be also used in place of 'input()'.

### Parameters:

```colour```: accept the following ANSI colour codes ```0, 30, 31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97, 40, 41, 42, 43, 44, 45, 46, 47, 100, 101, 102, 103, 104, 105, 106, 107```, and allows to set the colour of the frame and text.   
default value = ```'white'```  

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

## Usage:
1st - Copy the file borders.py in the same folder where you will be running your main file.  
2nd - Add the following line in your code to import the module:  

```
from borders import frame
```
### Standard use: 'print'
Simply use the function ```frame()``` instead of ```print()``` to print a frame around your output.  
The function accepts only a list of strings as argument, and considers any element as a different line of the output.
```
1    from borders import frame
2
3    output = ["Hello,", "World!"]
4    frame(output)
```
Output:
```
╔══════════════╗
║              ║
║    Hello,    ║
║    World!    ║
║              ║
╚══════════════╝
```  
#### 'spacing'
Specifying a different value for the parameter ```spacing```, you can increase or decrease the space between text and frame.  

With value ```2``` it will leave two blank lines at the top and the bottom, and 8 blank spaces before and after the text.
```
1    from borders import frame
2
3    output = ["Hello,", "World!"]
4    frame(output, spacing=2)
```
Output:
```
╔══════════════════════╗
║                      ║
║                      ║
║        Hello,        ║
║        World!        ║
║                      ║
║                      ║
╚══════════════════════╝
```
With value ```0``` it will create the frame around the text with no spaces.
```
1    from borders import frame
2
3    output = ["Hello,", "World!"]
4    frame(output, spacing=0)
```
Output:
```
╔══════╗
║Hello,║
║World!║
╚══════╝
```
#### 'min_width' and 'max_width'

The parameter ```min_width``` set the minimum width inside the frame.  
With value of ```30``` the output frame will have a wider space on the left.
```
1    from borders import frame
2
3    output = ["Hello,", "World!"]
4    frame(output, min_width=30)
```
Output:
```
╔══════════════════════════════╗
║                              ║
║    Hello,                    ║
║    World!                    ║
║                              ║
╚══════════════════════════════╝
```  
The parameter ```max_width``` set the max length of text on a line.  
Let's see what happens to the following string:
```"There are only 10 kinds of people in this world: Those who know binary and Those who don’t."```, with value ```100```
```
1    from borders import frame
2
3    output = ["There are only 10 kinds of people in this world: Those who know binary and Those who don’t."]
4    frame(output, max_width=100)
```
Output:
```
╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                   ║
║    There are only 10 kinds of people in this world: Those who know binary and Those who don’t.    ║
║                                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝
```
With value ```50```  
```
4    frame(output, max_width=50)
```
Output:
```
╔════════════════════════════════════════════════════════╗
║                                                        ║
║    There are only 10 kinds of people in this world:    ║
║    Those who know binary and Those who don’t.          ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
```
With value ```25```  
```
4    frame(output, max_width=25)
```
Output:
```
╔═════════════════════════════════╗
║                                 ║
║    There are only 10 kinds      ║
║    of people in this world:     ║
║    Those who know binary and    ║
║    Those who don’t.             ║
║                                 ║
╚═════════════════════════════════╝
```
### Alternative use: 'input'
You can use the function ```frame()``` in place of ```input()``` to create a frame around the prompt and get the input from the user.
```
1    from borders import frame
2
3    num1 = int(frame(["Please,", "enter a number"], window="input"))
4    num2 = num1 * 2
5    output = [f"The double of {num1}",f"is {num2}"]
6    frame(output)
```
```
╔═══════════════════════╗
║                       ║
║    Please,            ║
║    enter a number!    ║
║                       ║
╚═══════════════════════╝
6
╔════════════════════════╗
║                        ║
║    The double of 6,    ║
║    is 12               ║
║                        ║
╚════════════════════════╝
```