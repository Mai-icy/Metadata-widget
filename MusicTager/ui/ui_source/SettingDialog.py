# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingDialog(object):
    def setupUi(self, MetadataDialogSetting):
        MetadataDialogSetting.setObjectName("MetadataDialogSetting")
        MetadataDialogSetting.resize(400, 221)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        MetadataDialogSetting.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(MetadataDialogSetting)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(MetadataDialogSetting)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.api_comboBox = QtWidgets.QComboBox(MetadataDialogSetting)
        self.api_comboBox.setObjectName("api_comboBox")
        self.api_comboBox.addItem("")
        self.api_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.api_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.is_download_lrc_checkBox = QtWidgets.QCheckBox(MetadataDialogSetting)
        self.is_download_lrc_checkBox.setObjectName("is_download_lrc_checkBox")
        self.verticalLayout.addWidget(self.is_download_lrc_checkBox)
        self.is_rename_file_checkBox = QtWidgets.QCheckBox(MetadataDialogSetting)
        self.is_rename_file_checkBox.setObjectName("is_rename_file_checkBox")
        self.verticalLayout.addWidget(self.is_rename_file_checkBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.auto_button = QtWidgets.QPushButton(MetadataDialogSetting)
        self.auto_button.setObjectName("auto_button")
        self.horizontalLayout_2.addWidget(self.auto_button)
        self.label_2 = QtWidgets.QLabel(MetadataDialogSetting)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(MetadataDialogSetting)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MetadataDialogSetting)
        self.buttonBox.accepted.connect(MetadataDialogSetting.accept)
        self.buttonBox.rejected.connect(MetadataDialogSetting.reject)
        QtCore.QMetaObject.connectSlotsByName(MetadataDialogSetting)

    def retranslateUi(self, MetadataDialogSetting):
        _translate = QtCore.QCoreApplication.translate
        MetadataDialogSetting.setWindowTitle(_translate("MetadataDialogSetting", "Dialog"))
        self.label.setText(_translate("MetadataDialogSetting", "元数据来源："))
        self.api_comboBox.setItemText(0, _translate("MetadataDialogSetting", "网易云api"))
        self.api_comboBox.setItemText(1, _translate("MetadataDialogSetting", "酷狗api"))
        self.is_download_lrc_checkBox.setText(_translate("MetadataDialogSetting", "补全同时下载歌词"))
        self.is_rename_file_checkBox.setText(_translate("MetadataDialogSetting", "修改元数据同时修改文件名"))
        self.auto_button.setText(_translate("MetadataDialogSetting", "自动补全元数据"))
        self.label_2.setText(_translate("MetadataDialogSetting", "将会对载入的还未进行补全的文件\n"
"进行补全"))
