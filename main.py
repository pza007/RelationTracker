from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from ui.main_window import Ui_MainWindow
from ui.single_relation import Ui_Form
from functions import *


# TODO: Pop-Up when closing MainWindow: do you want to save?
# TODO: Create plot for 10 "most changing relations", based on values from Sheets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.dbc = Database.get_instance()

        # main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # relation_window
        self.relation_window = RelationWindow(self)

        # in_name1
        completer = QtWidgets.QCompleter(self.dbc.names)
        completer.setCompletionMode(QtWidgets.QCompleter.CompletionMode.PopupCompletion)
        completer.setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
        self.ui.in_name1.setCompleter(completer)
        self.ui.in_name1.setToolTip('\n'.join(self.dbc.names))
        # in_name2
        self.ui.in_name2.setCompleter(completer)
        self.ui.in_name2.setToolTip('\n'.join(self.dbc.names))

        # out_names1
        self.ui.out_names1.addItems(self.dbc.names)
        # out_names2
        self.ui.out_names2.addItems(self.dbc.names)

        # table
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        self.link_objects()

    def link_objects(self):
        # update_out_names 1
        self.ui.cb_location1.activated.connect(lambda: self.update_out_names('cb_location1'))
        self.ui.cb_group1.activated.connect(lambda: self.update_out_names("cb_group1"))
        self.ui.cb_name1.activated.connect(lambda: self.update_out_names("cb_name1"))
        # update_out_names 2
        self.ui.cb_location2.activated.connect(lambda: self.update_out_names('cb_location2'))
        self.ui.cb_group2.activated.connect(lambda: self.update_out_names("cb_group2"))
        self.ui.cb_name2.activated.connect(lambda: self.update_out_names("cb_name2"))

        # _showPopup 1
        self.ui.cb_location1.showPopup = lambda: self._showPopup("cb_location1")
        self.ui.cb_group1.showPopup = lambda: self._showPopup("cb_group1")
        self.ui.cb_name1.showPopup = lambda: self._showPopup("cb_name1")
        # _showPopup 2
        self.ui.cb_location2.showPopup = lambda: self._showPopup("cb_location2")
        self.ui.cb_group2.showPopup = lambda: self._showPopup("cb_group2")
        self.ui.cb_name2.showPopup = lambda: self._showPopup("cb_name2")

        # add_to_qlist 1
        self.ui.in_name1.returnPressed.connect(lambda: self.add_to_qlist("in_name1"))
        # add_to_qlist 2
        self.ui.in_name2.returnPressed.connect(lambda: self.add_to_qlist("in_name2"))

        # remove_from_qlist 1
        self.ui.out_characters1.doubleClicked.connect(self.remove_from_qlist)
        # remove_from_qlist 2
        self.ui.out_characters2.doubleClicked.connect(self.remove_from_qlist)

        # buttons 1
        self.ui.b_clear_inputs1.clicked.connect(lambda: self.clear_inputs("b_clear_inputs1"))
        self.ui.b_clear_out_names1.clicked.connect(lambda: self.ui.out_names1.clear())
        self.ui.b_clear_out_characters1.clicked.connect(lambda: self.ui.out_characters1.clear())
        self.ui.b_shift1.clicked.connect(lambda: self.shift_names("b_clear_inputs1"))
        # buttons 2
        self.ui.b_clear_inputs2.clicked.connect(lambda: self.clear_inputs("b_clear_inputs2"))
        self.ui.b_clear_out_names2.clicked.connect(lambda: self.ui.out_names2.clear())
        self.ui.b_clear_out_characters2.clicked.connect(lambda: self.ui.out_characters2.clear())
        self.ui.b_shift2.clicked.connect(lambda: self.shift_names("b_clear_inputs2"))

        # matrix
        self.ui.b_generate.clicked.connect(self.generate_matrix)
        self.ui.tableWidget.doubleClicked.connect(self.show_relation_window)
        self.ui.b_save.clicked.connect(self.save_matrix)

    def _showPopup(self, obj_name):
        number = obj_name[-1]
        cb_location = getattr(self.ui, "cb_location" + number)
        cb_group = getattr(self.ui, "cb_group" + number)
        cb_name = getattr(self.ui, "cb_name" + number)

        # clear data of current QComboBox
        getattr(self.ui, obj_name).clear()

        # get data
        location = cb_location.currentText()
        group = cb_group.currentText()
        name = cb_name.currentText()

        # clear data for all QComboBoxes
        cb_location.clear()
        cb_group.clear()
        cb_name.clear()

        # filter data
        location_values = list(set(self.dbc.filter_characters(location, group, name).loc[:, 'Location'].values))
        group_values = list(set(self.dbc.filter_characters(location, group, name).loc[:, 'Group'].values))
        name_values = list(set(self.dbc.filter_characters(location, group, name).loc[:, 'Name'].values))

        # add filtered data for all QComboBoxes
        cb_location.addItems([''] + location_values)
        cb_group.addItems([''] + group_values)
        cb_name.addItems([''] + name_values)

        # set previously set values for the rest of QComboBoxes
        if obj_name.find('cb_location') < 0:
            values = [''] + location_values
            idx = values.index(location)
            cb_location.setCurrentIndex(idx)
        if obj_name.find('cb_group') < 0:
            values = [''] + group_values
            idx = values.index(group)
            cb_group.setCurrentIndex(idx)
        if obj_name.find('cb_name') < 0:
            values = [''] + name_values
            idx = values.index(name)
            cb_name.setCurrentIndex(idx)

        # execute parent function
        QtWidgets.QComboBox.showPopup(getattr(self.ui, obj_name))

    def update_out_names(self, obj_name):
        number = obj_name[-1]
        cb_location = getattr(self.ui, "cb_location" + number)
        cb_group = getattr(self.ui, "cb_group" + number)
        cb_name = getattr(self.ui, "cb_name" + number)
        out_names = getattr(self.ui, "out_names" + number)

        # clear
        out_names.clear()

        # set filtered data
        location = cb_location.currentText()
        group = cb_group.currentText()
        name = cb_name.currentText()
        list_of_names = list(set(self.dbc.filter_characters(location, group, name).loc[:, 'Name'].values))
        out_names.addItems(list_of_names)

    def clear_inputs(self, obj_name):
        number = obj_name[-1]
        getattr(self.ui, "cb_location" + number).clear()
        getattr(self.ui, "cb_group" + number).clear()
        getattr(self.ui, "cb_name" + number).clear()

    def shift_names(self, obj_name):
        number = obj_name[-1]
        out_names = getattr(self.ui, "out_names" + number)
        out_characters = getattr(self.ui, "out_characters" + number)
        out_names_values = [out_names.item(idx).text() for idx in range(out_names.count())]
        out_characters_values = [out_characters.item(idx).text() for idx in range(out_characters.count())]
        # set new values
        out_characters.clear()
        out_characters.addItems(list(set(out_names_values+out_characters_values)))

    def add_to_qlist(self, obj_name):
        number = obj_name[-1]
        text = getattr(self.ui, "in_name" + number).text()
        out_characters = getattr(self.ui, "out_characters" + number)

        if text not in self.dbc.names:
            return  # invalid input

        out_characters_values = [out_characters.item(idx).text() for idx in range(out_characters.count())]
        if text in out_characters_values:
            return  # input value is already in the Qlist

        # clear and add new data
        out_characters.clear()
        out_characters.addItems(list(set(out_characters_values + [text])))

    def remove_from_qlist(self):
        sender = self.sender()
        if sender.count() <= 0:
            return  # nothing to remove

        row_number = [idx for idx in range(sender.count()) if sender.item(idx).isSelected()][0]
        sender.takeItem(row_number)   # remove
        self.deselect_items_qlist(sender)   # deselect

    @staticmethod
    def deselect_items_qlist(obj: QtWidgets.QListWidget):
        for idx in range(obj.count()):
            if obj.item(idx).isSelected:
                obj.item(idx).setSelected(False)

    @staticmethod
    def get_rgb(in_value):
        in_value = round(float(in_value))
        if in_value <= -5:  # red
            return 255, 0, 0
        elif in_value >= 5:  # greed
            return 0, 255, 0
        elif in_value == 0:  # white
            return 255, 255, 255
        else:
            if in_value < 0:    # light-red
                return 255, 255+(in_value*50), 255+(in_value*50)
            else:   # light-green
                return 255-(in_value*50), 255, 255-(in_value*50)

    def set_table_item(self, item, row, col, in_value):
        """
        Set text, color and tooltip for table's item

        :param item: QTableWidgetItem
        :param in_value: None or [int, [(int, str), (int, str), ...]]
        :return: QTableWidgetItem
        """
        table = self.ui.tableWidget
        table.setItem(row, col, item)
        item = table.item(row, col)

        # set internal variables
        name1 = table.verticalHeaderItem(item.row()).text().replace('\n', ' ')
        name2 = table.horizontalHeaderItem(item.column()).text().replace('\n', ' ')
        setattr(item, '_name1', name1)
        setattr(item, '_name2', name2)
        setattr(item, '_value', in_value)

        # in_value == 'X'
        if in_value is None:
            # text
            item.setText('X')
            # color
            item.setBackground(QtGui.QColor.fromRgb(255, 255, 255))  # white
            # tooltip
            item.setToolTip('')   # no tooltip

        # in_value ==  [int, []]
        elif len(in_value[1]) == 0:
            # text
            out_val = '+' + str(in_value[0]) if in_value[0] > 0 else str(in_value[0])
            item.setText(out_val)
            # color
            rgb = self.get_rgb(in_value[0])  # based on in_value[0]
            item.setBackground(QtGui.QColor.fromRgb(rgb[0], rgb[1], rgb[2]))
            # tooltip
            item.setToolTip('')   # no tooltip

        # in_value ==  [int, [(str, int), ...]]
        else:
            # text
            out_val = '+' + str(in_value[0]) if in_value[0] > 0 else str(in_value[0])
            out_val += '*'
            item.setText(out_val)
            # color
            rgb = self.get_rgb(in_value[0])  # based on in_value[0]
            item.setBackground(QtGui.QColor.fromRgb(rgb[0], rgb[1], rgb[2]))
            # tooltip
            tooltip_text = ''
            for weight, description in in_value[1]:
                if weight > 0: weight = str('+' + str(weight))
                tooltip_text += str(weight) + ' ' + str(description) + '\n'
            item.setToolTip(tooltip_text[:-1])

    def generate_matrix(self):
        """
        Read data from frame1, frame2, Database and populate table with new items
        """
        table = self.ui.tableWidget
        df = self.dbc.df_relations

        # get inputs
        names1 = [self.ui.out_characters1.item(idx).text() for idx in range(self.ui.out_characters1.count())]
        names2 = [self.ui.out_characters2.item(idx).text() for idx in range(self.ui.out_characters2.count())]

        # get values
        df = df.loc[names1, names2]
        data = []
        for index, row in df.iterrows():
            data.append(row.values)

        # TABLE
        # preconditions
        template_item = table.item(0, 0).clone()
        template_item.setBackground(QtGui.QColor.fromRgb(255, 255, 255))
        table.clear()
        # set rows
        table_names1 = [name.replace(' ', '\n') for name in names1]
        table.setRowCount(len(table_names1))
        table.setVerticalHeaderLabels(table_names1)
        # set columns
        table_names2 = [name.replace(' ', '\n') for name in names2]
        table.setColumnCount(len(table_names2))
        table.setHorizontalHeaderLabels(table_names2)
        # set items of table
        for row in range(len(names1)):
            for col in range(len(names2)):
                new_item = template_item.clone()
                self.set_table_item(new_item, row, col, data[row][col])

    def show_relation_window(self):
        """
        When DoubleClick on selected table's item -> show relation_window
        """
        table = self.ui.tableWidget
        item = table.selectedItems()[0]

        # invalid data?
        if item.text() == 'X':
            return

        # show window
        window = self.relation_window
        window.show(item._name1, item._name2)

    def save_matrix(self):
        with pd.ExcelWriter('input_files\\relations.xlsx', mode='a') as writer:
            df = self.dbc.df_relations.copy(deep=True)
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            for row_name in df.index.values:
                for column_name in df.columns.values:
                    val = df.loc[row_name, column_name]     # [-1, [(2, 'drink'), (-3, 'fight')]]
                    if val is None:
                        df.loc[row_name, column_name] = ''
                        continue
                    out_val = int(val[0])
                    if len(val[1]) > 0:
                        out_val = str(out_val) + '\n'
                        out_val += '\n'.join([str(obj[0]) + ' ' + str(obj[1]) for obj in val[1]])
                    df.loc[row_name, column_name] = out_val    # "-1\n2 drink\n-3 fight"

            sheet_name = list(self.dbc.stat_relations.keys())[-1]
            sheet_name = sheet_name[:-1] + str(int(sheet_name[-1]) + 1)
            df.to_excel(writer, sheet_name=sheet_name)


class RelationWindow(QtWidgets.QWidget):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.data = [0, []]

        self.ui.out_relations.itemSelectionChanged.connect(self.update_modify_fields)
        self.ui.out_relations.doubleClicked.connect(self.b_remove_entry)
        self.ui.b_add.clicked.connect(self.b_add_entry)
        self.ui.b_modify.clicked.connect(self.b_modify_entry)
        self.ui.b_clear.clicked.connect(self.b_clear_entries)
        self.ui.b_save.clicked.connect(self.b_save)

    def show(self, name1, name2):
        dbc = Database.get_instance()
        self.data = dbc.df_relations[name1][name2]

        # set ui elements
        self.ui.out_name1.setText(name1)
        self.ui.out_name2.setText(name2)
        self.ui.out_sum.setText(str(self.data[0]))
        self.ui.out_relations.clear()
        # tooltip
        if len(self.data[1]) > 0:
            out_list = []
            for obj in self.data[1]:   # example [(2, 'drink'), (-3, 'fight')]
                text = str(obj[0]) + ' ' + obj[1]
                if obj[0] > 0: text = '+' + text
                out_list.append(text)
            self.ui.out_relations.addItems(out_list)
            self.ui.out_relations.setCurrentRow(0)  # set 1st element as selected

        super().show()

    def update_modify_fields(self):
        """
        fill "modify" fields with data from selected qlist item
        """
        qlist = self.ui.out_relations
        modify_weight = self.ui.sb_modify_weight
        modify_description = self.ui.in_modify_description

        if len(qlist.selectedItems()) == 0:
            # clear
            modify_weight.setValue(0)
            modify_description.setText('')
            return  # nothing is selected

        # get values from current selection
        item = qlist.selectedItems()[0]
        text = item.text()
        idx = text.find(' ')
        weight, description = int(text[:idx]), text[idx + 1:]
        # set values
        modify_weight.setValue(weight)
        modify_description.setText(description)

    def b_add_entry(self):
        """
        add new qlist item
        """
        qlist = self.ui.out_relations

        weight = int(self.ui.sb_add_weight.text())
        description = self.ui.in_add_description.text()
        qlist.addItem(f'{weight} {description}')
        self.set_data()

    def b_modify_entry(self):
        """
        modify selected qlist item
        """
        qlist = self.ui.out_relations
        item = qlist.selectedItems()[0]
        weight = int(self.ui.sb_modify_weight.text())
        description = self.ui.in_modify_description.text()

        item.setText(f'{weight} {description}')
        self.set_data()

    def b_remove_entry(self):
        """
        delete selected qlist item (on DoubleClick)
        """
        qlist = self.ui.out_relations

        if qlist.count() <= 0:
            return  # nothing to remove

        row_number = [idx for idx in range(qlist.count()) if qlist.item(idx).isSelected()][0]
        qlist.takeItem(row_number)  # remove
        self.set_data()

    def b_clear_entries(self):
        """
        delete all qlist items
        """
        qlist = self.ui.out_relations

        qlist.clear()
        self.set_data()

    def set_data(self):
        """
        set new values for internal "data", based on qlist items
        """
        qlist = self.ui.out_relations
        out_sum = self.ui.out_sum

        sum = 0
        self.data = [sum, []]
        for row in range(qlist.count()):
            text = qlist.item(row).text()
            idx = text.find(' ')
            weight, description = int(text[:idx]), text[idx + 1:]
            sum += weight
            self.data[1].append((weight, description))
        self.data[0] = sum
        out_sum.setText(str(sum))

    def b_save(self):
        """
        set new values for database and regenerate matrix
        """
        dbc = Database.get_instance()
        dbc.set_relation_value(self.ui.out_name1.text(),
                               self.ui.out_name2.text(),
                               self.data)  # [ int, [(int, str), (int, str), ...] ]

        self.root.generate_matrix()
        self.close()


app = QtWidgets.QApplication(sys.argv)
app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
screen = MainWindow()
screen.show()
app.exec()
