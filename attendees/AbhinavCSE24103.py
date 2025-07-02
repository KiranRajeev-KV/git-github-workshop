def print_big_text(text):
    # Simple block letter representation for each character
    letters = {
        'A': ["  ***  ",
              " *   * ",
              "*     *",
              "*******",
              "*     *",
              "*     *"],
        'B': ["****** ",
              "*     *",
              "****** ",
              "*     *",
              "*     *",
              "****** "],
        'H': ["*     *",
              "*     *",
              "*******",
              "*     *",
              "*     *",
              "*     *"],
        'I': [" ***** ",
              "   *   ",
              "   *   ",
              "   *   ",
              "   *   ",
              " ***** "],
        'N': ["*     *",
              "**    *",
              "* *   *",
              "*  *  *",
              "*   ** ",
              "*    * "],
        'V': ["*     *",
              "*     *",
              " *   * ",
              " *   * ",
              "  * *  ",
              "   *   "],
        'R': ["****** ",
              "*     *",
              "****** ",
              "*   *  ",
              "*    * ",
              "*     *"],
        'G': [" ***** ",
              "*      ",
              "*  ****",
              "*     *",
              "*     *",
              " ***** "],
        'E': ["*******",
              "*      ",
              "****** ",
              "*      ",
              "*      ",
              "*******"],
        'D': ["****** ",
              "*     *",
              "*     *",
              "*     *",
              "*     *",
              "****** "],
        ' ': ["   ",
              "   ",
              "   ",
              "   ",
              "   ",
              "   "],
        '*': ["   *   ",
              "  ***  ",
              "*******",
              "  ***  ",
              "   *   ",
              "       "]
    }

    text = text.upper()
    lines = [""] * 6
    for char in text:
        if char in letters:
            for i in range(6):
                lines[i] += letters[char] [i] + "  "
        else:
            for i in range(6):
                lines[i] += "       "  # Space for unknown chars

    for line in lines:
        print(line.replace(' ', '*'))

print_big_text("ABHINAV RAGHAVENDRA*")