# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FeatureMerge.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_FeatureMerge(object):
    def setupUi(self, FeatureMerge):
        FeatureMerge.setObjectName("FeatureMerge")
        FeatureMerge.resize(771, 571)
        self.gridLayout_4 = QtWidgets.QGridLayout(FeatureMerge)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(FeatureMerge)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditFeature1Path = QtWidgets.QLineEdit(FeatureMerge)
        self.lineEditFeature1Path.setObjectName("lineEditFeature1Path")
        self.gridLayout.addWidget(self.lineEditFeature1Path, 0, 1, 1, 1)
        self.buttonLoadFeatureMatrix1 = QtWidgets.QPushButton(FeatureMerge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonLoadFeatureMatrix1.sizePolicy().hasHeightForWidth())
        self.buttonLoadFeatureMatrix1.setSizePolicy(sizePolicy)
        self.buttonLoadFeatureMatrix1.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.buttonLoadFeatureMatrix1.setFont(font)
        self.buttonLoadFeatureMatrix1.setObjectName("buttonLoadFeatureMatrix1")
        self.gridLayout.addWidget(self.buttonLoadFeatureMatrix1, 0, 2, 1, 1)
        self.textEditDescription = QtWidgets.QTextEdit(FeatureMerge)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.textEditDescription.setFont(font)
        self.textEditDescription.setObjectName("textEditDescription")
        self.gridLayout.addWidget(self.textEditDescription, 0, 3, 2, 1)
        self.label_2 = QtWidgets.QLabel(FeatureMerge)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditFeature2Path = QtWidgets.QLineEdit(FeatureMerge)
        self.lineEditFeature2Path.setObjectName("lineEditFeature2Path")
        self.gridLayout.addWidget(self.lineEditFeature2Path, 1, 1, 1, 1)
        self.buttonLoadFeatureMatrix2 = QtWidgets.QPushButton(FeatureMerge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonLoadFeatureMatrix2.sizePolicy().hasHeightForWidth())
        self.buttonLoadFeatureMatrix2.setSizePolicy(sizePolicy)
        self.buttonLoadFeatureMatrix2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.buttonLoadFeatureMatrix2.setFont(font)
        self.buttonLoadFeatureMatrix2.setObjectName("buttonLoadFeatureMatrix2")
        self.gridLayout.addWidget(self.buttonLoadFeatureMatrix2, 1, 2, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 2)
        self.gridLayout.setColumnMinimumWidth(2, 1)
        self.gridLayout.setColumnMinimumWidth(3, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableFeature1 = QtWidgets.QTableWidget(FeatureMerge)
        self.tableFeature1.setObjectName("tableFeature1")
        self.tableFeature1.setColumnCount(0)
        self.tableFeature1.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableFeature1, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(FeatureMerge)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.tableFeature2 = QtWidgets.QTableWidget(FeatureMerge)
        self.tableFeature2.setObjectName("tableFeature2")
        self.tableFeature2.setColumnCount(0)
        self.tableFeature2.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableFeature2, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(FeatureMerge)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioMergeTypeFeatures = QtWidgets.QRadioButton(FeatureMerge)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.radioMergeTypeFeatures.setFont(font)
        self.radioMergeTypeFeatures.setObjectName("radioMergeTypeFeatures")
        self.gridLayout_3.addWidget(self.radioMergeTypeFeatures, 0, 0, 1, 1)
        self.radioMergeTypeCases = QtWidgets.QRadioButton(FeatureMerge)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.radioMergeTypeCases.setFont(font)
        self.radioMergeTypeCases.setObjectName("radioMergeTypeCases")
        self.gridLayout_3.addWidget(self.radioMergeTypeCases, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(FeatureMerge)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEditPreName1 = QtWidgets.QLineEdit(FeatureMerge)
        self.lineEditPreName1.setObjectName("lineEditPreName1")
        self.gridLayout_3.addWidget(self.lineEditPreName1, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(FeatureMerge)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEditPreName2 = QtWidgets.QLineEdit(FeatureMerge)
        self.lineEditPreName2.setObjectName("lineEditPreName2")
        self.gridLayout_3.addWidget(self.lineEditPreName2, 2, 1, 1, 1)
        self.gridLayout_3.setColumnMinimumWidth(0, 1)
        self.gridLayout_3.setColumnMinimumWidth(1, 2)
        self.gridLayout_3.setColumnMinimumWidth(2, 3)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setColumnStretch(2, 3)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.buttonMerge = QtWidgets.QPushButton(FeatureMerge)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonMerge.sizePolicy().hasHeightForWidth())
        self.buttonMerge.setSizePolicy(sizePolicy)
        self.buttonMerge.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.buttonMerge.setFont(font)
        self.buttonMerge.setObjectName("buttonMerge")
        self.verticalLayout.addWidget(self.buttonMerge)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(FeatureMerge)
        QtCore.QMetaObject.connectSlotsByName(FeatureMerge)

    def retranslateUi(self, FeatureMerge):
        _translate = QtCore.QCoreApplication.translate
        FeatureMerge.setWindowTitle(_translate("FeatureMerge", "Feature Merge"))
        self.label.setText(_translate("FeatureMerge", "Feature Matrix 1"))
        self.buttonLoadFeatureMatrix1.setText(_translate("FeatureMerge", "Load"))
        self.textEditDescription.setHtml(_translate("FeatureMerge", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:\'Adobe Devanagari\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:6pt;\">NOTE: Make sure the case ID is in the first columne.</span></p></body></html>"))
        self.label_2.setText(_translate("FeatureMerge", "Feature Matrix 2"))
        self.buttonLoadFeatureMatrix2.setText(_translate("FeatureMerge", "Load"))
        self.label_5.setText(_translate("FeatureMerge", "Feature Matrix 1"))
        self.label_6.setText(_translate("FeatureMerge", "Feature Matrix 2"))
        self.radioMergeTypeFeatures.setText(_translate("FeatureMerge", "Merge Feature"))
        self.radioMergeTypeCases.setText(_translate("FeatureMerge", "Merge Case"))
        self.label_3.setText(_translate("FeatureMerge", "Add PreName in Feature Matrix 1"))
        self.label_4.setText(_translate("FeatureMerge", "Add PreName in Feature Matrix 2"))
        self.buttonMerge.setText(_translate("FeatureMerge", "Merge"))
