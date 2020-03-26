# before
class Task:
    global possible_figures

    def __init__(self, name, text, highlighted_text, figures_list):
        self.name = name
        self.text = text
        self.highlighted_text = highlighted_text
        self.figures_list = figures_list

    def __str__(self):
        n = (self.name + "\n")
        n += self.text + "\n"
        counter = 1
        for i in self.figures_list:
            n += (str(counter) + " ")
            n += (str(i) + "\n")
            counter += 1
        return n

    def add_figure(self, type, key_symbols, key_symbols_text, possible_symbols, possible_symbols_text):
        figure = dict()
        figure[type] = type
        figure[key_symbols] = key_symbols
        figure[key_symbols_text] = key_symbols_text  # для отображения при проверке и других обращениях
        figure[possible_symbols] = possible_symbols
        figure[possible_symbols_text] = possible_symbols_text
        self.figures_list(figure)


# after
class TaskFigure:
    global possible_figures

    def __init__(self, type, key_symbols, key_symbols_text, possible_symbols, possible_symbols_text):
        self.type = type
        self.key_symbols = key_symbols
        self.key_symbols_text = key_symbols_text  # для отображения при проверке и других обращениях
        self.possible_symbols = possible_symbols
        self.possible_symbols_text = possible_symbols_text  # для отображения при проверке и других обращениях

    def __str__(self):
        return ('[TaskFigure: type - %s, key symbols - %s, possible symbols from %s to %s]'
                % (self.type, self.key_symbols,
                   self.possible_symbols[0], self.possible_symbols[-1]))


class Task:
    def __init__(self, name, text, highlighted_text, figures_list):
        self.name = name
        self.text = text
        self.highlighted_text = highlighted_text
        self.figures_list = figures_list

    def __str__(self):
        n = (self.name + "\n")
        n += self.text + "\n"
        counter = 1
        for i in self.figuresList:
            n += (str(counter) + " ")
            n += (str(i) + "\n")
            counter += 1
        return n