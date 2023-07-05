#!/usr/bin/python3
"""
Indent the given text.
"""


def text_indentation(text):
    """Print the text with two newlines after each of these chars . ? :.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delim_chars = ['.', '?', ':']
    lines = text.split('\n')
    indented_lines = []

    for line in lines:
        stripped_line = line.strip()

        if stripped_line:
            s = stripped_line.split('. ')
            for i, sentence in enumerate(s):
                indented_lines.append(sentence)
                if i < len(s) - 1 or stripped_line[-1] in delim_chars:
                    indented_lines.append('')

    indented_text = '\n'.join(indented_lines)
    print(indented_text)
