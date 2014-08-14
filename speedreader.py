import sys
from drawingpanel import *

class WordGenerator:

    def __init__(self, filename):
        with open(filename) as f:
            lines = [line.strip() for line in f.readlines()]
            self.words = []
            for line in lines:
                self.words.extend(line.split())
            self.pos = 0
            self.state = False

    def is_empty(self):
        return self.pos >= len(self.words)

    def next_word(self):
        ans = self.words[self.pos]
        self.pos += 1
        return ans

    def in_quotes(self,word):
        if ("\"" in word):
            self.state = not self.state

        

def animate_text(gen, width, height, size, delay):
    panel = DrawingPanel(width, height)
    canvas = panel.canvas
    panel.set_background("Beige")


    while not (gen.is_empty()):
        word = gen.next_word()
        canvas.create_rectangle(0,0, width, height, fill = "Beige")
        canvas.create_line(width/2, 0, width/2, 150)
        canvas.create_line(width/2, height, width/2, height - 150)
        letter = ""
        
        if (len(word) <= 1):
            letter = word[0]
        elif (len(word) == 2):
            letter = word[1]
            word = word + " "
        elif (len(word) <= 5):
            spaces = " " * (len(word) - 3)
            letter = word[1]
            word = spaces + word
        elif (len(word) <= 9):
            spaces = " " * (len(word) - 5)
            letter = word[2]
            word = spaces + word
        elif (len(word) <= 13):
            spaces = " " * (len(word) - 7)
            letter = word[3]
            word = spaces + word
        else:
            spaces = " " * (len(word) - 9)
            letter = word[4]
            word = spaces + word

        gen.in_quotes(word)

        if gen.state or "\"" in word:
            canvas.create_text(width/2, height/2, text=word, font=("Courier", size*2))
            canvas.create_text(width/2, height/2, text=letter, font=("Courier", size*2), fill="red")
        else:
            canvas.create_text(width/2, height/2, text=word, font=("Courier", size))
            canvas.create_text(width/2, height/2, text=letter, font=("Courier", size), fill="red")

        if ("." in word) or ("?" in word) or ("!" in word) or (":" in word) or (";" in word):
            panel.sleep(1.3 * delay)
        else:
            panel.sleep(delay)


def main(args):
    gen = WordGenerator(args[1])
    animate_text(gen, 800, 400, 40, float(args[2]))

if __name__ == "__main__":
    main(sys.argv)