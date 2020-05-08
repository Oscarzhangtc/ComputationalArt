"""
Mini project 2
computational-art

@author: Oscar Zhang
"""

import random
import math
from PIL import Image


def build_random_function(min_depth, max_depth):
    """Build a random function.

    Builds a random function of depth at least min_depth and depth at most
    max_depth. (See the assignment write-up for the definition of depth
    in this context)

    Args:
        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function

    Returns:
        The randomly generated function represented as a nested list.
        (See the assignment write-up for details on the representation of
        these functions
    Doctest is not implemented since the functions generates random value, meaning the specific output is unpredictable
    """
    build_blocks = ["prod","avg","cos_pi","sin_pi","x","y","arctan_pi","circle"]

    if (max_depth <= 0) or (min_depth <=0):
        # checks is depth reaches the basecase
    	random1 = random.randint(0 , 1)
        # generate random integer between 0-1,  the output would just be 1 or 0 since its needs to an int
    	if random1 == 0:
    		return "x"
            # base case, also the 'deepest' value, returns to recurse_blocks
    	elif random1 == 1:
    		return "y"
    else:
    	recurse_blocks = build_random_function(min_depth - 1, max_depth - 1)
        # recursion occurs when  (max_depth <=! 0) & (min_depth <=! 0)

    	random2 = random.randint(0 ,7)
        # generate a random int within the range of the building block every interation of recursion

    	if random2 <= 1:
            # if random2 <=1 it would be prod or avg, we need to return 2 recurse_blocks, to calculate the first and second var in evaluate_random_funtion
    		return [build_blocks[random2], recurse_blocks, recurse_blocks]
            # every interation of recurse_blocks, build_blocks[random2] is a random block and added to the next recurse_blocks
            # the returned value is an array with 3 elements, the first element is a string, the other 2 being the same nested arrays(with more nested array in side depending on depth)
            # returns to recurse_blocks until the recursions ends, then return to the function call
    	if random2 >= 2:
    		return [build_blocks[random2],recurse_blocks]
            # returns to recurse_blocks until the recursions ends, then return to the function call
            # the returned value is an array with 2 elements, the first element is a string, the other 1 being a nested array(with might also have nested arrays depending on the value of depth)


    pass


def evaluate_random_function(f, x, y):
    """Evaluate the random function f with inputs x,y.

    The representation of the function f is defined in the assignment write-up.

    Args:
        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function

    Returns:
        The function value

    Examples:
        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"], 0.1, 0.02)
        0.02
        >>> evaluate_random_function(["circle", "x", "y"], 1, 2)
        5
        >>> evaluate_random_function(["cos_pi", "x"], 1, 3)
        -1.0
        >>> evaluate_random_function(["avg", "x", "y"], 1, 2)
        1.5
        >>> evaluate_random_function(['prod', ['avg', ['avg', 'y','x'],'x'],'y'], 1, 2)
        2.5
    """
    # first base cases:
    # Starting with handling the x,y(bases from build_random_function and function that we can use  x & y to evaluate): evaluate the part of the f that contains x, y,
    # eventually f HAS to contain x, since it is the base case of evaluate_random_function
    if f[0] == "x":
        return x
    elif f[0] == "y":
        return y
    elif f[0] == "circle":
        return x**2 + y**2


    # calls the next element of the f in interation, if the previous element does not contain "x","y", "circle"
    # kinda like a forloop until it finds the base case and evaluate
    first = evaluate_random_function(f[1], x, y)

    # with the result from first, we draft to the second set of "base cases",
    # the folling runs when the x, y  is found,  and the depth starts to decrease
    if f[0] == "cos_pi":
        return math.cos(math.pi * first)
    elif f[0] == "sin_pi":
        return math.sin(math.pi * first)
    elif f[0] == "arctan_pi":
        return math.atan(math.pi * first)

    # same as above, but for prod and avg:
    # we recurse again to calculate value of second element(avg and prod is always followed by 2 recurse_blocks)
    # we calculate 2nd element of the current f interation in order produce "prod" and "avg"
    second = evaluate_random_function(f[2], x, y)

    if f[0] == "prod":
        return first * second
    elif f[0] == "avg":
        return (first + second) / 2

    pass


def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    """Remap a value from one interval to another.

    Given an input value in the interval [input_interval_start,
    input_interval_end], return an output value scaled to fall within
    the output interval [output_interval_start, output_interval_end].

    Args:
        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values

    Returns:
        The value remapped from the input to the output interval

    Examples:
        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """

    input_interval = input_interval_start - input_interval_end
    output_interval = output_interval_start - output_interval_end
    ratio = output_interval / input_interval
    value = val - input_interval_start

    final_output = value * ratio + output_interval_start

    return final_output
    # TODO: implement this
    pass


def color_map(val):
    """Maps input value between -1 and 1 to an integer 0-255, suitable for use as an RGB color code.

    Args:
        val: value to remap, must be a float in the interval [-1, 1]

    Returns:
        An integer in the interval [0,255]

    Examples:
        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide

    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """Generate a test image with random pixels and save as an image file.

    Args:
        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """Generate computational art and save as an image file.

    Args:
        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function(7, 9)
    green_function = build_random_function(7, 9)
    blue_function = build_random_function(7, 9)


    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                color_map(evaluate_random_function(red_function, x, y)),
                # maps and evaluate the fuction returned by build_random_function
                color_map(evaluate_random_function(green_function, x, y)),
                color_map(evaluate_random_function(blue_function, x, y))
            )

    im.save(filename)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    generate_art("myart.png")
