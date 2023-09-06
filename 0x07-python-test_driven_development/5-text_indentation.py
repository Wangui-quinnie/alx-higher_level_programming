"""Defines a function that prints 2 new lines after:., ? and :."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':',.

    Args:
        text (str):The input text to format.
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    inside_paragraph = False

    for char in text:
        if char in [".", "?", ":"]:
            result += char + "\n\n"
            inside_paragraph = False
        elif char == " " and not inside_paragraph:
            continue
        else:
            result += char
            inside_paragraph = True

    print(result)
