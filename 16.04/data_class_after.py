class TaskFigure:
    global possible_figures

    def __init__(self, type, key_symbols, key_symbols_text, possible_symbols, possible_symbols_text):
        self.type = type  # todo rename figure_type
        self.key_symbols = key_symbols
        self.key_symbols_text = key_symbols_text  # для отображения при проверке и других обращениях
        self.possible_symbols = possible_symbols
        self.possible_symbols_text = possible_symbols_text  # для отображения при проверке и других обращениях

    def __str__(self):
        return ('[TaskFigure: type - %s, key symbols - %s, possible symbols from %s to %s]'
                % (self.type, self.key_symbols,
                   self.possible_symbols[0], self.possible_symbols[-1]))

    def check_figure(self, answer_figure):
        if self.type == answer_figure.figure_type:  # Тип
            if (min(self.key_symbols) >= answer_figure.symbols_range[0] and
                    max(self.key_symbols) <= answer_figure.symbols_range[-1]):
                if (self.possible_symbols[0] <= answer_figure.symbols_range[0] and
                        self.possible_symbols[-1] >= answer_figure.symbols_range[-1]):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


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
        for i in self.figures_list:
            n += (str(counter) + " ")
            n += (str(i) + "\n")
            counter += 1
        return n

    def answer_checker(self, answer):
        answer_figures = answer.figures_list[:]
        task_figures = self.figures_list[:]
        correct, not_found = [], []
        for i in range(len(task_figures)):
            current_task_figure = task_figures.pop(0)
            for j in range(len(answer_figures)):
                if answer_figures[j].check_figure(current_task_figure) is True:
                    correct.append(current_task_figure)
                    answer_figures.remove(answer_figures[j])
                    break
            else:
                not_found.append(current_task_figure)
        not_right = answer_figures[:]
        return correct, not_found, not_right
