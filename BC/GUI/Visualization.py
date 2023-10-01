# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Visualization.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Visualization(object):
    def setupUi(self, Visualization):
        Visualization.setObjectName("Visualization")
        Visualization.resize(1272, 773)
        self.gridLayout_4 = QtWidgets.QGridLayout(Visualization)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonLoadResult = QtWidgets.QPushButton(Visualization)
        self.buttonLoadResult.setObjectName("buttonLoadResult")
        self.verticalLayout.addWidget(self.buttonLoadResult)
        self.buttonClearResult = QtWidgets.QPushButton(Visualization)
        self.buttonClearResult.setEnabled(False)
        self.buttonClearResult.setObjectName("buttonClearResult")
        self.verticalLayout.addWidget(self.buttonClearResult)
        self.lineEditResultPath = QtWidgets.QLineEdit(Visualization)
        self.lineEditResultPath.setObjectName("lineEditResultPath")
        self.verticalLayout.addWidget(self.lineEditResultPath)
        self.textEditDescription = QtWidgets.QTextEdit(Visualization)
        self.textEditDescription.setObjectName("textEditDescription")
        self.verticalLayout.addWidget(self.textEditDescription)
        self.buttonSave = QtWidgets.QPushButton(Visualization)
        self.buttonSave.setEnabled(False)
        self.buttonSave.setObjectName("buttonSave")
        self.verticalLayout.addWidget(self.buttonSave)
        self.buttonGenerateDescription = QtWidgets.QPushButton(Visualization)
        self.buttonGenerateDescription.setEnabled(False)
        self.buttonGenerateDescription.setObjectName("buttonGenerateDescription")
        self.verticalLayout.addWidget(self.buttonGenerateDescription)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(Visualization)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.comboSheet = QtWidgets.QComboBox(Visualization)
        self.comboSheet.setObjectName("comboSheet")
        self.verticalLayout_2.addWidget(self.comboSheet)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.checkMaxFeatureNumber = QtWidgets.QCheckBox(Visualization)
        self.checkMaxFeatureNumber.setObjectName("checkMaxFeatureNumber")
        self.verticalLayout_2.addWidget(self.checkMaxFeatureNumber)
        self.label = QtWidgets.QLabel(Visualization)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_8 = QtWidgets.QLabel(Visualization)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.tableClinicalStatistic = QtWidgets.QTableWidget(Visualization)
        self.tableClinicalStatistic.setObjectName("tableClinicalStatistic")
        self.tableClinicalStatistic.setColumnCount(0)
        self.tableClinicalStatistic.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableClinicalStatistic)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(Visualization)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.canvasROC = MatplotlibWidget(Visualization)
        self.canvasROC.setMinimumSize(QtCore.QSize(400, 400))
        self.canvasROC.setObjectName("canvasROC")
        self.verticalLayout_3.addWidget(self.canvasROC)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkROCCVTrain = QtWidgets.QCheckBox(Visualization)
        self.checkROCCVTrain.setObjectName("checkROCCVTrain")
        self.horizontalLayout_3.addWidget(self.checkROCCVTrain)
        self.checkROCCVValidation = QtWidgets.QCheckBox(Visualization)
        self.checkROCCVValidation.setObjectName("checkROCCVValidation")
        self.horizontalLayout_3.addWidget(self.checkROCCVValidation)
        self.checkROCTrain = QtWidgets.QCheckBox(Visualization)
        self.checkROCTrain.setObjectName("checkROCTrain")
        self.horizontalLayout_3.addWidget(self.checkROCTrain)
        self.checkROCTest = QtWidgets.QCheckBox(Visualization)
        self.checkROCTest.setObjectName("checkROCTest")
        self.horizontalLayout_3.addWidget(self.checkROCTest)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinBoxFeatureNumber = QtWidgets.QSpinBox(Visualization)
        self.spinBoxFeatureNumber.setObjectName("spinBoxFeatureNumber")
        self.gridLayout.addWidget(self.spinBoxFeatureNumber, 1, 2, 1, 1)
        self.comboFeatureSelector = QtWidgets.QComboBox(Visualization)
        self.comboFeatureSelector.setObjectName("comboFeatureSelector")
        self.gridLayout.addWidget(self.comboFeatureSelector, 1, 1, 1, 1)
        self.comboClassifier = QtWidgets.QComboBox(Visualization)
        self.comboClassifier.setObjectName("comboClassifier")
        self.gridLayout.addWidget(self.comboClassifier, 1, 0, 1, 1)
        self.comboDimensionReduction = QtWidgets.QComboBox(Visualization)
        self.comboDimensionReduction.setObjectName("comboDimensionReduction")
        self.gridLayout.addWidget(self.comboDimensionReduction, 0, 2, 1, 1)
        self.comboNormalizer = QtWidgets.QComboBox(Visualization)
        self.comboNormalizer.setObjectName("comboNormalizer")
        self.gridLayout.addWidget(self.comboNormalizer, 0, 1, 1, 1)
        self.comboShowType = QtWidgets.QComboBox(Visualization)
        self.comboShowType.setObjectName("comboShowType")
        self.gridLayout.addWidget(self.comboShowType, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(Visualization)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.canvasPlot = MatplotlibWidget(Visualization)
        self.canvasPlot.setMinimumSize(QtCore.QSize(400, 400))
        self.canvasPlot.setObjectName("canvasPlot")
        self.verticalLayout_4.addWidget(self.canvasPlot)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkPlotCVTrain = QtWidgets.QCheckBox(Visualization)
        self.checkPlotCVTrain.setObjectName("checkPlotCVTrain")
        self.horizontalLayout_4.addWidget(self.checkPlotCVTrain)
        self.checkPlotCVValidation = QtWidgets.QCheckBox(Visualization)
        self.checkPlotCVValidation.setObjectName("checkPlotCVValidation")
        self.horizontalLayout_4.addWidget(self.checkPlotCVValidation)
        self.checkPlotTrain = QtWidgets.QCheckBox(Visualization)
        self.checkPlotTrain.setObjectName("checkPlotTrain")
        self.horizontalLayout_4.addWidget(self.checkPlotTrain)
        self.checkPlotTest = QtWidgets.QCheckBox(Visualization)
        self.checkPlotTest.setObjectName("checkPlotTest")
        self.horizontalLayout_4.addWidget(self.checkPlotTest)
        self.checkPlotOneSE = QtWidgets.QCheckBox(Visualization)
        self.checkPlotOneSE.setObjectName("checkPlotOneSE")
        self.horizontalLayout_4.addWidget(self.checkPlotOneSE)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(Visualization)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.comboPlotY = QtWidgets.QComboBox(Visualization)
        self.comboPlotY.setObjectName("comboPlotY")
        self.gridLayout_2.addWidget(self.comboPlotY, 0, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(Visualization)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 2)
        self.comboPlotX = QtWidgets.QComboBox(Visualization)
        self.comboPlotX.setObjectName("comboPlotX")
        self.gridLayout_2.addWidget(self.comboPlotX, 0, 5, 1, 2)
        self.comboPlotNormalizer = QtWidgets.QComboBox(Visualization)
        self.comboPlotNormalizer.setObjectName("comboPlotNormalizer")
        self.gridLayout_2.addWidget(self.comboPlotNormalizer, 1, 0, 1, 2)
        self.comboPlotDimensionReduction = QtWidgets.QComboBox(Visualization)
        self.comboPlotDimensionReduction.setObjectName("comboPlotDimensionReduction")
        self.gridLayout_2.addWidget(self.comboPlotDimensionReduction, 1, 2, 1, 2)
        self.comboPlotFeatureSelector = QtWidgets.QComboBox(Visualization)
        self.comboPlotFeatureSelector.setObjectName("comboPlotFeatureSelector")
        self.gridLayout_2.addWidget(self.comboPlotFeatureSelector, 1, 4, 1, 2)
        self.comboPlotClassifier = QtWidgets.QComboBox(Visualization)
        self.comboPlotClassifier.setObjectName("comboPlotClassifier")
        self.gridLayout_2.addWidget(self.comboPlotClassifier, 1, 6, 1, 2)
        self.spinPlotFeatureNumber = QtWidgets.QSpinBox(Visualization)
        self.spinPlotFeatureNumber.setObjectName("spinPlotFeatureNumber")
        self.gridLayout_2.addWidget(self.spinPlotFeatureNumber, 1, 8, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(Visualization)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.canvasFeature = MatplotlibWidget(Visualization)
        self.canvasFeature.setMinimumSize(QtCore.QSize(400, 400))
        self.canvasFeature.setObjectName("canvasFeature")
        self.verticalLayout_5.addWidget(self.canvasFeature)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioContributionFeatureSelector = QtWidgets.QRadioButton(Visualization)
        self.radioContributionFeatureSelector.setChecked(True)
        self.radioContributionFeatureSelector.setObjectName("radioContributionFeatureSelector")
        self.horizontalLayout_5.addWidget(self.radioContributionFeatureSelector)
        self.radioContributionClassifier = QtWidgets.QRadioButton(Visualization)
        self.radioContributionClassifier.setObjectName("radioContributionClassifier")
        self.horizontalLayout_5.addWidget(self.radioContributionClassifier)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboContributionFeatureSelector = QtWidgets.QComboBox(Visualization)
        self.comboContributionFeatureSelector.setObjectName("comboContributionFeatureSelector")
        self.gridLayout_3.addWidget(self.comboContributionFeatureSelector, 1, 1, 1, 1)
        self.comboContributionClassifier = QtWidgets.QComboBox(Visualization)
        self.comboContributionClassifier.setObjectName("comboContributionClassifier")
        self.gridLayout_3.addWidget(self.comboContributionClassifier, 2, 1, 1, 1)
        self.spinContributeFeatureNumber = QtWidgets.QSpinBox(Visualization)
        self.spinContributeFeatureNumber.setMinimum(1)
        self.spinContributeFeatureNumber.setObjectName("spinContributeFeatureNumber")
        self.gridLayout_3.addWidget(self.spinContributeFeatureNumber, 1, 2, 1, 1)
        self.comboContributionNormalizor = QtWidgets.QComboBox(Visualization)
        self.comboContributionNormalizor.setObjectName("comboContributionNormalizor")
        self.gridLayout_3.addWidget(self.comboContributionNormalizor, 1, 0, 1, 1)
        self.comboContributionDimension = QtWidgets.QComboBox(Visualization)
        self.comboContributionDimension.setObjectName("comboContributionDimension")
        self.gridLayout_3.addWidget(self.comboContributionDimension, 2, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.retranslateUi(Visualization)
        QtCore.QMetaObject.connectSlotsByName(Visualization)

    def retranslateUi(self, Visualization):
        _translate = QtCore.QCoreApplication.translate
        Visualization.setWindowTitle(_translate("Visualization", "Visualization"))
        self.buttonLoadResult.setText(_translate("Visualization", "Load"))
        self.buttonClearResult.setText(_translate("Visualization", "Clear"))
        self.buttonSave.setText(_translate("Visualization", "Save Figure"))
        self.buttonGenerateDescription.setText(_translate("Visualization", "Generate Description"))
        self.label_7.setText(_translate("Visualization", "Show:"))
        self.checkMaxFeatureNumber.setText(_translate("Visualization", "Estimate"))
        self.label.setText(_translate("Visualization", "model based"))
        self.label_8.setText(_translate("Visualization", "on val by 1-SE"))
        self.label_2.setText(_translate("Visualization", "ROC Curve / Result"))
        self.checkROCCVTrain.setText(_translate("Visualization", "CV Training"))
        self.checkROCCVValidation.setText(_translate("Visualization", "Validation"))
        self.checkROCTrain.setText(_translate("Visualization", "Training"))
        self.checkROCTest.setText(_translate("Visualization", "Test"))
        self.label_3.setText(_translate("Visualization", "Hyper Parameters Relationship"))
        self.checkPlotCVTrain.setText(_translate("Visualization", "CV Training"))
        self.checkPlotCVValidation.setText(_translate("Visualization", "Validation"))
        self.checkPlotTrain.setText(_translate("Visualization", "Training"))
        self.checkPlotTest.setText(_translate("Visualization", "Test"))
        self.checkPlotOneSE.setText(_translate("Visualization", "1-SE"))
        self.label_5.setText(_translate("Visualization", "Y-Label"))
        self.label_6.setText(_translate("Visualization", "X-Label"))
        self.label_4.setText(_translate("Visualization", "Feature Contribution"))
        self.radioContributionFeatureSelector.setText(_translate("Visualization", "Feature Selector"))
        self.radioContributionClassifier.setText(_translate("Visualization", "Classifier"))
from MatplotlibWidget import MatplotlibWidget
