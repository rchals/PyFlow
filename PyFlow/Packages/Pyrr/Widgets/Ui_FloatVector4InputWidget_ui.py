# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\GIT\PyFlow\PyFlow\Packages\Pyrr\Widgets\FloatVector4InputWidget_ui.ui',
# licensing of 'e:\GIT\PyFlow\PyFlow\Packages\Pyrr\Widgets\FloatVector4InputWidget_ui.ui' applies.
#
# Created: Sun Mar 10 22:43:58 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(142, 98)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dsbX = QtWidgets.QDoubleSpinBox(Form)
        self.dsbX.setObjectName("dsbX")
        self.horizontalLayout.addWidget(self.dsbX)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.dsbY = QtWidgets.QDoubleSpinBox(Form)
        self.dsbY.setObjectName("dsbY")
        self.horizontalLayout_2.addWidget(self.dsbY)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.dsbZ = QtWidgets.QDoubleSpinBox(Form)
        self.dsbZ.setObjectName("dsbZ")
        self.horizontalLayout_3.addWidget(self.dsbZ)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.dsbW = QtWidgets.QDoubleSpinBox(Form)
        self.dsbW.setObjectName("dsbW")
        self.horizontalLayout_4.addWidget(self.dsbW)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pbReset = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbReset.sizePolicy().hasHeightForWidth())
        self.pbReset.setSizePolicy(sizePolicy)
        self.pbReset.setMaximumSize(QtCore.QSize(25, 25))
        self.pbReset.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbReset.setIcon(icon)
        self.pbReset.setObjectName("pbReset")
        self.horizontalLayout_5.addWidget(self.pbReset)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "x", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "y", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "z", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "w", None, -1))
        self.pbReset.setToolTip(QtWidgets.QApplication.translate("Form", "Reset to defaults", None, -1))

import nodes_res_rc