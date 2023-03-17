from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

import os
import maya.cmds as cmds
import openai

class mayaGpt(MayaQWidgetDockableMixin, QWidget):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent=parent)

		if not self.objectName():
			self.setObjectName("mayaGpt")
		Form = self

		## OpenAi settings
		openai.api_key = "API KEY"
		self.model_engine = "text-davinci-003"
		self.preprompt = "Create a script in Python for Maya with no comments that creates: "
		self.prompt = ""
		self.postprompt = ". Use real name and existed objects in the scene."
		self.max_tokens = 2048
		self.temperature = 0.2

		# UPDATE FROM HERE
		Form.resize(820, 160)
		self.verticalLayout_2 = QVBoxLayout(Form)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.promptEdt = QPlainTextEdit(Form)
		self.promptEdt.setObjectName(u"promptEdt")
		font = QFont()
		font.setPointSize(12)
		self.promptEdt.setFont(font)
		self.promptEdt.setTabChangesFocus(True)
		self.promptEdt.setLineWrapMode(QPlainTextEdit.WidgetWidth)

		self.verticalLayout.addWidget(self.promptEdt)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout.addItem(self.horizontalSpacer)

		self.execBtn = QPushButton(Form)
		self.execBtn.setObjectName(u"execBtn")

		self.horizontalLayout.addWidget(self.execBtn)

		self.closeBtn = QPushButton(Form)
		self.closeBtn.setObjectName(u"closeBtn")

		self.horizontalLayout.addWidget(self.closeBtn)


		self.verticalLayout.addLayout(self.horizontalLayout)


		self.horizontalLayout_3.addLayout(self.verticalLayout)

		self.groupBox = QGroupBox(Form)
		self.groupBox.setObjectName(u"groupBox")
		self.verticalLayout_3 = QVBoxLayout(self.groupBox)
		self.verticalLayout_3.setObjectName(u"verticalLayout_3")
		self.horizontalLayout_5 = QHBoxLayout()
		self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
		self.label_2 = QLabel(self.groupBox)
		self.label_2.setObjectName(u"label_2")

		self.horizontalLayout_5.addWidget(self.label_2)

		self.modelCbox = QComboBox(self.groupBox)
		self.modelCbox.addItem("")
		self.modelCbox.addItem("")
		self.modelCbox.addItem("")
		self.modelCbox.setObjectName(u"modelCbox")

		self.horizontalLayout_5.addWidget(self.modelCbox)


		self.verticalLayout_3.addLayout(self.horizontalLayout_5)

		self.horizontalLayout_6 = QHBoxLayout()
		self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
		self.label_3 = QLabel(self.groupBox)
		self.label_3.setObjectName(u"label_3")
		self.label_3.setLayoutDirection(Qt.LeftToRight)

		self.horizontalLayout_6.addWidget(self.label_3)

		self.maxTokensSpn = QSpinBox(self.groupBox)
		self.maxTokensSpn.setObjectName(u"maxTokensSpn")
		self.maxTokensSpn.setMaximum(9999999)
		self.maxTokensSpn.setValue(1024)

		self.horizontalLayout_6.addWidget(self.maxTokensSpn)


		self.verticalLayout_3.addLayout(self.horizontalLayout_6)

		self.horizontalLayout_4 = QHBoxLayout()
		self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
		self.label = QLabel(self.groupBox)
		self.label.setObjectName(u"label")
		self.label.setLayoutDirection(Qt.LeftToRight)

		self.horizontalLayout_4.addWidget(self.label)

		self.temperatureSpn = QDoubleSpinBox(self.groupBox)
		self.temperatureSpn.setObjectName(u"temperatureSpn")
		self.temperatureSpn.setDecimals(1)
		self.temperatureSpn.setMaximum(1.000000000000000)
		self.temperatureSpn.setSingleStep(0.100000000000000)
		self.temperatureSpn.setValue(0.200000000000000)

		self.horizontalLayout_4.addWidget(self.temperatureSpn)


		self.verticalLayout_3.addLayout(self.horizontalLayout_4)

		self.showScriptChk = QCheckBox(self.groupBox)
		self.showScriptChk.setObjectName(u"showScriptChk")
		self.showScriptChk.setChecked(True)

		self.verticalLayout_3.addWidget(self.showScriptChk)

		self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.verticalLayout_3.addItem(self.verticalSpacer)


		self.horizontalLayout_3.addWidget(self.groupBox)

		self.horizontalLayout_3.setStretch(0, 1)

		self.verticalLayout_2.addLayout(self.horizontalLayout_3)


		self.retranslateUi(Form)

		## CONNECTIONS
		self.execBtn.clicked.connect(self.execScript)
		self.closeBtn.clicked.connect(self.close)


    # setupUi

	def retranslateUi(self, Form):
		Form.setWindowTitle(QCoreApplication.translate("Form", u"MayaGPT", None))
		self.promptEdt.setPlainText("")
		self.execBtn.setText(QCoreApplication.translate("Form", u"Execute", None))
		self.closeBtn.setText(QCoreApplication.translate("Form", u"Close", None))
		self.groupBox.setTitle(QCoreApplication.translate("Form", u"Settings:", None))
		self.label_2.setText(QCoreApplication.translate("Form", u"Engine Model:", None))
		self.modelCbox.setItemText(0, QCoreApplication.translate("Form", u"text-davinci-003", None))
		self.modelCbox.setItemText(1, QCoreApplication.translate("Form", u"code-davinci-002", None))
		self.modelCbox.setItemText(2, QCoreApplication.translate("Form", u"text-davinci-002", None))

		self.label_3.setText(QCoreApplication.translate("Form", u"Max Tokens:", None))
		self.label.setText(QCoreApplication.translate("Form", u"Temperature:", None))
		self.showScriptChk.setText(QCoreApplication.translate("Form", u"Show generated script in the log", None))
	# retranslateUi

	def run(self):
		self.show(dockable=True)
		self.promptEdt.setFocus()

	def close(self):
		self.hide()

	def execScript(self):
		self.prompt = self.promptEdt.toPlainText()
		if self.prompt != "":
			self.sendRequest()
		else:
			cmds.confirmDialog(m="Please write some prompt before execute.")

	def sendRequest(self):
		self.model_engine = self.modelCbox.currentText()
		self.max_tokens = self.max_tokens
		self.temperature = self.temperatureSpn.value()

		self.makeLessHuman()

		response = openai.Completion.create(
			engine = self.model_engine,
			prompt = self.preprompt + self.prompt + self.postprompt,
			n=1,
			stop=None,
			max_tokens = self.max_tokens,
			temperature = self.temperature
		)

		result = response.choices[0].text
		
		if self.showScriptChk.isChecked():
			print(result)

		try:
			exec(result)
		except Exception as e:
			self.fixError(e, result)


	def makeLessHuman(self):
		prompt = self.prompt

		# And
		prompt = prompt.replace(" and ", ". ")

		# to it
		prompt = prompt.replace("to it", "to the object")

		# them
		prompt = prompt.replace("them", "each object")

		self.prompt = prompt

	def fixError(self, e, result):
		confirm = cmds.confirmDialog( title='MayaGPT', message='The generated script has a issue, do you want to try to auto solve it?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )

		if confirm == "Yes":
			prompt = result

			response = openai.Edit.create(
				model = "text-davinci-edit-001",
				input = prompt,
				instruction = "I'm having this error, give me a new code with the error fixed: \n" + str(e),
				temperature = 0.2
			)

			newResult = response.choices[0].text
			exec(newResult)


mayaGptDlg = mayaGpt()
mayaGptDlg.run()
