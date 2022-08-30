#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.10.1

from PyQt5 import QtCore, QtGui, QtWidgets
import icons.icons


class ui_management:
    def __init__(self, ui):
        self.ui = ui

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/window_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.ui.centralwidget = QtWidgets.QWidget(MainWindow)
        self.ui.centralwidget.setObjectName("centralwidget")
        self.ui.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.ui.centralwidget)
        self.ui.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ui.widget_left_panel = QtWidgets.QWidget(self.ui.centralwidget)
        self.ui.widget_left_panel.setMaximumSize(QtCore.QSize(231, 16777215))
        self.ui.widget_left_panel.setObjectName("widget_left_panel")
        self.ui.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.ui.widget_left_panel)
        self.ui.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ui.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ui.VL_lp_main = QtWidgets.QVBoxLayout()
        self.ui.VL_lp_main.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.ui.VL_lp_main.setContentsMargins(-1, -1, 0, -1)
        self.ui.VL_lp_main.setSpacing(6)
        self.ui.VL_lp_main.setObjectName("VL_lp_main")
        self.ui.groupBox_jpegoptim = QtWidgets.QGroupBox(self.ui.widget_left_panel)
        self.ui.groupBox_jpegoptim.setCheckable(True)
        self.ui.groupBox_jpegoptim.setObjectName("groupBox_jpegoptim")
        self.ui.verticalLayout = QtWidgets.QVBoxLayout(self.ui.groupBox_jpegoptim)
        self.ui.verticalLayout.setObjectName("verticalLayout")
        self.ui.radioButton_jpegoptim_optimize = QtWidgets.QRadioButton(self.ui.groupBox_jpegoptim)
        self.ui.radioButton_jpegoptim_optimize.setChecked(True)
        self.ui.radioButton_jpegoptim_optimize.setObjectName("radioButton_jpegoptim_optimize")
        self.ui.verticalLayout.addWidget(self.ui.radioButton_jpegoptim_optimize)
        self.ui.radioButton_jpegoptim_compression = QtWidgets.QRadioButton(self.ui.groupBox_jpegoptim)
        self.ui.radioButton_jpegoptim_compression.setObjectName("radioButton_jpegoptim_compression")
        self.ui.verticalLayout.addWidget(self.ui.radioButton_jpegoptim_compression)
        self.ui.HL_jpegoptim_jpegoptim_compression = QtWidgets.QHBoxLayout()
        self.ui.HL_jpegoptim_jpegoptim_compression.setObjectName("HL_jpegoptim_jpegoptim_compression")
        self.ui.horizontalSlider_jpegoptim_compression = QtWidgets.QSlider(self.ui.groupBox_jpegoptim)
        self.ui.horizontalSlider_jpegoptim_compression.setMaximum(100)
        self.ui.horizontalSlider_jpegoptim_compression.setSliderPosition(50)
        self.ui.horizontalSlider_jpegoptim_compression.setOrientation(QtCore.Qt.Horizontal)
        self.ui.horizontalSlider_jpegoptim_compression.setInvertedAppearance(False)
        self.ui.horizontalSlider_jpegoptim_compression.setInvertedControls(False)
        self.ui.horizontalSlider_jpegoptim_compression.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.ui.horizontalSlider_jpegoptim_compression.setTickInterval(5)
        self.ui.horizontalSlider_jpegoptim_compression.setObjectName("horizontalSlider_jpegoptim_compression")
        self.ui.HL_jpegoptim_jpegoptim_compression.addWidget(self.ui.horizontalSlider_jpegoptim_compression)
        self.ui.spinBox_jpegoptim_compression = QtWidgets.QSpinBox(self.ui.groupBox_jpegoptim)
        self.ui.spinBox_jpegoptim_compression.setMaximum(100)
        self.ui.spinBox_jpegoptim_compression.setSingleStep(5)
        self.ui.spinBox_jpegoptim_compression.setProperty("value", 50)
        self.ui.spinBox_jpegoptim_compression.setObjectName("spinBox_jpegoptim_compression")
        self.ui.HL_jpegoptim_jpegoptim_compression.addWidget(self.ui.spinBox_jpegoptim_compression)
        self.ui.verticalLayout.addLayout(self.ui.HL_jpegoptim_jpegoptim_compression)
        self.ui.HL_jpegoptim_compression_up_to = QtWidgets.QHBoxLayout()
        self.ui.HL_jpegoptim_compression_up_to.setObjectName("HL_jpegoptim_compression_up_to")
        self.ui.radioButton_jpegoptim_compression_up_to = QtWidgets.QRadioButton(self.ui.groupBox_jpegoptim)
        self.ui.radioButton_jpegoptim_compression_up_to.setObjectName("radioButton_jpegoptim_compression_up_to")
        self.ui.HL_jpegoptim_compression_up_to.addWidget(self.ui.radioButton_jpegoptim_compression_up_to)
        self.ui.spinBox_jpegoptim_compression_up_to = QtWidgets.QSpinBox(self.ui.groupBox_jpegoptim)
        self.ui.spinBox_jpegoptim_compression_up_to.setMinimum(1)
        self.ui.spinBox_jpegoptim_compression_up_to.setMaximum(999999999)
        self.ui.spinBox_jpegoptim_compression_up_to.setSingleStep(50)
        self.ui.spinBox_jpegoptim_compression_up_to.setProperty("value", 100)
        self.ui.spinBox_jpegoptim_compression_up_to.setObjectName("spinBox_jpegoptim_compression_up_to")
        self.ui.HL_jpegoptim_compression_up_to.addWidget(self.ui.spinBox_jpegoptim_compression_up_to)
        self.ui.verticalLayout.addLayout(self.ui.HL_jpegoptim_compression_up_to)
        self.ui.VL_lp_main.addWidget(self.ui.groupBox_jpegoptim)
        self.ui.checkBox_mat = QtWidgets.QCheckBox(self.ui.widget_left_panel)
        self.ui.checkBox_mat.setChecked(True)
        self.ui.checkBox_mat.setObjectName("checkBox_mat")
        self.ui.VL_lp_main.addWidget(self.ui.checkBox_mat)
        self.ui.HL_advdef = QtWidgets.QHBoxLayout()
        self.ui.HL_advdef.setObjectName("HL_advdef")
        self.ui.checkBox_advdef = QtWidgets.QCheckBox(self.ui.widget_left_panel)
        self.ui.checkBox_advdef.setChecked(True)
        self.ui.checkBox_advdef.setObjectName("checkBox_advdef")
        self.ui.HL_advdef.addWidget(self.ui.checkBox_advdef)
        self.ui.comboBox_advdef = QtWidgets.QComboBox(self.ui.widget_left_panel)
        self.ui.comboBox_advdef.setEnabled(True)
        self.ui.comboBox_advdef.setMinimumSize(QtCore.QSize(130, 0))
        self.ui.comboBox_advdef.setObjectName("comboBox_advdef")
        self.ui.comboBox_advdef.addItem("")
        self.ui.comboBox_advdef.addItem("")
        self.ui.comboBox_advdef.addItem("")
        self.ui.comboBox_advdef.addItem("")
        self.ui.HL_advdef.addWidget(self.ui.comboBox_advdef)
        self.ui.VL_lp_main.addLayout(self.ui.HL_advdef)
        self.ui.HL_optipng = QtWidgets.QHBoxLayout()
        self.ui.HL_optipng.setObjectName("HL_optipng")
        self.ui.checkBox_optipng = QtWidgets.QCheckBox(self.ui.widget_left_panel)
        self.ui.checkBox_optipng.setChecked(True)
        self.ui.checkBox_optipng.setObjectName("checkBox_optipng")
        self.ui.HL_optipng.addWidget(self.ui.checkBox_optipng)
        self.ui.comboBox_optipng = QtWidgets.QComboBox(self.ui.widget_left_panel)
        self.ui.comboBox_optipng.setEnabled(True)
        self.ui.comboBox_optipng.setMinimumSize(QtCore.QSize(130, 25))
        self.ui.comboBox_optipng.setObjectName("comboBox_optipng")
        for item in range(9):
            self.ui.comboBox_optipng.addItem("")
        self.ui.HL_optipng.addWidget(self.ui.comboBox_optipng)
        self.ui.VL_lp_main.addLayout(self.ui.HL_optipng)
        self.ui.VL_list_optimized = QtWidgets.QVBoxLayout()
        self.ui.VL_list_optimized.setObjectName("VL_list_optimized")
        self.ui.label_list_optimized = QtWidgets.QLabel(self.ui.widget_left_panel)
        self.ui.label_list_optimized.setObjectName("label_list_optimized")
        self.ui.VL_list_optimized.addWidget(self.ui.label_list_optimized)
        self.ui.listWidget_list_optimized = QtWidgets.QListWidget(self.ui.widget_left_panel)
        self.ui.listWidget_list_optimized.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.ui.listWidget_list_optimized.setDragEnabled(True)
        self.ui.listWidget_list_optimized.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.ui.listWidget_list_optimized.setDefaultDropAction(QtCore.Qt.MoveAction)
        # self.ui.listWidget_list_optimized.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.ui.listWidget_list_optimized.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ui.listWidget_list_optimized.setObjectName("listWidget_list_optimized")
        self.ui.VL_list_optimized.addWidget(self.ui.listWidget_list_optimized)
        self.ui.progressBar_list_optimized = QtWidgets.QProgressBar(self.ui.widget_left_panel)
        self.ui.progressBar_list_optimized.setEnabled(False)
        self.ui.progressBar_list_optimized.setProperty("value", 0)
        self.ui.progressBar_list_optimized.setObjectName("progressBar_list_optimized")
        self.ui.VL_list_optimized.addWidget(self.ui.progressBar_list_optimized)
        self.ui.VL_lp_main.addLayout(self.ui.VL_list_optimized)
        self.ui.horizontalLayout_6.addLayout(self.ui.VL_lp_main)
        self.ui.horizontalLayout_7.addWidget(self.ui.widget_left_panel)
        self.ui.verticalLayout_rp_main = QtWidgets.QVBoxLayout()
        self.ui.verticalLayout_rp_main.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.ui.verticalLayout_rp_main.setContentsMargins(-1, -1, 0, 0)
        self.ui.verticalLayout_rp_main.setObjectName("verticalLayout_rp_main")
        self.ui.label_drag_and_drop = QtWidgets.QLabel(self.ui.centralwidget)
        self.ui.label_drag_and_drop.setObjectName("label_drag_and_drop")
        self.ui.verticalLayout_rp_main.addWidget(self.ui.label_drag_and_drop)
        self.ui.listWidget_queue = MyQListWidget(self.ui.centralwidget)
        self.ui.listWidget_queue.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.ui.listWidget_queue.setDragEnabled(True)
        self.ui.listWidget_queue.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.ui.listWidget_queue.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ui.listWidget_queue.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ui.listWidget_queue.setObjectName("listWidget_queue")
        self.ui.verticalLayout_rp_main.addWidget(self.ui.listWidget_queue)
        self.ui.HL_buttons = QtWidgets.QHBoxLayout()
        self.ui.HL_buttons.setObjectName("HL_buttons")
        self.ui.pushButton_start = QtWidgets.QPushButton(self.ui.centralwidget)
        self.ui.pushButton_start.setEnabled(True)
        self.ui.pushButton_start.setObjectName("pushButton_start")
        self.ui.HL_buttons.addWidget(self.ui.pushButton_start)
        self.ui.pushButton_pause = QtWidgets.QPushButton(self.ui.centralwidget)
        self.ui.pushButton_pause.setEnabled(False)
        self.ui.pushButton_pause.setObjectName("pushButton_pause")
        self.ui.HL_buttons.addWidget(self.ui.pushButton_pause)
        self.ui.pushButton_delete_items = QtWidgets.QPushButton(self.ui.centralwidget)
        self.ui.pushButton_delete_items.setObjectName("pushButton_delete_items")
        self.ui.HL_buttons.addWidget(self.ui.pushButton_delete_items)
        self.ui.pushButton_delete_all_items = QtWidgets.QPushButton(self.ui.centralwidget)
        self.ui.pushButton_delete_all_items.setObjectName("pushButton_delete_all_items")
        self.ui.HL_buttons.addWidget(self.ui.pushButton_delete_all_items)
        self.ui.verticalLayout_rp_main.addLayout(self.ui.HL_buttons)
        self.ui.horizontalLayout_7.addLayout(self.ui.verticalLayout_rp_main)
        MainWindow.setCentralWidget(self.ui.centralwidget)
        self.ui.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.ui.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.ui.statusbar)
        self.ui.menubar = QtWidgets.QMenuBar(MainWindow)
        self.ui.menubar.setGeometry(QtCore.QRect(0, 0, 659, 22))
        self.ui.menubar.setObjectName("menubar")
        self.ui.menu_settings = QtWidgets.QMenu(self.ui.menubar)
        self.ui.menu_settings.setTearOffEnabled(False)
        self.ui.menu_settings.setSeparatorsCollapsible(False)
        self.ui.menu_settings.setToolTipsVisible(False)
        self.ui.menu_settings.setObjectName("menu_settings")
        MainWindow.setMenuBar(self.ui.menubar)
        self.ui.action_save_config = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/save_config.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.action_save_config.setIcon(icon1)
        self.ui.action_save_config.setMenuRole(QtWidgets.QAction.NoRole)
        self.ui.action_save_config.setIconVisibleInMenu(True)
        self.ui.action_save_config.setObjectName("action_save_config")
        self.ui.action_auto_optimize = QtWidgets.QAction(MainWindow)
        self.ui.action_auto_optimize.setCheckable(True)
        self.ui.action_auto_optimize.setChecked(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/auto_optimize_1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.action_auto_optimize.setIcon(icon2)
        self.ui.action_auto_optimize.setObjectName("action_auto_optimize")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/show_full_file_names.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.action_about = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/about.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.action_about.setIcon(icon4)
        self.ui.action_about.setObjectName("action_about")
        self.ui.menu_settings.addAction(self.ui.action_save_config)
        self.ui.menu_settings.addAction(self.ui.action_auto_optimize)
        self.ui.menu_settings.addSeparator()
        self.ui.menu_settings.addAction(self.ui.action_about)
        self.ui.menubar.addAction(self.ui.menu_settings.menuAction())

        self.retranslateUi(MainWindow)

        self.ui.comboBox_advdef.setCurrentIndex(2)
        self.ui.comboBox_optipng.setCurrentIndex(6)
        self.ui.horizontalSlider_jpegoptim_compression.sliderMoved['int'].connect(
            self.ui.spinBox_jpegoptim_compression.setValue)
        self.ui.spinBox_jpegoptim_compression.valueChanged['int'].connect(
            self.ui.horizontalSlider_jpegoptim_compression.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ui.run_when_app_starting()
        MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Optimizer for GNU/Linux v0.1"))
        self.ui.groupBox_jpegoptim.setToolTip(_translate("MainWindow", "Оптимизация jpg"))
        self.ui.groupBox_jpegoptim.setTitle(_translate("MainWindow", "jpegoptim"))
        self.ui.radioButton_jpegoptim_optimize.setToolTip(_translate("MainWindow", "Режим оптимизации"))
        self.ui.radioButton_jpegoptim_optimize.setText(_translate("MainWindow", "Оптимизация"))
        self.ui.radioButton_jpegoptim_compression.setToolTip(_translate("MainWindow", "Отключает режим оптимизации"))
        self.ui.radioButton_jpegoptim_compression.setText(_translate("MainWindow", "Сжатие с потерями"))
        self.ui.horizontalSlider_jpegoptim_compression.setToolTip(
            _translate("MainWindow", "Качество выходного файла, %"))
        self.ui.spinBox_jpegoptim_compression.setToolTip(_translate("MainWindow", "Качество выходного файла, %"))
        self.ui.radioButton_jpegoptim_compression_up_to.setToolTip(
            _translate("MainWindow", "Сделать размер изображения строго:"))
        self.ui.radioButton_jpegoptim_compression_up_to.setText(_translate("MainWindow", "Сжать до (Kb)"))
        self.ui.spinBox_jpegoptim_compression_up_to.setToolTip(_translate("MainWindow", "Размер выходного файла в Kb"))
        self.ui.checkBox_mat.setToolTip(_translate("MainWindow", "Пытаться очищать метаданные"))
        self.ui.checkBox_mat.setText(_translate("MainWindow", "mat"))
        self.ui.checkBox_advdef.setToolTip(_translate("MainWindow", "Оптимизация png"))
        self.ui.checkBox_advdef.setText(_translate("MainWindow", "advdef"))
        self.ui.comboBox_advdef.setToolTip(
            _translate("MainWindow", "Степень сжатия advdef, где -z1 — минимум, -z4 — максимум."))
        self.ui.comboBox_advdef.setItemText(0, _translate("MainWindow", "-z1"))
        self.ui.comboBox_advdef.setItemText(1, _translate("MainWindow", "-z2"))
        self.ui.comboBox_advdef.setItemText(2, _translate("MainWindow", "-z3"))
        self.ui.comboBox_advdef.setItemText(3, _translate("MainWindow", "-z4"))
        self.ui.checkBox_optipng.setToolTip(_translate("MainWindow", "Оптимизация png"))
        self.ui.checkBox_optipng.setText(_translate("MainWindow", "optipng"))
        self.ui.comboBox_optipng.setToolTip(_translate("MainWindow",
                                                       "Степень сжатия optipng, где -o0 — минимум, -o7 — максимум. В скобках - кол-во попыток оптимизации"))
        self.ui.comboBox_optipng.setItemText(0, _translate("MainWindow", "-o0 (0 или 1)"))
        self.ui.comboBox_optipng.setItemText(1, _translate("MainWindow", "-o1 (1)"))
        self.ui.comboBox_optipng.setItemText(2, _translate("MainWindow", "-o2 (8)"))
        self.ui.comboBox_optipng.setItemText(3, _translate("MainWindow", "-o3 (16)"))
        self.ui.comboBox_optipng.setItemText(4, _translate("MainWindow", "-o4 (24)"))
        self.ui.comboBox_optipng.setItemText(5, _translate("MainWindow", "-o5 (48)"))
        self.ui.comboBox_optipng.setItemText(6, _translate("MainWindow", "-o6 (120)"))
        self.ui.comboBox_optipng.setItemText(7, _translate("MainWindow", "-o7 (240)"))
        self.ui.comboBox_optipng.setItemText(8, _translate("MainWindow", "-o7 -zm1-9 (1080)"))
        self.ui.label_list_optimized.setText(_translate("MainWindow", "Оптимизировано"))
        self.ui.progressBar_list_optimized.setToolTip(_translate("MainWindow", "Прогресс оптимизации"))
        self.ui.label_drag_and_drop.setText(_translate("MainWindow", "Drop"))
        self.ui.listWidget_queue.setSortingEnabled(False)
        self.ui.pushButton_start.setToolTip(_translate("MainWindow", "Запустить оптимизацию"))
        self.ui.pushButton_start.setText(_translate("MainWindow", "Запустить"))
        self.ui.pushButton_pause.setToolTip(
            _translate("MainWindow", "Закончить оптимизацию текущего файла и приостановить работу"))
        self.ui.pushButton_pause.setText(_translate("MainWindow", "Пауза"))
        self.ui.pushButton_delete_items.setToolTip(_translate("MainWindow", "Убрать выбранные файлы из списка"))
        self.ui.pushButton_delete_items.setText(_translate("MainWindow", "Убрать"))
        self.ui.pushButton_delete_all_items.setToolTip(_translate("MainWindow", "Убрать все файлы из списка"))
        self.ui.pushButton_delete_all_items.setText(_translate("MainWindow", "Убрать все"))
        self.ui.menu_settings.setTitle(_translate("MainWindow", "Настройки"))
        self.ui.action_save_config.setText(_translate("MainWindow", "Сохранить текущие настройки"))
        self.ui.action_save_config.setToolTip(_translate("MainWindow",
                                                         "Текущие настройки программы будут автоматически загружены при следующем запуске программы"))
        self.ui.action_auto_optimize.setText(_translate("MainWindow", "Автозапуск оптимизации"))
        self.ui.action_auto_optimize.setToolTip(_translate("MainWindow",
                                                           "Запускать оптимизацию сразу, если при открытии программы были переданы изображения"))
        self.ui.action_about.setText(_translate("MainWindow", "О программе"))


    def analyze_cli_parameters(self):
        self.ui.parser = argparse.ArgumentParser(
            prog=sys.argv[0],
            description='Программа для оптимизации изображений',
            epilog='(c) adminka-root. https://github.com/adminka-root',
            add_help=False
        )

        parent_group = self.ui.parser.add_argument_group(title='Опциональные параметры')
        parent_group.add_argument('-f', '--files', nargs='*', type=os.path.expanduser,
                                  help='Указать исходные изображения', metavar='FILE')
        parent_group.add_argument('--help', '-h', action='help', help='Справка')

        self.ui.options = self.ui.parser.parse_args(sys.argv[1:])
        if not self.ui.options.files:  # чтоб не передавать None в будущем
            self.ui.options.files = []

    def off_on_widgets_used_to_generate_commands(self, need_on: bool):
        self.ui.groupBox_jpegoptim.setEnabled(need_on)
        self.ui.checkBox_mat.setEnabled(need_on)
        self.ui.checkBox_advdef.setEnabled(need_on)
        self.ui.comboBox_advdef.setEnabled(need_on)
        self.ui.checkBox_optipng.setEnabled(need_on)
        self.ui.comboBox_optipng.setEnabled(need_on)
        self.ui.pushButton_start.setEnabled(need_on)
        self.ui.pushButton_pause.setEnabled(not need_on)
        self.__need_pause = need_on

        if need_on:
            self.ui.listWidget_list_optimized.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        else:
            self.ui.listWidget_list_optimized.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)

    def clicked_button_start(self):
        # когда нажата была пауза, всегда существует объект self.ui.item_0
        # "умная" очистка. полностью чистим, когда "единичный" запуск был закончен
        if not hasattr(self.ui, 'item_0'):
            self.ui.listWidget_list_optimized.clear()
            self.ui.progressBar_list_optimized.setValue(0)

        self.off_on_widgets_used_to_generate_commands(need_on=False)
        self.ui.settings.updating_internal_variables()
        self.ui.optimize_process.need_pause = False
        self.ui.optimize_process.start_process()

    def clicked_button_pause(self):
        self.ui.optimize_process.need_pause = True
        self.ui.pushButton_pause.setEnabled(False)
        self.ui.statusbar.showMessage("Завершаю для " + self.ui.item_0.image_name)

    def about_show(self, MainWindow):
        if not hasattr(self.ui, 'about_window'):
            from about import Ui_About
            self.ui.about_window = QtWidgets.QDialog(MainWindow)
            self.about_window = Ui_About()
            self.about_window.setupUi(self.ui.about_window)
        self.ui.about_window.exec_()


class optimize_process:
    def __init__(self, ui):
        self.ui = ui
        self.need_pause = False
        self.process = QtCore.QProcess()
        # кол-во оптимизир. файлов в рамках цельного запуска
        self.count_optimized_in_box = 0
        self.mat_or_mat2()

    def mat_or_mat2(self):
        if os.path.isfile('/usr/bin/mat'):
            self.is_mat = True
        elif os.path.isfile('/usr/bin/mat2'):
            self.is_mat = False
        else:
            print("Не обнаружен mat/mat2!")

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        print(stderr)

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        print(stdout)

    def start_process(self):
        if self.need_pause:
            self.ui.ui_management.off_on_widgets_used_to_generate_commands(need_on=True)
            if self.ui.item_0.is_in_queue():
                self.ui.statusbar.showMessage("В очереди " + self.ui.item_0.image_name)
            else:
                self.ui.statusbar.showMessage("")
        else:
            if hasattr(self.ui, 'item_0'):
                program, options = self.ui.item_0.return_current_command()
                # print(self.ui.item_0.image_queue, program, options, self.image_queue_exec_index)
                if program is not None and options is not None:
                    print(program, *options, repr(self.ui.item_0.image_name))
                    self.ui.statusbar.showMessage(
                        "[%s] Оптимизирую %s" % (self.count_optimized_in_box, self.ui.item_0.image_name))
                    self.process.readyReadStandardOutput.connect(self.handle_stdout)
                    self.process.readyReadStandardError.connect(self.handle_stderr)
                    self.process.finished.connect(self.process_finished)
                    self.process.start(program, options + [self.ui.item_0.image_name])
                else:
                    if self.ui.item_0.image_name:  # если файл НЕ исчез до запуска, т.е. !=''
                        self.ui.listWidget_list_optimized.addItem(self.ui.item_0.image_name)
                    del self.ui.item_0
                    self.start_process()
            else:
                if self.ui.listWidget_queue.count() > 0:
                    self.ui.progressBar_list_optimized.setValue(
                        100 / (
                                self.ui.listWidget_queue.count() + self.count_optimized_in_box
                        ) * self.count_optimized_in_box
                    )

                    self.count_optimized_in_box += 1

                    self.ui.item_0 = item_0(self.ui)
                    self.start_process()
                else:
                    if self.ui.listWidget_list_optimized.count() == 0:
                        print("Нечего оптимизировать!")
                        self.ui.statusbar.showMessage("Нечего оптимизировать!")
                    else:
                        self.count_optimized_in_box = 0
                        self.ui.progressBar_list_optimized.setValue(100)
                        print("Оптимизация завершена!")
                        self.ui.statusbar.showMessage("Оптимизация завершена!")
                    self.ui.ui_management.off_on_widgets_used_to_generate_commands(need_on=True)
                    # self.ui.listWidget_list_optimized.clear

    def process_finished(self):
        self.process = QtCore.QProcess()
        self.start_process()


class item_0:
    def __init__(self, ui):
        self.ui = ui
        self.image_name = ''
        self.generate_command()
        self.image_queue_exec_index = 0

    def generate_command(self):
        while not self.image_name and self.ui.listWidget_queue.count() != 0:
            self.image_name = self.ui.return_valid_files(
                [self.ui.listWidget_queue.item(0).text()],
                self.ui.valid_ext
            )
            self.ui.listWidget_queue.takeItem(0)

        self.image_queue = []
        if self.image_name:
            self.image_name = self.image_name[0]

            if self.ui.config_params['mat']['enabled']:
                if self.ui.optimize_process.is_mat:
                    self.image_queue.append(['mat', []])
                else:
                    self.image_queue.append(['mat2', ['--inplace']])

            image_ext = os.path.splitext(self.image_name)[1][1:].lower()
            if image_ext in self.ui.valid_jpg:
                if self.ui.config_params['jpegoptim']['jpegoptim_enabled']:
                    params = []
                    if self.ui.config_params['jpegoptim']['optimize_enabled']:
                        params = []
                    elif self.ui.config_params['jpegoptim']['compression_enabled']:
                        params = ['-m' + str(self.ui.spinBox_jpegoptim_compression.value())]
                    else:  # self.ui.config_params['jpegoptim']['compression_up_to_enabled']
                        params = ['--size=' + str(self.ui.spinBox_jpegoptim_compression_up_to.value()) + 'k']
                    self.image_queue.append(['jpegoptim', params])

            elif image_ext in self.ui.valid_png:
                if self.ui.config_params['optipng']['enabled']:
                    self.image_queue.append(
                        [
                            'optipng',
                            ''.join(
                                self.ui.comboBox_optipng.itemText(
                                    self.ui.config_params['optipng']['mode']
                                ).split(' (')[0]
                            ).split()
                        ]
                    )

                if self.ui.config_params['advdef']['enabled']:
                    # на будущее??
                    self.image_queue.append(
                        ['advdef',
                         ''.join(
                             self.ui.comboBox_advdef.itemText(
                                 self.ui.config_params['advdef']['mode']
                             ).split(' (')[0]
                         ).split()
                         ]
                    )
                    # self.image_queue.append(
                    #     ['advdef',
                    #      [self.ui.comboBox_advdef.itemText(self.ui.config_params['advdef']['mode'])]
                    #      ]
                    # )


    def return_current_command(self):
        if self.is_in_queue():
            self.image_queue_exec_index += 1
            return self.image_queue[self.image_queue_exec_index - 1][0], \
                   self.image_queue[self.image_queue_exec_index - 1][1]
        else:
            return None, None

    def is_in_queue(self):
        if len(self.image_queue) > self.image_queue_exec_index:
            return True
        return False


class management_of_config:
    def __init__(self, ui):
        self.ui = ui

    def load_settings_from_config_file(self):
        try:
            with open(self.ui.config_file) as file:
                self.ui.config_params = json.load(file)

                self.ui.groupBox_jpegoptim.setChecked(self.ui.config_params['jpegoptim']['jpegoptim_enabled'])
                self.ui.horizontalSlider_jpegoptim_compression.setSliderPosition(
                    self.ui.config_params['jpegoptim']['compression_value'])

                self.ui.radioButton_jpegoptim_optimize.setChecked(
                    self.ui.config_params['jpegoptim']['optimize_enabled'])
                self.ui.radioButton_jpegoptim_compression.setChecked(
                    self.ui.config_params['jpegoptim']['compression_enabled'])
                self.ui.radioButton_jpegoptim_compression_up_to.setChecked(
                    self.ui.config_params['jpegoptim']['compression_up_to_enabled'])

                self.ui.checkBox_mat.setChecked(self.ui.config_params['mat']['enabled'])
                self.ui.checkBox_advdef.setChecked(self.ui.config_params['advdef']['enabled'])
                self.ui.checkBox_optipng.setChecked(self.ui.config_params['optipng']['enabled'])

                self.ui.spinBox_jpegoptim_compression.setValue(self.ui.config_params['jpegoptim']['compression_value'])
                self.ui.spinBox_jpegoptim_compression_up_to.setValue(
                    self.ui.config_params['jpegoptim']['compression_up_to_value'])

                self.ui.comboBox_advdef.setCurrentIndex(self.ui.config_params['advdef']['mode'])
                self.ui.comboBox_optipng.setCurrentIndex(self.ui.config_params['optipng']['mode'])

                self.ui.action_auto_optimize.setChecked(self.ui.config_params['settings']['auto_optimize'])
        except:
            print("Не удалось загрузить файл настроек %s!" % self.ui.config_file)
            self.updating_internal_variables()

    def overwrite_config_file(self):
        self.updating_internal_variables()
        try:
            with open(self.ui.config_file, 'w+') as file:
                json.dump(self.ui.config_params, file, sort_keys=False, indent=4, ensure_ascii=False)
        except:
            print("Невозможно сохранить настройки!")  # PermissionError

    def updating_internal_variables(self):
        self.ui.config_params = {}
        self.ui.config_params['jpegoptim'] = {
            'jpegoptim_enabled': self.ui.groupBox_jpegoptim.isChecked(),
            'optimize_enabled': self.ui.radioButton_jpegoptim_optimize.isChecked(),
            'compression_enabled': self.ui.radioButton_jpegoptim_compression.isChecked(),
            'compression_value': self.ui.horizontalSlider_jpegoptim_compression.value(),
            'compression_up_to_enabled': self.ui.radioButton_jpegoptim_compression_up_to.isChecked(),
            'compression_up_to_value': self.ui.spinBox_jpegoptim_compression_up_to.value()
        }

        self.ui.config_params['mat'] = {
            'enabled': self.ui.checkBox_mat.isChecked()
        }

        self.ui.config_params['advdef'] = {
            'enabled': self.ui.checkBox_advdef.isChecked(),
            'mode': self.ui.comboBox_advdef.currentIndex()
        }

        self.ui.config_params['advdef'] = {
            'enabled': self.ui.checkBox_advdef.isChecked(),
            'mode': self.ui.comboBox_advdef.currentIndex()
        }

        self.ui.config_params['optipng'] = {
            'enabled': self.ui.checkBox_optipng.isChecked(),
            'mode': self.ui.comboBox_optipng.currentIndex()
        }

        self.ui.config_params['settings'] = {
            'auto_optimize': self.ui.action_auto_optimize.isChecked()
        }


class MyQListWidget(QtWidgets.QListWidget):
    dropped = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

    @staticmethod
    def return_ListWidget_elements(list_widget):
        list_of_elements = []
        for index in range(list_widget.count()):
            list_of_elements.append(list_widget.item(index).text())
        return list_of_elements

    @staticmethod
    def add_ListWidget_elements(list_widget, elements: "list of str"):
        for elem in elements:
            list_widget.addItem(elem)

    @staticmethod
    def remove_ListWidget_selected_elements(list_widget):
        for item in list_widget.selectedItems():
            list_widget.takeItem(list_widget.row(item))

    # d&d из файлового менеджера и анализ
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls() or event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls() or event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()

            if event.mimeData().hasUrls():
                event.setDropAction(QtCore.Qt.CopyAction)
                drop_items = set(map(lambda z: z.toLocalFile(), event.mimeData().urls()))
            else:
                event.setDropAction(QtCore.Qt.MoveAction)
                source_item = QtGui.QStandardItemModel()
                source_item.dropMimeData(event.mimeData(), QtCore.Qt.CopyAction, 0, 0, QtCore.QModelIndex())
                drop_items = set(map(lambda h: h.text(), source_item.takeColumn(0)))

            current_items = set(self.return_ListWidget_elements(self))
            drop_items -= current_items
            drop_items = Ui_MainWindow.return_valid_files(drop_items, ['jpg', 'jpeg', 'png'])
            self.addItems(drop_items)
            self.dropped.emit(drop_items)

        else:
            event.ignore()


class Ui_MainWindow(object):

    @staticmethod
    def return_valid_files(files: "list of str", exts: "list of str"):
        good_files = set()
        for file in files:
            if os.path.isfile(file) and os.access(file, os.W_OK) and \
                    os.path.splitext(file)[1][1:].lower() in exts:
                good_files.add(file)
        return list(good_files)

    @staticmethod
    def sys_depends_installed():
        from subprocess import Popen, PIPE, DEVNULL
        no_package = []
        try:
            status = Popen(['mat'], stdout=DEVNULL, stderr=DEVNULL)
        except FileNotFoundError:
            try:
                status = Popen(['mat2'], stdout=DEVNULL, stderr=DEVNULL)
            except FileNotFoundError:
                no_package.append('mat2')

        try:
            status = Popen(['advdef'], stdout=DEVNULL, stderr=DEVNULL)
        except FileNotFoundError:
            no_package.append('advancecomp')

        try:
            status = Popen(['optipng'], stdout=DEVNULL, stderr=DEVNULL)
        except FileNotFoundError:
            no_package.append('optipng')

        try:
            status = Popen(['jpegoptim'], stdout=DEVNULL, stderr=DEVNULL)
        except FileNotFoundError:
            no_package.append('jpegoptim')

        if no_package:
            errors = 'Отсутствуют необходимые зависимости! Пожалуйста, выполните:\n' + \
                     'sudo apt install ' + ' '.join(no_package)
            print(errors)
            QtWidgets.QMessageBox.critical(None, 'Ошибка!', errors)
            return False
        else:
            return True

    def __init__(self):
        super().__init__()
        # переменные
        self.valid_jpg = ['jpg', 'jpeg']
        self.valid_png = ['png']
        self.valid_ext = self.valid_jpg + self.valid_png

        self.base_config_path = os.path.expanduser('~/.config/image_optimizer/')
        os.makedirs(self.base_config_path, exist_ok=True)
        self.config_file = self.base_config_path + 'config_file.txt'

        # объекты классов
        self.ui_management = ui_management(self)
        self.settings = management_of_config(self)
        self.optimize_process = optimize_process(self)

    def run_when_app_starting(self):
        self.connect_widgets()  # сюда подключаем сигналы и слоты...

        self.settings.load_settings_from_config_file()

        # заносим в ListWidget список валидных файлов из cli
        self.ui_management.analyze_cli_parameters()  # получаем self.options.files
        MyQListWidget.add_ListWidget_elements(
            self.listWidget_queue,
            Ui_MainWindow.return_valid_files(
                self.options.files, self.valid_ext
            )
        )

        if self.config_params['settings']['auto_optimize']:
            self.ui_management.clicked_button_start()

    def connect_widgets(self):
        self.action_save_config.triggered.connect(self.settings.overwrite_config_file)
        self.pushButton_start.clicked.connect(self.ui_management.clicked_button_start)
        self.pushButton_pause.clicked.connect(self.ui_management.clicked_button_pause)

        self.pushButton_delete_items.clicked.connect(
            lambda:
            MyQListWidget.remove_ListWidget_selected_elements(
                self.listWidget_queue
            )
        )
        self.pushButton_delete_all_items.clicked.connect(self.listWidget_queue.clear)

        # передача глобалки. так себе style
        self.action_about.triggered.connect(lambda: self.ui_management.about_show(MainWindow))


if __name__ == "__main__":
    import sys
    import json
    import os
    import argparse

    app = QtWidgets.QApplication(sys.argv)
    if Ui_MainWindow.sys_depends_installed():
        MainWindow = QtWidgets.QMainWindow()
        ui_w = Ui_MainWindow()
        ui_w.ui_management.setupUi(MainWindow)
        sys.exit(app.exec_())
