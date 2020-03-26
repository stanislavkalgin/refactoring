# before
def check_figure(self, task_figure):
    if task_figure.type == self.figure_type:  # Тип
        if (min(task_figure.key_symbols) >= self.symbols_range[0] and
                max(task_figure.key_symbols) <= self.symbols_range[-1]):
            if (task_figure.possible_symbols[0] <= self.symbols_range[0] and
                    task_figure.possible_symbols[-1] >= self.symbols_range[-1]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


#after
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def check_figure(self, task_figure):
    if task_figure.type == self.figure_type:  # Тип

        if (task_figure.key_symbols.start >= self.symbols_range.start and
                task_figure.key_symbols.end <= self.symbols_range.end):

            if (task_figure.possible_symbols.start <= self.symbols_range.start and
                    task_figure.possible_symbols.end >= self.symbols_range.end):
                return True
            else:
                return False
        else:
            return False
    else:
        return False