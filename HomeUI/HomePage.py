# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_HomePage(object):
    def setupUi(self, HomePage):
        HomePage.setObjectName("HomePage")
        HomePage.resize(885, 431)
        self.gridLayout_3 = QtWidgets.QGridLayout(HomePage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelTitle = QtWidgets.QLabel(HomePage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout_4.addWidget(self.labelTitle)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(HomePage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(HomePage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(HomePage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.buttonFeatureExtraction = QtWidgets.QPushButton(HomePage)
        self.buttonFeatureExtraction.setObjectName("buttonFeatureExtraction")
        self.verticalLayout_3.addWidget(self.buttonFeatureExtraction)
        self.buttonFeatureMerge = QtWidgets.QPushButton(HomePage)
        self.buttonFeatureMerge.setObjectName("buttonFeatureMerge")
        self.verticalLayout_3.addWidget(self.buttonFeatureMerge)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonBcFeaturePreprocessing = QtWidgets.QPushButton(HomePage)
        self.buttonBcFeaturePreprocessing.setObjectName("buttonBcFeaturePreprocessing")
        self.verticalLayout.addWidget(self.buttonBcFeaturePreprocessing)
        self.buttonBcModelExploration = QtWidgets.QPushButton(HomePage)
        self.buttonBcModelExploration.setObjectName("buttonBcModelExploration")
        self.verticalLayout.addWidget(self.buttonBcModelExploration)
        self.buttonBcVisulization = QtWidgets.QPushButton(HomePage)
        self.buttonBcVisulization.setObjectName("buttonBcVisulization")
        self.verticalLayout.addWidget(self.buttonBcVisulization)
        self.buttonBcPrediction = QtWidgets.QPushButton(HomePage)
        self.buttonBcPrediction.setObjectName("buttonBcPrediction")
        self.verticalLayout.addWidget(self.buttonBcPrediction)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonSaModelExploration = QtWidgets.QPushButton(HomePage)
        self.buttonSaModelExploration.setObjectName("buttonSaModelExploration")
        self.verticalLayout_2.addWidget(self.buttonSaModelExploration)
        self.buttonSaVisulization = QtWidgets.QPushButton(HomePage)
        self.buttonSaVisulization.setObjectName("buttonSaVisulization")
        self.verticalLayout_2.addWidget(self.buttonSaVisulization)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.label_5 = QtWidgets.QLabel(HomePage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboPlugin = QtWidgets.QComboBox(HomePage)
        self.comboPlugin.setObjectName("comboPlugin")
        self.gridLayout.addWidget(self.comboPlugin, 0, 0, 1, 1)
        self.labelPluginFigure = QtWidgets.QLabel(HomePage)
        self.labelPluginFigure.setText("")
        self.labelPluginFigure.setObjectName("labelPluginFigure")
        self.gridLayout.addWidget(self.labelPluginFigure, 0, 1, 2, 1)
        self.textBrowser = QtWidgets.QTextBrowser(HomePage)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 2, 2, 1)
        self.buttonPluginRun = QtWidgets.QPushButton(HomePage)
        self.buttonPluginRun.setObjectName("buttonPluginRun")
        self.gridLayout.addWidget(self.buttonPluginRun, 1, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 2)
        self.verticalLayout_4.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelIntroduction = QtWidgets.QLabel(HomePage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.labelIntroduction.setFont(font)
        self.labelIntroduction.setTextFormat(QtCore.Qt.AutoText)
        self.labelIntroduction.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIntroduction.setObjectName("labelIntroduction")
        self.horizontalLayout.addWidget(self.labelIntroduction)
        self.labelIntroduction_2 = QtWidgets.QLabel(HomePage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.labelIntroduction_2.setFont(font)
        self.labelIntroduction_2.setTextFormat(QtCore.Qt.AutoText)
        self.labelIntroduction_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIntroduction_2.setObjectName("labelIntroduction_2")
        self.horizontalLayout.addWidget(self.labelIntroduction_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(HomePage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        _translate = QtCore.QCoreApplication.translate
        HomePage.setWindowTitle(_translate("HomePage", "FeAture Explorer (Research Used Only)"))
        self.labelTitle.setText(_translate("HomePage", "FeAture Explorer (FAE)"))
        self.label.setText(_translate("HomePage", "Feature Extraction"))
        self.label_2.setText(_translate("HomePage", "Binay Classification"))
        self.label_3.setText(_translate("HomePage", "Survival Analysis"))
        self.buttonFeatureExtraction.setText(_translate("HomePage", "Feature Extraction"))
        self.buttonFeatureMerge.setText(_translate("HomePage", "Feature Merge"))
        self.buttonBcFeaturePreprocessing.setText(_translate("HomePage", "Feature Preprocessing"))
        self.buttonBcModelExploration.setText(_translate("HomePage", "Model Exploration"))
        self.buttonBcVisulization.setText(_translate("HomePage", "Visulization"))
        self.buttonBcPrediction.setText(_translate("HomePage", "External Prediction"))
        self.buttonSaModelExploration.setText(_translate("HomePage", "Model Exploration"))
        self.buttonSaVisulization.setText(_translate("HomePage", "Visulization"))
        self.label_5.setText(_translate("HomePage", "Plugins"))
        self.buttonPluginRun.setText(_translate("HomePage", "Run Plugin"))
        self.labelIntroduction.setText(_translate("HomePage", "Yang Song (songyangmri@gmail.com)\n"
"Jing Zhang (zhangjingmri@gmail.com)\n"
"Chengxiu Zhang (cxzhang@phy.ecnu.edu.cn)\n"
"Guang Yang (gyang@phy.ecnu.edu.cn)"))
        self.labelIntroduction_2.setText(_translate("HomePage", "Shanghai Key Laboratory of Magnetic Resonance\n"
"East China Normal University\n"
"3663, Zhongshan North Road. Shanghai, China, 200062"))
        self.label_4.setText(_translate("HomePage", "Song, Yang et al. FeAture Explorer: A tool for developing and comparing radiomics models. PLoS ONE 15 (2020)"))
