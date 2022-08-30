#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
import icons.icons


class Ui_About(QtWidgets.QDialog):
    # без родителя вызовет ошибку
    def __init__(self, parent=None):
        super().__init__(parent)

    def setupUi(self, About):
        About.setObjectName("About")
        About.setFixedSize(360, 160)  # !!!
        About.resize(360, 160)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/window_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setMaximumSize(QtCore.QSize(48, 48))
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap(":/icons/window_icon.svg"))
        self.label_image.setObjectName("label_image")
        self.verticalLayout.addWidget(self.label_image)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.label_description = QtWidgets.QLabel(self.centralwidget)
        self.label_description.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_description.setObjectName("label_description")
        self.verticalLayout_2.addWidget(self.label_description)
        self.label_copyright = QtWidgets.QLabel(self.centralwidget)
        self.label_copyright.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_copyright.setObjectName("label_copyright")
        self.verticalLayout_2.addWidget(self.label_copyright)
        self.label_license = QtWidgets.QLabel(self.centralwidget)
        self.label_license.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_license.setObjectName("label_license")
        self.verticalLayout_2.addWidget(self.label_license)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_site = QtWidgets.QLabel(self.centralwidget)
        self.label_site.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_site.setOpenExternalLinks(True)  # !!!
        self.label_site.setObjectName("label_site")
        self.horizontalLayout.addWidget(self.label_site)
        self.buttonBox_close = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox_close.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox_close.setObjectName("buttonBox_close")
        self.horizontalLayout.addWidget(self.buttonBox_close)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.retranslateUi(About)
        self.buttonBox_close.rejected.connect(About.close)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Image Optimizer v0.1"))
        self.label_title.setText(_translate("About", "Image Optimizer for GNU/Linux"))
        self.label_description.setText(_translate(
            "About", "Контроль размера изображений путем \n" "оптимизации, сжатия, удаления метаданных"))
        self.label_copyright.setText(_translate("About", "Copyright @2022 adminka-root"))
        self.label_license.setText(_translate("About", "GPL-3.0"))
        self.label_site.setText(_translate("About",
                                           "<html><head/><body><p><a href=\"https://github.com/adminka-root/image_optimizer\"><span style=\" text-decoration: underline; color:#0000ff;\">Перейти на github.com</span></a></p></body></html>"))
        self.buttonBox_close.button(QtWidgets.QDialogButtonBox.Close).setText(_translate("About", "Закрыть"))
