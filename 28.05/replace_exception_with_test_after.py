def delete_last_figure(self):
    if len(self.figures_list) > 0:
        deleted_figure = self.figures_list.pop()
        start = deleted_figure.symbols_range[0]
        end = deleted_figure.symbols_range[-1] + 1
        repaint_text(start, end)
        self.refresh_figures_to_show()
        self.ui.figures_browser.setText(self.figures_to_show)
    else:
        self.ui.label_chosen_figure_type.setText('Нет оборотов для удаления')


def repaint_text(self, start, end):
    cursor = self.ui.task_text.textCursor()
    cursor.setPosition(start)
    cursor.setPosition(end, QtGui.QTextCursor.KeepAnchor)
    char_format = cursor.charFormat()
    char_format.setBackground(QtCore.Qt.white)
    cursor.setCharFormat(char_format)