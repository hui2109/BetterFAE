# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Process.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Process(object):
    def setupUi(self, Process):
        Process.setObjectName("Process")
        Process.resize(1042, 827)
        self.gridLayout_9 = QtWidgets.QGridLayout(Process)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.groupBox = QtWidgets.QGroupBox(Process)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.buttonLoadTrainingData = QtWidgets.QPushButton(self.groupBox)
        self.buttonLoadTrainingData.setObjectName("buttonLoadTrainingData")
        self.horizontalLayout_2.addWidget(self.buttonLoadTrainingData)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.lineEditTrainingData = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditTrainingData.setObjectName("lineEditTrainingData")
        self.verticalLayout_3.addWidget(self.lineEditTrainingData)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.buttonLoadTestingData = QtWidgets.QPushButton(self.groupBox)
        self.buttonLoadTestingData.setObjectName("buttonLoadTestingData")
        self.horizontalLayout_3.addWidget(self.buttonLoadTestingData)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.lineEditTestingData = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditTestingData.setObjectName("lineEditTestingData")
        self.verticalLayout_4.addWidget(self.lineEditTestingData)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.comboEvent = QtWidgets.QComboBox(self.groupBox)
        self.comboEvent.setObjectName("comboEvent")
        self.gridLayout.addWidget(self.comboEvent, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.comboDuration = QtWidgets.QComboBox(self.groupBox)
        self.comboDuration.setObjectName("comboDuration")
        self.gridLayout.addWidget(self.comboDuration, 1, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.buttonLoad = QtWidgets.QPushButton(self.groupBox)
        self.buttonLoad.setObjectName("buttonLoad")
        self.verticalLayout_6.addWidget(self.buttonLoad)
        self.buttonClear = QtWidgets.QPushButton(self.groupBox)
        self.buttonClear.setObjectName("buttonClear")
        self.verticalLayout_6.addWidget(self.buttonClear)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_10.addWidget(self.groupBox)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(Process)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.textEditDescription = QtWidgets.QTextEdit(Process)
        self.textEditDescription.setObjectName("textEditDescription")
        self.verticalLayout_9.addWidget(self.textEditDescription)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(Process)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.textEditVerbose = QtWidgets.QTextEdit(Process)
        self.textEditVerbose.setObjectName("textEditVerbose")
        self.verticalLayout_2.addWidget(self.textEditVerbose)
        self.verticalLayout_10.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupNormalization = QtWidgets.QGroupBox(Process)
        self.groupNormalization.setObjectName("groupNormalization")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupNormalization)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.checkNormalizeNone = QtWidgets.QCheckBox(self.groupNormalization)
        self.checkNormalizeNone.setObjectName("checkNormalizeNone")
        self.verticalLayout_7.addWidget(self.checkNormalizeNone)
        self.checkNormalizeMinMax = QtWidgets.QCheckBox(self.groupNormalization)
        self.checkNormalizeMinMax.setObjectName("checkNormalizeMinMax")
        self.verticalLayout_7.addWidget(self.checkNormalizeMinMax)
        self.checkNormalizeZscore = QtWidgets.QCheckBox(self.groupNormalization)
        self.checkNormalizeZscore.setObjectName("checkNormalizeZscore")
        self.verticalLayout_7.addWidget(self.checkNormalizeZscore)
        self.checkNormalizeMean = QtWidgets.QCheckBox(self.groupNormalization)
        self.checkNormalizeMean.setChecked(True)
        self.checkNormalizeMean.setObjectName("checkNormalizeMean")
        self.verticalLayout_7.addWidget(self.checkNormalizeMean)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupNormalization)
        self.groupPreprocess = QtWidgets.QGroupBox(Process)
        self.groupPreprocess.setObjectName("groupPreprocess")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupPreprocess)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkDimensionReducePCC = QtWidgets.QCheckBox(self.groupPreprocess)
        self.checkDimensionReducePCC.setChecked(True)
        self.checkDimensionReducePCC.setObjectName("checkDimensionReducePCC")
        self.gridLayout_4.addWidget(self.checkDimensionReducePCC, 1, 0, 1, 1)
        self.checkDimensionReduceNone = QtWidgets.QCheckBox(self.groupPreprocess)
        self.checkDimensionReduceNone.setObjectName("checkDimensionReduceNone")
        self.gridLayout_4.addWidget(self.checkDimensionReduceNone, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupPreprocess)
        self.groupSelector = QtWidgets.QGroupBox(Process)
        self.groupSelector.setObjectName("groupSelector")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupSelector)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupSelector)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.spinBoxMinFeatureNumber = QtWidgets.QSpinBox(self.groupSelector)
        self.spinBoxMinFeatureNumber.setMinimum(1)
        self.spinBoxMinFeatureNumber.setObjectName("spinBoxMinFeatureNumber")
        self.horizontalLayout_6.addWidget(self.spinBoxMinFeatureNumber)
        self.label_8 = QtWidgets.QLabel(self.groupSelector)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.spinBoxMaxFeatureNumber = QtWidgets.QSpinBox(self.groupSelector)
        self.spinBoxMaxFeatureNumber.setMinimum(1)
        self.spinBoxMaxFeatureNumber.setProperty("value", 20)
        self.spinBoxMaxFeatureNumber.setObjectName("spinBoxMaxFeatureNumber")
        self.horizontalLayout_6.addWidget(self.spinBoxMaxFeatureNumber)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkFeatureSelectorNone = QtWidgets.QCheckBox(self.groupSelector)
        self.checkFeatureSelectorNone.setChecked(False)
        self.checkFeatureSelectorNone.setObjectName("checkFeatureSelectorNone")
        self.gridLayout_3.addWidget(self.checkFeatureSelectorNone, 0, 0, 1, 1)
        self.checkFeatureSelectorCluster = QtWidgets.QCheckBox(self.groupSelector)
        self.checkFeatureSelectorCluster.setChecked(True)
        self.checkFeatureSelectorCluster.setObjectName("checkFeatureSelectorCluster")
        self.gridLayout_3.addWidget(self.checkFeatureSelectorCluster, 0, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_3)
        self.gridLayout_8.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupSelector)
        self.groupClassifier = QtWidgets.QGroupBox(Process)
        self.groupClassifier.setObjectName("groupClassifier")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupClassifier)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkCoxPH = QtWidgets.QCheckBox(self.groupClassifier)
        self.checkCoxPH.setChecked(True)
        self.checkCoxPH.setObjectName("checkCoxPH")
        self.gridLayout_5.addWidget(self.checkCoxPH, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupClassifier)
        self.groupBox_2 = QtWidgets.QGroupBox(Process)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.spinCvFold = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinCvFold.setMinimum(2)
        self.spinCvFold.setObjectName("spinCvFold")
        self.horizontalLayout_7.addWidget(self.spinCvFold)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.gridLayout_7.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_4 = QtWidgets.QLabel(Process)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.listOnePipeline = QtWidgets.QListWidget(Process)
        self.listOnePipeline.setObjectName("listOnePipeline")
        self.verticalLayout_11.addWidget(self.listOnePipeline)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.buttonRun = QtWidgets.QPushButton(Process)
        self.buttonRun.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonRun.setObjectName("buttonRun")
        self.verticalLayout_12.addWidget(self.buttonRun)
        self.horizontalLayout.addLayout(self.verticalLayout_12)
        self.gridLayout_9.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Process)
        QtCore.QMetaObject.connectSlotsByName(Process)

    def retranslateUi(self, Process):
        _translate = QtCore.QCoreApplication.translate
        Process.setWindowTitle(_translate("Process", "Model Exploration"))
        self.groupBox.setTitle(_translate("Process", "Load"))
        self.label.setText(_translate("Process", "Training data"))
        self.buttonLoadTrainingData.setText(_translate("Process", "Browse"))
        self.label_2.setText(_translate("Process", "Testing data"))
        self.buttonLoadTestingData.setText(_translate("Process", "Browse"))
        self.label_6.setText(_translate("Process", "Event"))
        self.label_9.setText(_translate("Process", "Duration"))
        self.buttonLoad.setText(_translate("Process", "Load Data"))
        self.buttonClear.setText(_translate("Process", "Clear Data"))
        self.label_3.setText(_translate("Process", "Data Description"))
        self.label_5.setText(_translate("Process", "Verbose"))
        self.groupNormalization.setTitle(_translate("Process", "Normalization"))
        self.checkNormalizeNone.setText(_translate("Process", "None Normalization"))
        self.checkNormalizeMinMax.setText(_translate("Process", "MinMax Normalization"))
        self.checkNormalizeZscore.setText(_translate("Process", "Z-Score Normalization"))
        self.checkNormalizeMean.setText(_translate("Process", "Mean Normalization"))
        self.groupPreprocess.setTitle(_translate("Process", "Preprocess"))
        self.checkDimensionReducePCC.setText(_translate("Process", "Pearson Correlation Coefficients （0.99）"))
        self.checkDimensionReduceNone.setText(_translate("Process", "None"))
        self.groupSelector.setTitle(_translate("Process", "Feature Selector"))
        self.label_7.setText(_translate("Process", "minNumber"))
        self.label_8.setText(_translate("Process", "maxNumber"))
        self.checkFeatureSelectorNone.setText(_translate("Process", "None"))
        self.checkFeatureSelectorCluster.setText(_translate("Process", "Cluster"))
        self.groupClassifier.setTitle(_translate("Process", "Classifier"))
        self.checkCoxPH.setText(_translate("Process", "CoxPH"))
        self.groupBox_2.setTitle(_translate("Process", "Cross Validation"))
        self.label_10.setText(_translate("Process", "    Fold"))
        self.label_4.setText(_translate("Process", "Pipeline Description"))
        self.buttonRun.setText(_translate("Process", "Run and Save"))
