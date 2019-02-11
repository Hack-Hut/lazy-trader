# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import qdarkgraystyle
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QTableWidget,QMessageBox, QPushButton, QMainWindow, QWidget, QApplication, QVBoxLayout, QTableWidgetItem, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LazyTrader(QtWidgets.QMainWindow):
    def setupUi(self, LazyTrader):

        LazyTrader.setObjectName("LazyTrader")
        LazyTrader.resize(1574, 988)

        self.centralwidget = QtWidgets.QWidget(LazyTrader)
        self.centralwidget.setObjectName("centralwidget")

        self.widget_left = QtWidgets.QWidget(self.centralwidget)
        self.widget_left.setGeometry(QtCore.QRect(0, 0, 531, 911))
        self.widget_left.setObjectName("widget_left")

        self.tabWidget = QtWidgets.QTabWidget(self.widget_left)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 501, 901))
        self.tabWidget.setObjectName("tabWidget")

        self.tab_action = QtWidgets.QWidget()
        self.tab_action.setObjectName("tab_action")
        self.tbl_actions = QtWidgets.QTableWidget(self.tab_action)
        self.tbl_actions.setGeometry(QtCore.QRect(10, 10, 471, 491))
        self.tbl_actions.setObjectName("tbl_actions")
        self.tbl_actions.setColumnCount(0)
        self.tbl_actions.setRowCount(0)

        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_action)
        self.tabWidget_4.setGeometry(QtCore.QRect(10, 510, 471, 351))
        self.tabWidget_4.setObjectName("tabWidget_4")

        self.tab_trade_actions = QtWidgets.QWidget()
        self.tab_trade_actions.setObjectName("tab_trade_actions")

        self.gridLayoutWidget_16 = QtWidgets.QWidget(self.tab_trade_actions)
        self.gridLayoutWidget_16.setGeometry(QtCore.QRect(10, 100, 441, 211))
        self.gridLayoutWidget_16.setObjectName("gridLayoutWidget_16")

        self.gridLayout_16 = QtWidgets.QGridLayout(self.gridLayoutWidget_16)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")

        self.btn_update_stop_action = QtWidgets.QPushButton(self.gridLayoutWidget_16)
        self.btn_update_stop_action.setObjectName("btn_update_stop_action")
        
        self.gridLayout_17.addWidget(self.btn_update_stop_action, 1, 0, 1, 1)
        
        self.btn_pyramid_action = QtWidgets.QPushButton(self.gridLayoutWidget_16)
        self.btn_pyramid_action.setObjectName("btn_pyramid_action")
        
        self.gridLayout_17.addWidget(self.btn_pyramid_action, 0, 0, 1, 1)
        
        self.label_unit_action = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.label_unit_action.setAlignment(QtCore.Qt.AlignCenter)
        self.label_unit_action.setObjectName("label_unit_action")
        
        self.gridLayout_17.addWidget(self.label_unit_action, 0, 2, 1, 1)
        
        self.spin_action = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_16)
        self.spin_action.setMaximum(99999.0)
        self.spin_action.setObjectName("spin_action")
        
        self.gridLayout_17.addWidget(self.spin_action, 1, 1, 1, 1)
        
        self.spin_pyramid_units = QtWidgets.QSpinBox(self.gridLayoutWidget_16)
        self.spin_pyramid_units.setObjectName("spin_pyramid_units")
        
        self.gridLayout_17.addWidget(self.spin_pyramid_units, 0, 1, 1, 1)
        
        self.spin_open_price_action = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_16)
        self.spin_open_price_action.setMaximum(9999.99)
        self.spin_open_price_action.setObjectName("spin_open_price_action")
        
        self.gridLayout_17.addWidget(self.spin_open_price_action, 2, 1, 1, 1)
        
        self.label_stop_action = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.label_stop_action.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stop_action.setObjectName("label_stop_action")
        
        self.gridLayout_17.addWidget(self.label_stop_action, 1, 2, 1, 1)
        
        self.btn_update_open_action = QtWidgets.QPushButton(self.gridLayoutWidget_16)
        self.btn_update_open_action.setObjectName("btn_update_open_action")
        
        self.gridLayout_17.addWidget(self.btn_update_open_action, 2, 0, 1, 1)
        
        self.label_open_action = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.label_open_action.setAlignment(QtCore.Qt.AlignCenter)
        self.label_open_action.setObjectName("label_open_action")
        
        self.gridLayout_17.addWidget(self.label_open_action, 2, 2, 1, 1)
        
        self.spin_close = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_16)
        self.spin_close.setMaximum(999999.0)
        self.spin_close.setObjectName("spin_close")
        
        self.gridLayout_17.addWidget(self.spin_close, 3, 1, 1, 1)
        
        self.label_close_action = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.label_close_action.setAlignment(QtCore.Qt.AlignCenter)
        self.label_close_action.setObjectName("label_close_action")
        
        self.gridLayout_17.addWidget(self.label_close_action, 3, 2, 1, 1)
        
        self.btn_close_action = QtWidgets.QPushButton(self.gridLayoutWidget_16)
        self.btn_close_action.setObjectName("btn_close_action")
        
        self.gridLayout_17.addWidget(self.btn_close_action, 3, 0, 1, 1)
        
        self.btn_order_open_action = QtWidgets.QPushButton(self.gridLayoutWidget_16)
        self.btn_order_open_action.setObjectName("btn_order_open_action")
        
        self.gridLayout_17.addWidget(self.btn_order_open_action, 4, 0, 1, 1)
        
        self.btn_hit_action = QtWidgets.QPushButton(self.gridLayoutWidget_16)
        self.btn_hit_action.setObjectName("btn_hit_action")
        
        self.gridLayout_17.addWidget(self.btn_hit_action, 4, 1, 1, 1)
        
        self.btn_auto_action = QtWidgets.QPushButton(self.gridLayoutWidget_16)
        
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        self.btn_auto_action.setFont(font)
        self.btn_auto_action.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.btn_auto_action.setAutoFillBackground(False)
        self.btn_auto_action.setObjectName("btn_auto_action")

        self.gridLayout_17.addWidget(self.btn_auto_action, 4, 2, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_17, 0, 0, 1, 1)

        self.picture_action = QtWidgets.QGraphicsView(self.tab_trade_actions)
        self.picture_action.setGeometry(QtCore.QRect(360, 10, 91, 71))
        self.picture_action.setObjectName("picture_action")
        
        self.btn_select_trade_action = QtWidgets.QPushButton(self.tab_trade_actions)
        self.btn_select_trade_action.setGeometry(QtCore.QRect(120, 10, 231, 21))
        self.btn_select_trade_action.setObjectName("btn_select_trade_action")
        
        self.spin_action_id_action = QtWidgets.QSpinBox(self.tab_trade_actions)
        self.spin_action_id_action.setGeometry(QtCore.QRect(10, 10, 101, 22))
        self.spin_action_id_action.setObjectName("spin_action_id_action")
        
        self.label_first_action = QtWidgets.QLabel(self.tab_trade_actions)
        self.label_first_action.setGeometry(QtCore.QRect(10, 50, 341, 16))
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        
        self.label_first_action.setFont(font)
        self.label_first_action.setAlignment(QtCore.Qt.AlignCenter)
        self.label_first_action.setObjectName("label_first_action")
        
        self.label_second_action = QtWidgets.QLabel(self.tab_trade_actions)
        self.label_second_action.setGeometry(QtCore.QRect(10, 70, 351, 16))
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        
        self.label_second_action.setFont(font)
        self.label_second_action.setAlignment(QtCore.Qt.AlignCenter)
        self.label_second_action.setObjectName("label_second_action")
        
        self.tabWidget_4.addTab(self.tab_trade_actions, "")
        
        self.tab_trade_info = QtWidgets.QWidget()
        self.tab_trade_info.setObjectName("tab_trade_info")
        
        self.gridLayoutWidget_15 = QtWidgets.QWidget(self.tab_trade_info)
        self.gridLayoutWidget_15.setGeometry(QtCore.QRect(10, 10, 441, 301))
        self.gridLayoutWidget_15.setObjectName("gridLayoutWidget_15")
        
        self.gridLayout_15 = QtWidgets.QGridLayout(self.gridLayoutWidget_15)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        
        self.label_open_action_info = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.label_open_action_info.setObjectName("label_open_action_info")
        
        self.gridLayout_15.addWidget(self.label_open_action_info, 2, 0, 1, 1)
        
        self.label_stoploss_action_info = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.label_stoploss_action_info.setObjectName("label_stoploss_action_info")
        
        self.gridLayout_15.addWidget(self.label_stoploss_action_info, 0, 0, 1, 1)
        
        self.label_profit_action_info = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.label_profit_action_info.setObjectName("label_profit_action_info")
        
        self.gridLayout_15.addWidget(self.label_profit_action_info, 0, 1, 1, 1)
        
        self.label_type_action_info = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.label_type_action_info.setObjectName("label_type_action_info")
        
        self.gridLayout_15.addWidget(self.label_type_action_info, 1, 1, 1, 1)
        
        self.label_volatility_action_info = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.label_volatility_action_info.setObjectName("label_volatility_action_info")
        
        self.gridLayout_15.addWidget(self.label_volatility_action_info, 1, 0, 1, 1)
        
        self.label_system_action_info = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.label_system_action_info.setObjectName("label_system_action_info")
        
        self.gridLayout_15.addWidget(self.label_system_action_info, 2, 1, 1, 1)
        
        self.label_entry_point_action_info = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.label_entry_point_action_info.setObjectName("label_entry_point_action_info")
        
        self.gridLayout_15.addWidget(self.label_entry_point_action_info, 3, 1, 1, 1)
        
        self.label_stoploss_dis_action_info = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.label_stoploss_dis_action_info.setObjectName("label_stoploss_dis_action_info")
        
        self.gridLayout_15.addWidget(self.label_stoploss_dis_action_info, 3, 0, 1, 1)
        
        self.tabWidget_4.addTab(self.tab_trade_info, "")
        self.tabWidget.addTab(self.tab_action, "")
        
        self.tab_sugested_pos = QtWidgets.QWidget()
        self.tab_sugested_pos.setObjectName("tab_sugested_pos")
        
        self.tbl_sug = QtWidgets.QTableWidget(self.tab_sugested_pos)
        self.tbl_sug.setGeometry(QtCore.QRect(10, 10, 471, 671))
        self.tbl_sug.setObjectName("tbl_sug")
        self.tbl_sug.setColumnCount(0)
        self.tbl_sug.setRowCount(0)
        
        self.gridLayoutWidget_19 = QtWidgets.QWidget(self.tab_sugested_pos)
        self.gridLayoutWidget_19.setGeometry(QtCore.QRect(190, 690, 281, 171))
        self.gridLayoutWidget_19.setObjectName("gridLayoutWidget_19")
        
        self.gridLayout_21 = QtWidgets.QGridLayout(self.gridLayoutWidget_19)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        
        self.label_stop_sug = QtWidgets.QLabel(self.gridLayoutWidget_19)
        self.label_stop_sug.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_stop_sug.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_stop_sug.setObjectName("label_stop_sug")
        
        self.gridLayout_21.addWidget(self.label_stop_sug, 2, 0, 1, 1)
        
        self.btn_opn_sug = QtWidgets.QPushButton(self.gridLayoutWidget_19)
        self.btn_opn_sug.setObjectName("btn_opn_sug")
        
        self.gridLayout_21.addWidget(self.btn_opn_sug, 3, 1, 1, 1)
        
        self.spin_entry_sug = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_19)
        self.spin_entry_sug.setObjectName("spin_entry_sug")
        
        self.gridLayout_21.addWidget(self.spin_entry_sug, 1, 1, 1, 1)
        
        self.label_entry_sug = QtWidgets.QLabel(self.gridLayoutWidget_19)
        self.label_entry_sug.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_entry_sug.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_entry_sug.setObjectName("label_entry_sug")
        
        self.gridLayout_21.addWidget(self.label_entry_sug, 1, 0, 1, 1)
        
        self.spin_stop_sug = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_19)
        self.spin_stop_sug.setObjectName("spin_stop_sug")
        
        self.gridLayout_21.addWidget(self.spin_stop_sug, 2, 1, 1, 1)
        
        self.spin_id_sug = QtWidgets.QSpinBox(self.gridLayoutWidget_19)
        self.spin_id_sug.setObjectName("spin_id_sug")
        
        self.gridLayout_21.addWidget(self.spin_id_sug, 0, 1, 1, 1)
        
        self.label_id_sug = QtWidgets.QLabel(self.gridLayoutWidget_19)
        self.label_id_sug.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_id_sug.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_id_sug.setObjectName("label_id_sug")
        
        self.gridLayout_21.addWidget(self.label_id_sug, 0, 0, 1, 1)

        self.btn_view_chart_sug = QtWidgets.QPushButton(self.gridLayoutWidget_19)
        self.btn_view_chart_sug.setObjectName("btn_view_chart_sug")
        
        self.gridLayout_21.addWidget(self.btn_view_chart_sug, 3, 0, 1, 1)
        
        self.picture_sug = QtWidgets.QGraphicsView(self.tab_sugested_pos)
        self.picture_sug.setGeometry(QtCore.QRect(10, 690, 171, 171))
        self.picture_sug.setObjectName("picture_sug")
        
        self.tabWidget.addTab(self.tab_sugested_pos, "")
        
        self.tab_open_pos = QtWidgets.QWidget()
        self.tab_open_pos.setObjectName("tab_open_pos")
        
        self.tbl_open = QtWidgets.QTableWidget(self.tab_open_pos)
        self.tbl_open.setGeometry(QtCore.QRect(10, 10, 471, 711))
        self.tbl_open.setObjectName("tbl_open")
        self.tbl_open.setColumnCount(0)
        self.tbl_open.setRowCount(0)
        
        self.gridLayoutWidget_18 = QtWidgets.QWidget(self.tab_open_pos)
        self.gridLayoutWidget_18.setGeometry(QtCore.QRect(10, 730, 471, 141))
        self.gridLayoutWidget_18.setObjectName("gridLayoutWidget_18")
        
        self.gridLayout_19 = QtWidgets.QGridLayout(self.gridLayoutWidget_18)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        
        self.btn_close_pos_open = QtWidgets.QPushButton(self.gridLayoutWidget_18)
        self.btn_close_pos_open.setObjectName("btn_close_pos_open")
        
        self.gridLayout_19.addWidget(self.btn_close_pos_open, 3, 1, 1, 1)
        
        self.btn_search_open = QtWidgets.QPushButton(self.gridLayoutWidget_18)
        self.btn_search_open.setObjectName("btn_search_open")
        
        self.gridLayout_19.addWidget(self.btn_search_open, 1, 1, 1, 1)
        
        self.combo_type_open = QtWidgets.QComboBox(self.gridLayoutWidget_18)
        self.combo_type_open.setObjectName("combo_type_open")
        
        self.gridLayout_19.addWidget(self.combo_type_open, 2, 0, 1, 1)
        
        self.btn_search_type_open = QtWidgets.QPushButton(self.gridLayoutWidget_18)
        self.btn_search_type_open.setObjectName("btn_search_type_open")
        
        self.gridLayout_19.addWidget(self.btn_search_type_open, 2, 1, 1, 1)
        
        self.spin_close_pos_open = QtWidgets.QSpinBox(self.gridLayoutWidget_18)
        self.spin_close_pos_open.setObjectName("spin_close_pos_open")
        
        self.gridLayout_19.addWidget(self.spin_close_pos_open, 3, 0, 1, 1)
        
        self.txt_name_open = QtWidgets.QLineEdit(self.gridLayoutWidget_18)
        self.txt_name_open.setObjectName("txt_name_open")
        
        self.gridLayout_19.addWidget(self.txt_name_open, 1, 0, 1, 1)
        
        self.spin_view_chart_open = QtWidgets.QSpinBox(self.gridLayoutWidget_18)
        self.spin_view_chart_open.setObjectName("spin_view_chart_open")
        
        self.gridLayout_19.addWidget(self.spin_view_chart_open, 0, 0, 1, 1)
        
        self.btn_view_chart_open = QtWidgets.QPushButton(self.gridLayoutWidget_18)
        self.btn_view_chart_open.setObjectName("btn_view_chart_open")
        
        self.gridLayout_19.addWidget(self.btn_view_chart_open, 0, 1, 1, 1)
        
        self.tabWidget.addTab(self.tab_open_pos, "")
        
        self.tab_closed_pos = QtWidgets.QWidget()
        self.tab_closed_pos.setObjectName("tab_closed_pos")
        
        self.tbl_closed = QtWidgets.QTableWidget(self.tab_closed_pos)
        self.tbl_closed.setGeometry(QtCore.QRect(10, 10, 471, 771))
        self.tbl_closed.setObjectName("tbl_closed")
        self.tbl_closed.setColumnCount(0)
        self.tbl_closed.setRowCount(0)
        
        self.gridLayoutWidget_17 = QtWidgets.QWidget(self.tab_closed_pos)
        self.gridLayoutWidget_17.setGeometry(QtCore.QRect(10, 800, 471, 61))
        self.gridLayoutWidget_17.setObjectName("gridLayoutWidget_17")
        
        self.gridLayout_18 = QtWidgets.QGridLayout(self.gridLayoutWidget_17)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        
        self.btn_search_closed = QtWidgets.QPushButton(self.gridLayoutWidget_17)
        self.btn_search_closed.setObjectName("btn_search_closed")
        
        self.gridLayout_18.addWidget(self.btn_search_closed, 1, 1, 1, 1)
        
        self.txt_search_closed = QtWidgets.QLineEdit(self.gridLayoutWidget_17)
        self.txt_search_closed.setObjectName("txt_search_closed")
        
        self.gridLayout_18.addWidget(self.txt_search_closed, 1, 0, 1, 1)
        
        self.btn_export_closed = QtWidgets.QPushButton(self.gridLayoutWidget_17)
        self.btn_export_closed.setObjectName("btn_export_closed")
        
        self.gridLayout_18.addWidget(self.btn_export_closed, 2, 1, 1, 1)
        
        self.btn_sort_closed = QtWidgets.QPushButton(self.gridLayoutWidget_17)
        self.btn_sort_closed.setObjectName("btn_sort_closed")
        
        self.gridLayout_18.addWidget(self.btn_sort_closed, 2, 0, 1, 1)
        
        self.tabWidget.addTab(self.tab_closed_pos, "")
        
        self.tab_all_pos = QtWidgets.QWidget()
        self.tab_all_pos.setObjectName("tab_all_pos")
        
        self.tableWidget_7 = QtWidgets.QTableWidget(self.tab_all_pos)
        self.tableWidget_7.setGeometry(QtCore.QRect(10, 10, 471, 751))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        
        self.frame_3 = QtWidgets.QFrame(self.tab_all_pos)
        self.frame_3.setGeometry(QtCore.QRect(10, 770, 471, 81))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.frame_3)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(10, 10, 451, 61))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.btn_search_name_all = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.btn_search_name_all.setObjectName("btn_search_name_all")
        
        self.gridLayout_2.addWidget(self.btn_search_name_all, 1, 1, 1, 1)
        
        self.txt_search_all = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.txt_search_all.setObjectName("txt_search_all")
        
        self.gridLayout_2.addWidget(self.txt_search_all, 1, 0, 1, 1)
        
        self.combo_search_all = QtWidgets.QComboBox(self.gridLayoutWidget_7)
        self.combo_search_all.setObjectName("combo_search_all")
        
        self.gridLayout_2.addWidget(self.combo_search_all, 2, 0, 1, 1)
        
        self.btn_search_type_all = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.btn_search_type_all.setObjectName("btn_search_type_all")
        
        self.gridLayout_2.addWidget(self.btn_search_type_all, 2, 1, 1, 1)
        
        self.tabWidget.addTab(self.tab_all_pos, "")
        
        self.widget_top_right = QtWidgets.QWidget(self.centralwidget)
        self.widget_top_right.setGeometry(QtCore.QRect(530, 0, 1001, 671))
        self.widget_top_right.setObjectName("widget_top_right")
        
        self.tabWidget_2 = QtWidgets.QTabWidget(self.widget_top_right)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 10, 1001, 641))
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setObjectName("tabWidget_2")
        
        self.tab_price_graph = QtWidgets.QWidget()
        self.tab_price_graph.setObjectName("tab_price_graph")
        
        self.frame = QtWidgets.QFrame(self.tab_price_graph)
        self.frame.setGeometry(QtCore.QRect(10, 550, 971, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 971, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.horizontalLayout.addItem(spacerItem)
        
        self.label_stock_name_graph = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_stock_name_graph.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stock_name_graph.setObjectName("label_stock_name_graph")
        
        self.horizontalLayout.addWidget(self.label_stock_name_graph)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.horizontalLayout.addItem(spacerItem1)
        
        self.label_signal_graph = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_signal_graph.setAlignment(QtCore.Qt.AlignCenter)
        self.label_signal_graph.setObjectName("label_signal_graph")
        
        self.horizontalLayout.addWidget(self.label_signal_graph)
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.horizontalLayout.addItem(spacerItem2)
        
        self.btn_vol_graph = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_vol_graph.setObjectName("btn_vol_graph")
        
        self.horizontalLayout.addWidget(self.btn_vol_graph)
        
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.horizontalLayout.addItem(spacerItem3)
        
        self.btn_rsi_graph = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_rsi_graph.setObjectName("btn_rsi_graph")
        
        self.horizontalLayout.addWidget(self.btn_rsi_graph)
        
        self.btn_ma_graph = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_ma_graph.setObjectName("btn_ma_graph")
        
        self.horizontalLayout.addWidget(self.btn_ma_graph)
        
        self.btn_bol_bands_graph = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_bol_bands_graph.setObjectName("btn_bol_bands_graph")
        
        self.horizontalLayout.addWidget(self.btn_bol_bands_graph)
        
        self.btn_macd_graph = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_macd_graph.setObjectName("btn_macd_graph")
        
        self.horizontalLayout.addWidget(self.btn_macd_graph)
        
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.horizontalLayout.addItem(spacerItem4)
        
        self.btn_open_pos_graph = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_open_pos_graph.setObjectName("btn_open_pos_graph")
        
        self.horizontalLayout.addWidget(self.btn_open_pos_graph)
        
        self.btn_close_position_graph = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_close_position_graph.setObjectName("btn_close_position_graph")
        
        self.horizontalLayout.addWidget(self.btn_close_position_graph)
        
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.horizontalLayout.addItem(spacerItem5)
        
        self.frame_8 = QtWidgets.QFrame(self.tab_price_graph)
        self.frame_8.setGeometry(QtCore.QRect(10, 10, 971, 531))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        
        self.tabWidget_2.addTab(self.tab_price_graph, "")
        
        self.tab_portfolio_graph = QtWidgets.QWidget()
        self.tab_portfolio_graph.setObjectName("tab_portfolio_graph")
        
        self.frame_5 = QtWidgets.QFrame(self.tab_portfolio_graph)
        self.frame_5.setGeometry(QtCore.QRect(10, 540, 981, 61))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 151, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.label_unit_size_port = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_unit_size_port.setObjectName("label_unit_size_port")
        
        self.gridLayout.addWidget(self.label_unit_size_port, 2, 0, 1, 1)
        
        self.label_open_port = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_open_port.setObjectName("label_open_port")
        
        self.gridLayout.addWidget(self.label_open_port, 1, 0, 1, 1)
        
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(170, 10, 151, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.label_los_pos_port = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_los_pos_port.setObjectName("label_los_pos_port")
        
        self.gridLayout_3.addWidget(self.label_los_pos_port, 2, 0, 1, 1)
        
        self.label_win_pos_port = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_win_pos_port.setObjectName("label_win_pos_port")
        
        self.gridLayout_3.addWidget(self.label_win_pos_port, 1, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(330, 10, 151, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.label_avg_loss_port = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_avg_loss_port.setObjectName("label_avg_loss_port")
        
        self.gridLayout_4.addWidget(self.label_avg_loss_port, 2, 0, 1, 1)
        
        self.label_avg_win_port = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_avg_win_port.setObjectName("label_avg_win_port")
        
        self.gridLayout_4.addWidget(self.label_avg_win_port, 1, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(490, 10, 151, 41))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        
        self.label_edge_port = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_edge_port.setObjectName("label_edge_port")
        
        self.gridLayout_5.addWidget(self.label_edge_port, 2, 0, 1, 1)
        
        self.label_equity_port = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_equity_port.setObjectName("label_equity_port")
        
        self.gridLayout_5.addWidget(self.label_equity_port, 1, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(650, 10, 151, 41))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        
        self.label_daily_profit_port = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_daily_profit_port.setObjectName("label_daily_profit_port")
        
        self.gridLayout_6.addWidget(self.label_daily_profit_port, 2, 0, 1, 1)
        
        self.label_units_used_port = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_units_used_port.setObjectName("label_units_used_port")
        
        self.gridLayout_6.addWidget(self.label_units_used_port, 1, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(810, 10, 151, 41))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        
        self.label_tot_profit_port = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_tot_profit_port.setObjectName("label_tot_profit_port")
        
        self.gridLayout_7.addWidget(self.label_tot_profit_port, 2, 0, 1, 1)
        
        self.label_month_profit_port = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_month_profit_port.setObjectName("label_month_profit_port")
        
        self.gridLayout_7.addWidget(self.label_month_profit_port, 1, 0, 1, 1)
        
        self.frame_6 = QtWidgets.QFrame(self.tab_portfolio_graph)
        self.frame_6.setGeometry(QtCore.QRect(10, 480, 981, 61))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.frame_6)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(10, 10, 151, 41))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        
        self.btn_acc_growth_port = QtWidgets.QPushButton(self.gridLayoutWidget_8)
        self.btn_acc_growth_port.setObjectName("btn_acc_growth_port")
        
        self.gridLayout_8.addWidget(self.btn_acc_growth_port, 0, 0, 1, 1)
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.frame_6)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(170, 10, 151, 41))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        
        self.btn_acc_volatility_port = QtWidgets.QPushButton(self.gridLayoutWidget_9)
        self.btn_acc_volatility_port.setObjectName("btn_acc_volatility_port")

        self.gridLayout_9.addWidget(self.btn_acc_volatility_port, 0, 0, 1, 1)
        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.frame_6)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(330, 10, 151, 41))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")

        self.btn_win_lose_port = QtWidgets.QPushButton(self.gridLayoutWidget_10)
        self.btn_win_lose_port.setObjectName("btn_win_lose_port")

        self.gridLayout_10.addWidget(self.btn_win_lose_port, 0, 0, 1, 1)
        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.frame_6)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(490, 10, 151, 41))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")

        self.btn_pos_open_port = QtWidgets.QPushButton(self.gridLayoutWidget_11)
        self.btn_pos_open_port.setObjectName("btn_pos_open_port")

        self.gridLayout_11.addWidget(self.btn_pos_open_port, 0, 0, 1, 1)
        self.gridLayoutWidget_12 = QtWidgets.QWidget(self.frame_6)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(650, 10, 151, 41))
        self.gridLayoutWidget_12.setObjectName("gridLayoutWidget_12")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")

        self.btn_s1_s2_port = QtWidgets.QPushButton(self.gridLayoutWidget_12)
        self.btn_s1_s2_port.setObjectName("btn_s1_s2_port")

        self.gridLayout_12.addWidget(self.btn_s1_s2_port, 0, 0, 1, 1)
        self.gridLayoutWidget_13 = QtWidgets.QWidget(self.frame_6)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(810, 10, 151, 41))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget_13")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")

        self.btn_correlation_port = QtWidgets.QPushButton(self.gridLayoutWidget_13)
        self.btn_correlation_port.setObjectName("btn_correlation_port")

        self.gridLayout_13.addWidget(self.btn_correlation_port, 0, 0, 1, 1)

        self.frame_port = QtWidgets.QFrame(self.tab_portfolio_graph)
        self.frame_port.setGeometry(QtCore.QRect(10, 10, 971, 461))
        self.frame_port.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_port.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_port.setObjectName("frame_port")

        self.tabWidget_2.addTab(self.tab_portfolio_graph, "")

        self.tab_notes = QtWidgets.QWidget()
        self.tab_notes.setObjectName("tab_notes")

        self.textBrowser = QtWidgets.QTextBrowser(self.tab_notes)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 971, 461))
        self.textBrowser.setObjectName("textBrowser")

        self.frame_2 = QtWidgets.QFrame(self.tab_notes)
        self.frame_2.setGeometry(QtCore.QRect(10, 480, 971, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.txt_notes = QtWidgets.QLineEdit(self.frame_2)
        self.txt_notes.setGeometry(QtCore.QRect(10, 10, 951, 31))
        self.txt_notes.setObjectName("txt_notes")

        self.widget_3 = QtWidgets.QWidget(self.frame_2)
        self.widget_3.setGeometry(QtCore.QRect(10, 40, 951, 61))
        self.widget_3.setObjectName("widget_3")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 951, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.btn_buy_notes = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_buy_notes.setObjectName("btn_buy_notes")
        
        self.horizontalLayout_2.addWidget(self.btn_buy_notes)
        
        self.btn_sell_notes = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_sell_notes.setObjectName("btn_sell_notes")
        
        self.horizontalLayout_2.addWidget(self.btn_sell_notes)
        
        self.btn_prediction_notes = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_prediction_notes.setObjectName("btn_prediction_notes")
        
        self.horizontalLayout_2.addWidget(self.btn_prediction_notes)
        
        self.btn_submit_notes = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_submit_notes.setObjectName("btn_submit_notes")
        
        self.horizontalLayout_2.addWidget(self.btn_submit_notes)
        
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.horizontalLayout_2.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem7)
        
        self.btn_search_notes = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_search_notes.setObjectName("btn_search_notes")
        
        self.horizontalLayout_2.addWidget(self.btn_search_notes)
        
        self.btn_save_notes = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_save_notes.setObjectName("btn_save_notes")
        
        self.horizontalLayout_2.addWidget(self.btn_save_notes)
        self.tabWidget_2.addTab(self.tab_notes, "")
        self.tab_backtest = QtWidgets.QWidget()
        self.tab_backtest.setObjectName("tab_backtest")
        self.tabWidget_2.addTab(self.tab_backtest, "")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 910, 1531, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.bottom_bar_lay = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.bottom_bar_lay.setContentsMargins(0, 0, 0, 0)
        self.bottom_bar_lay.setObjectName("bottom_bar_lay")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.bottom_bar_lay.addItem(spacerItem8)

        self.label_action_required = QtWidgets.QLabel(self.horizontalLayoutWidget_3)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_action_required.setFont(font)
        self.label_action_required.setObjectName("label_action_required")
        
        self.bottom_bar_lay.addWidget(self.label_action_required)
        
        self.lcd_action_required = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_3)
        self.lcd_action_required.setObjectName("lcd_action_required")
        
        self.bottom_bar_lay.addWidget(self.lcd_action_required)
        
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.bottom_bar_lay.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.bottom_bar_lay.addItem(spacerItem10)
        
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_3)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        
        self.bottom_bar_lay.addWidget(self.progressBar)
        
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.bottom_bar_lay.addItem(spacerItem11)
        
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.bottom_bar_lay.addItem(spacerItem12)

        self.label_last_updated = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_last_updated.setObjectName("label_last_updated")

        self.bottom_bar_lay.addWidget(self.label_last_updated)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.bottom_bar_lay.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.bottom_bar_lay.addItem(spacerItem14)

        self.label_update_time = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_update_time.setObjectName("label_update_time")

        self.bottom_bar_lay.addWidget(self.label_update_time)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.bottom_bar_lay.addItem(spacerItem15)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.bottom_bar_lay.addItem(spacerItem16)
        self.btn_update_df = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_update_df.setObjectName("btn_update_df")
        self.bottom_bar_lay.addWidget(self.btn_update_df)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.bottom_bar_lay.addItem(spacerItem17)
        self.Widget_bot_right = QtWidgets.QTabWidget(self.centralwidget)
        self.Widget_bot_right.setGeometry(QtCore.QRect(530, 650, 1001, 241))
        self.Widget_bot_right.setObjectName("Widget_bot_right")
        self.tab_console = QtWidgets.QWidget()
        self.tab_console.setObjectName("tab_console")
        self.txt_browswer_logs = QtWidgets.QTextBrowser(self.tab_console)
        self.txt_browswer_logs.setGeometry(QtCore.QRect(10, 10, 961, 151))
        self.txt_browswer_logs.setObjectName("txt_browswer_logs")
        self.Widget_Console = QtWidgets.QWidget(self.tab_console)
        self.Widget_Console.setGeometry(QtCore.QRect(10, 170, 961, 31))
        self.Widget_Console.setObjectName("Widget_Console")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.Widget_Console)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 961, 27))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_copy_logs = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.btn_copy_logs.setObjectName("btn_copy_logs")
        self.horizontalLayout_8.addWidget(self.btn_copy_logs)
        self.btn_print_acc_sum = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.btn_print_acc_sum.setObjectName("btn_print_acc_sum")
        self.horizontalLayout_8.addWidget(self.btn_print_acc_sum)
        self.btn_save_logs = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.btn_save_logs.setObjectName("btn_save_logs")
        self.horizontalLayout_8.addWidget(self.btn_save_logs)
        self.Widget_bot_right.addTab(self.tab_console, "")
        self.tab_man_trade = QtWidgets.QWidget()
        self.tab_man_trade.setObjectName("tab_man_trade")
        self.frame_man = QtWidgets.QFrame(self.tab_man_trade)
        self.frame_man.setGeometry(QtCore.QRect(10, 10, 971, 191))
        self.frame_man.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_man.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_man.setObjectName("frame_man")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame_man)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 264, 171))
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayoutWidget_14 = QtWidgets.QWidget(self.frame_man)
        self.gridLayoutWidget_14.setGeometry(QtCore.QRect(290, 10, 661, 171))
        self.gridLayoutWidget_14.setObjectName("gridLayoutWidget_14")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_indices_man = QtWidgets.QLabel(self.gridLayoutWidget_14)
        self.label_indices_man.setObjectName("label_indices_man")
        self.gridLayout_14.addWidget(self.label_indices_man, 2, 0, 1, 1)
        self.label_type_man = QtWidgets.QLabel(self.gridLayoutWidget_14)
        self.label_type_man.setObjectName("label_type_man")
        self.gridLayout_14.addWidget(self.label_type_man, 1, 0, 1, 1)
        self.combobox_search_stock = QtWidgets.QComboBox(self.gridLayoutWidget_14)
        self.combobox_search_stock.setObjectName("combobox_search_stock")
        self.gridLayout_14.addWidget(self.combobox_search_stock, 1, 1, 1, 1)
        self.btn_search_man = QtWidgets.QPushButton(self.gridLayoutWidget_14)
        self.btn_search_man.setObjectName("btn_search_man")
        self.gridLayout_14.addWidget(self.btn_search_man, 1, 2, 1, 1)
        self.combobox_price_man = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_14)
        self.combobox_price_man.setObjectName("combobox_price_man")
        self.gridLayout_14.addWidget(self.combobox_price_man, 6, 1, 1, 1)
        self.rb_short_man = QtWidgets.QRadioButton(self.gridLayoutWidget_14)
        self.rb_short_man.setObjectName("rb_short_man")
        self.gridLayout_14.addWidget(self.rb_short_man, 3, 1, 1, 1)
        self.label_price_man = QtWidgets.QLabel(self.gridLayoutWidget_14)
        self.label_price_man.setObjectName("label_price_man")
        self.gridLayout_14.addWidget(self.label_price_man, 6, 0, 1, 1)
        self.rb_long_man = QtWidgets.QRadioButton(self.gridLayoutWidget_14)
        self.rb_long_man.setObjectName("rb_long_man")
        self.gridLayout_14.addWidget(self.rb_long_man, 3, 2, 1, 1)
        self.label_position_type = QtWidgets.QLabel(self.gridLayoutWidget_14)
        self.label_position_type.setObjectName("label_position_type")
        self.gridLayout_14.addWidget(self.label_position_type, 3, 0, 1, 1)
        self.comboBox_indices = QtWidgets.QComboBox(self.gridLayoutWidget_14)
        self.comboBox_indices.setObjectName("comboBox_indices")
        self.gridLayout_14.addWidget(self.comboBox_indices, 2, 1, 1, 1)
        self.btn_indices_man = QtWidgets.QPushButton(self.gridLayoutWidget_14)
        self.btn_indices_man.setObjectName("btn_indices_man")
        self.gridLayout_14.addWidget(self.btn_indices_man, 2, 2, 1, 1)
        self.label_stoploss_man = QtWidgets.QLabel(self.gridLayoutWidget_14)
        self.label_stoploss_man.setObjectName("label_stoploss_man")
        self.gridLayout_14.addWidget(self.label_stoploss_man, 4, 0, 1, 1)
        self.btn_calc_stop_man = QtWidgets.QPushButton(self.gridLayoutWidget_14)
        self.btn_calc_stop_man.setObjectName("btn_calc_stop_man")
        self.gridLayout_14.addWidget(self.btn_calc_stop_man, 4, 2, 1, 1)
        self.doubleSpinBox_stoploss_man = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_14)
        self.doubleSpinBox_stoploss_man.setObjectName("doubleSpinBox_stoploss_man")
        self.gridLayout_14.addWidget(self.doubleSpinBox_stoploss_man, 4, 1, 1, 1)
        self.btn_submit_man = QtWidgets.QPushButton(self.gridLayoutWidget_14)
        self.btn_submit_man.setObjectName("btn_submit_man")
        self.gridLayout_14.addWidget(self.btn_submit_man, 6, 2, 1, 1)
        self.Widget_bot_right.addTab(self.tab_man_trade, "")
        self.tab_autotrade_action = QtWidgets.QWidget()
        self.tab_autotrade_action.setObjectName("tab_autotrade_action")
        self.textBrowser_autotrade_actions = QtWidgets.QTextBrowser(self.tab_autotrade_action)
        self.textBrowser_autotrade_actions.setGeometry(QtCore.QRect(10, 10, 981, 201))
        self.textBrowser_autotrade_actions.setObjectName("textBrowser_autotrade_actions")
        self.Widget_bot_right.addTab(self.tab_autotrade_action, "")
        self.tab_autotrade_log = QtWidgets.QWidget()
        self.tab_autotrade_log.setObjectName("tab_autotrade_log")
        self.textBrowser_autotrade_log = QtWidgets.QTextBrowser(self.tab_autotrade_log)
        self.textBrowser_autotrade_log.setGeometry(QtCore.QRect(10, 10, 981, 201))
        self.textBrowser_autotrade_log.setObjectName("textBrowser_autotrade_log")
        self.Widget_bot_right.addTab(self.tab_autotrade_log, "")
        self.tab_http_codes = QtWidgets.QWidget()
        self.tab_http_codes.setObjectName("tab_http_codes")
        self.textBrowser_http_codes = QtWidgets.QTextBrowser(self.tab_http_codes)
        self.textBrowser_http_codes.setGeometry(QtCore.QRect(10, 10, 981, 201))
        self.textBrowser_http_codes.setObjectName("textBrowser_http_codes")
        self.Widget_bot_right.addTab(self.tab_http_codes, "")
        self.tab_shortcuts = QtWidgets.QWidget()
        self.tab_shortcuts.setObjectName("tab_shortcuts")
        self.textBrowser_shortcuts = QtWidgets.QTextBrowser(self.tab_shortcuts)
        self.textBrowser_shortcuts.setGeometry(QtCore.QRect(10, 10, 981, 201))
        self.textBrowser_shortcuts.setObjectName("textBrowser_shortcuts")
        self.Widget_bot_right.addTab(self.tab_shortcuts, "")
        LazyTrader.setCentralWidget(self.centralwidget)









        # Menu ---------

        self.menubar = QtWidgets.QMenuBar(LazyTrader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1574, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuIndicators = QtWidgets.QMenu(self.menubar)
        self.menuIndicators.setObjectName("menuIndicators")
        self.menuMoving_Average = QtWidgets.QMenu(self.menuIndicators)
        self.menuMoving_Average.setObjectName("menuMoving_Average")
        self.menuWeekly = QtWidgets.QMenu(self.menuMoving_Average)
        self.menuWeekly.setObjectName("menuWeekly")
        self.menuDaily = QtWidgets.QMenu(self.menuMoving_Average)
        self.menuDaily.setObjectName("menuDaily")
        self.menuMonthly = QtWidgets.QMenu(self.menuMoving_Average)
        self.menuMonthly.setObjectName("menuMonthly")
        self.menuRSI = QtWidgets.QMenu(self.menuIndicators)
        self.menuRSI.setObjectName("menuRSI")
        self.menuDay = QtWidgets.QMenu(self.menuRSI)
        self.menuDay.setObjectName("menuDay")
        self.menuWeek = QtWidgets.QMenu(self.menuRSI)
        self.menuWeek.setObjectName("menuWeek")
        self.menuMonth = QtWidgets.QMenu(self.menuRSI)
        self.menuMonth.setObjectName("menuMonth")
        self.menuOther = QtWidgets.QMenu(self.menubar)
        self.menuOther.setObjectName("menuOther")
        self.menuUpdate_API = QtWidgets.QMenu(self.menuOther)
        self.menuUpdate_API.setObjectName("menuUpdate_API")
        self.menuAutoTrade = QtWidgets.QMenu(self.menubar)
        self.menuAutoTrade.setObjectName("menuAutoTrade")
        LazyTrader.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LazyTrader)
        self.statusbar.setObjectName("statusbar")
        LazyTrader.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(LazyTrader)
        self.actionQuit.setObjectName("actionQuit")
        self.actionBolinger_Bands = QtWidgets.QAction(LazyTrader)
        self.actionBolinger_Bands.setObjectName("actionBolinger_Bands")
        self.actionMACD = QtWidgets.QAction(LazyTrader)
        self.actionMACD.setObjectName("actionMACD")
        self.action10 = QtWidgets.QAction(LazyTrader)
        self.action10.setObjectName("action10")
        self.action15 = QtWidgets.QAction(LazyTrader)
        self.action15.setObjectName("action15")
        self.action20 = QtWidgets.QAction(LazyTrader)
        self.action20.setObjectName("action20")
        self.action30 = QtWidgets.QAction(LazyTrader)
        self.action30.setObjectName("action30")
        self.action40 = QtWidgets.QAction(LazyTrader)
        self.action40.setObjectName("action40")
        self.action50 = QtWidgets.QAction(LazyTrader)
        self.action50.setObjectName("action50")
        self.action60 = QtWidgets.QAction(LazyTrader)
        self.action60.setObjectName("action60")
        self.action70 = QtWidgets.QAction(LazyTrader)
        self.action70.setObjectName("action70")
        self.action80 = QtWidgets.QAction(LazyTrader)
        self.action80.setObjectName("action80")
        self.action90 = QtWidgets.QAction(LazyTrader)
        self.action90.setObjectName("action90")
        self.action100 = QtWidgets.QAction(LazyTrader)
        self.action100.setObjectName("action100")
        self.action120 = QtWidgets.QAction(LazyTrader)
        self.action120.setObjectName("action120")
        self.action150 = QtWidgets.QAction(LazyTrader)
        self.action150.setObjectName("action150")
        self.action200 = QtWidgets.QAction(LazyTrader)
        self.action200.setObjectName("action200")
        self.action10_2 = QtWidgets.QAction(LazyTrader)
        self.action10_2.setObjectName("action10_2")
        self.action20_2 = QtWidgets.QAction(LazyTrader)
        self.action20_2.setObjectName("action20_2")
        self.action30_2 = QtWidgets.QAction(LazyTrader)
        self.action30_2.setObjectName("action30_2")
        self.action40_2 = QtWidgets.QAction(LazyTrader)
        self.action40_2.setObjectName("action40_2")
        self.action50_2 = QtWidgets.QAction(LazyTrader)
        self.action50_2.setObjectName("action50_2")
        self.action60_2 = QtWidgets.QAction(LazyTrader)
        self.action60_2.setObjectName("action60_2")
        self.action70_2 = QtWidgets.QAction(LazyTrader)
        self.action70_2.setObjectName("action70_2")
        self.action80_2 = QtWidgets.QAction(LazyTrader)
        self.action80_2.setObjectName("action80_2")
        self.action90_2 = QtWidgets.QAction(LazyTrader)
        self.action90_2.setObjectName("action90_2")
        self.action100_2 = QtWidgets.QAction(LazyTrader)
        self.action100_2.setObjectName("action100_2")
        self.action120_2 = QtWidgets.QAction(LazyTrader)
        self.action120_2.setObjectName("action120_2")
        self.action150_2 = QtWidgets.QAction(LazyTrader)
        self.action150_2.setObjectName("action150_2")
        self.action200_2 = QtWidgets.QAction(LazyTrader)
        self.action200_2.setObjectName("action200_2")
        self.action10_3 = QtWidgets.QAction(LazyTrader)
        self.action10_3.setObjectName("action10_3")
        self.action20_3 = QtWidgets.QAction(LazyTrader)
        self.action20_3.setObjectName("action20_3")
        self.action30_3 = QtWidgets.QAction(LazyTrader)
        self.action30_3.setObjectName("action30_3")
        self.action40_3 = QtWidgets.QAction(LazyTrader)
        self.action40_3.setObjectName("action40_3")
        self.action50_3 = QtWidgets.QAction(LazyTrader)
        self.action50_3.setObjectName("action50_3")
        self.action60_3 = QtWidgets.QAction(LazyTrader)
        self.action60_3.setObjectName("action60_3")
        self.action70_3 = QtWidgets.QAction(LazyTrader)
        self.action70_3.setObjectName("action70_3")
        self.action80_3 = QtWidgets.QAction(LazyTrader)
        self.action80_3.setObjectName("action80_3")
        self.action90_3 = QtWidgets.QAction(LazyTrader)
        self.action90_3.setObjectName("action90_3")
        self.action100_3 = QtWidgets.QAction(LazyTrader)
        self.action100_3.setObjectName("action100_3")
        self.action12 = QtWidgets.QAction(LazyTrader)
        self.action12.setObjectName("action12")
        self.action150_3 = QtWidgets.QAction(LazyTrader)
        self.action150_3.setObjectName("action150_3")
        self.action200_3 = QtWidgets.QAction(LazyTrader)
        self.action200_3.setObjectName("action200_3")
        self.action10_4 = QtWidgets.QAction(LazyTrader)
        self.action10_4.setObjectName("action10_4")
        self.action11 = QtWidgets.QAction(LazyTrader)
        self.action11.setObjectName("action11")
        self.action12_2 = QtWidgets.QAction(LazyTrader)
        self.action12_2.setObjectName("action12_2")
        self.action13 = QtWidgets.QAction(LazyTrader)
        self.action13.setObjectName("action13")
        self.action15_2 = QtWidgets.QAction(LazyTrader)
        self.action15_2.setObjectName("action15_2")
        self.action15_3 = QtWidgets.QAction(LazyTrader)
        self.action15_3.setObjectName("action15_3")
        self.action16 = QtWidgets.QAction(LazyTrader)
        self.action16.setObjectName("action16")
        self.action17 = QtWidgets.QAction(LazyTrader)
        self.action17.setObjectName("action17")
        self.action18 = QtWidgets.QAction(LazyTrader)
        self.action18.setObjectName("action18")
        self.action19 = QtWidgets.QAction(LazyTrader)
        self.action19.setObjectName("action19")
        self.action20_4 = QtWidgets.QAction(LazyTrader)
        self.action20_4.setObjectName("action20_4")
        self.action10_5 = QtWidgets.QAction(LazyTrader)
        self.action10_5.setObjectName("action10_5")
        self.action11_2 = QtWidgets.QAction(LazyTrader)
        self.action11_2.setObjectName("action11_2")
        self.action12_3 = QtWidgets.QAction(LazyTrader)
        self.action12_3.setObjectName("action12_3")
        self.action13_2 = QtWidgets.QAction(LazyTrader)
        self.action13_2.setObjectName("action13_2")
        self.action14 = QtWidgets.QAction(LazyTrader)
        self.action14.setObjectName("action14")
        self.action15_4 = QtWidgets.QAction(LazyTrader)
        self.action15_4.setObjectName("action15_4")
        self.action16_2 = QtWidgets.QAction(LazyTrader)
        self.action16_2.setObjectName("action16_2")
        self.action17_2 = QtWidgets.QAction(LazyTrader)
        self.action17_2.setObjectName("action17_2")
        self.action18_2 = QtWidgets.QAction(LazyTrader)
        self.action18_2.setObjectName("action18_2")
        self.action19_2 = QtWidgets.QAction(LazyTrader)
        self.action19_2.setObjectName("action19_2")
        self.action20_5 = QtWidgets.QAction(LazyTrader)
        self.action20_5.setObjectName("action20_5")
        self.action1 = QtWidgets.QAction(LazyTrader)
        self.action1.setObjectName("action1")
        self.action11_3 = QtWidgets.QAction(LazyTrader)
        self.action11_3.setObjectName("action11_3")
        self.action12_4 = QtWidgets.QAction(LazyTrader)
        self.action12_4.setObjectName("action12_4")
        self.action13_3 = QtWidgets.QAction(LazyTrader)
        self.action13_3.setObjectName("action13_3")
        self.action14_2 = QtWidgets.QAction(LazyTrader)
        self.action14_2.setObjectName("action14_2")
        self.action15_5 = QtWidgets.QAction(LazyTrader)
        self.action15_5.setObjectName("action15_5")
        self.action16_3 = QtWidgets.QAction(LazyTrader)
        self.action16_3.setObjectName("action16_3")
        self.action17_3 = QtWidgets.QAction(LazyTrader)
        self.action17_3.setObjectName("action17_3")
        self.action18_3 = QtWidgets.QAction(LazyTrader)
        self.action18_3.setObjectName("action18_3")
        self.action19_3 = QtWidgets.QAction(LazyTrader)
        self.action19_3.setObjectName("action19_3")
        self.action20_6 = QtWidgets.QAction(LazyTrader)
        self.action20_6.setObjectName("action20_6")
        self.actionQuandl = QtWidgets.QAction(LazyTrader)
        self.actionQuandl.setObjectName("actionQuandl")
        self.actionIEX = QtWidgets.QAction(LazyTrader)
        self.actionIEX.setObjectName("actionIEX")
        self.actionSave_Trade_History = QtWidgets.QAction(LazyTrader)
        self.actionSave_Trade_History.setObjectName("actionSave_Trade_History")
        self.actionAdd_Trade = QtWidgets.QAction(LazyTrader)
        self.actionAdd_Trade.setObjectName("actionAdd_Trade")
        self.actionOn = QtWidgets.QAction(LazyTrader)
        self.actionOn.setObjectName("actionOn")
        self.actionOFF = QtWidgets.QAction(LazyTrader)
        self.actionOFF.setObjectName("actionOFF")
        self.menuFile.addAction(self.actionSave_Trade_History)
        self.menuFile.addAction(self.actionQuit)
        self.menuWeekly.addAction(self.action10_3)
        self.menuWeekly.addAction(self.action20_3)
        self.menuWeekly.addAction(self.action30_3)
        self.menuWeekly.addAction(self.action40_3)
        self.menuWeekly.addAction(self.action50_3)
        self.menuWeekly.addAction(self.action60_3)
        self.menuWeekly.addAction(self.action70_3)
        self.menuWeekly.addAction(self.action80_3)
        self.menuWeekly.addAction(self.action90_3)
        self.menuWeekly.addAction(self.action100_3)
        self.menuWeekly.addAction(self.action12)
        self.menuWeekly.addAction(self.action150_3)
        self.menuWeekly.addAction(self.action200_3)
        self.menuDaily.addAction(self.action10)
        self.menuDaily.addAction(self.action15)
        self.menuDaily.addAction(self.action20)
        self.menuDaily.addAction(self.action30)
        self.menuDaily.addAction(self.action40)
        self.menuDaily.addAction(self.action50)
        self.menuDaily.addAction(self.action60)
        self.menuDaily.addAction(self.action70)
        self.menuDaily.addAction(self.action80)
        self.menuDaily.addAction(self.action90)
        self.menuDaily.addAction(self.action100)
        self.menuDaily.addAction(self.action120)
        self.menuDaily.addAction(self.action150)
        self.menuDaily.addAction(self.action200)
        self.menuMonthly.addAction(self.action10_2)
        self.menuMonthly.addAction(self.action20_2)
        self.menuMonthly.addAction(self.action30_2)
        self.menuMonthly.addAction(self.action40_2)
        self.menuMonthly.addAction(self.action50_2)
        self.menuMonthly.addAction(self.action60_2)
        self.menuMonthly.addAction(self.action70_2)
        self.menuMonthly.addAction(self.action80_2)
        self.menuMonthly.addAction(self.action90_2)
        self.menuMonthly.addAction(self.action100_2)
        self.menuMonthly.addAction(self.action120_2)
        self.menuMonthly.addAction(self.action150_2)
        self.menuMonthly.addAction(self.action200_2)
        self.menuMoving_Average.addAction(self.menuWeekly.menuAction())
        self.menuMoving_Average.addAction(self.menuMonthly.menuAction())
        self.menuMoving_Average.addAction(self.menuDaily.menuAction())
        self.menuDay.addAction(self.action10_4)
        self.menuDay.addAction(self.action11)
        self.menuDay.addAction(self.action12_2)
        self.menuDay.addAction(self.action13)
        self.menuDay.addAction(self.action15_2)
        self.menuDay.addAction(self.action15_3)
        self.menuDay.addAction(self.action16)
        self.menuDay.addAction(self.action17)
        self.menuDay.addAction(self.action18)
        self.menuDay.addAction(self.action19)
        self.menuDay.addAction(self.action20_4)
        self.menuWeek.addAction(self.action10_5)
        self.menuWeek.addAction(self.action11_2)
        self.menuWeek.addAction(self.action12_3)
        self.menuWeek.addAction(self.action13_2)
        self.menuWeek.addAction(self.action14)
        self.menuWeek.addAction(self.action15_4)
        self.menuWeek.addAction(self.action16_2)
        self.menuWeek.addAction(self.action17_2)
        self.menuWeek.addAction(self.action18_2)
        self.menuWeek.addAction(self.action19_2)
        self.menuWeek.addAction(self.action20_5)
        self.menuMonth.addAction(self.action1)
        self.menuMonth.addAction(self.action11_3)
        self.menuMonth.addAction(self.action12_4)
        self.menuMonth.addAction(self.action13_3)
        self.menuMonth.addAction(self.action14_2)
        self.menuMonth.addAction(self.action15_5)
        self.menuMonth.addAction(self.action16_3)
        self.menuMonth.addAction(self.action17_3)
        self.menuMonth.addAction(self.action18_3)
        self.menuMonth.addAction(self.action19_3)
        self.menuMonth.addAction(self.action20_6)
        self.menuRSI.addAction(self.menuDay.menuAction())
        self.menuRSI.addAction(self.menuWeek.menuAction())
        self.menuRSI.addAction(self.menuMonth.menuAction())
        self.menuIndicators.addAction(self.menuRSI.menuAction())
        self.menuIndicators.addAction(self.actionBolinger_Bands)
        self.menuIndicators.addAction(self.actionMACD)
        self.menuIndicators.addAction(self.menuMoving_Average.menuAction())
        self.menuUpdate_API.addAction(self.actionQuandl)
        self.menuUpdate_API.addAction(self.actionIEX)
        self.menuOther.addAction(self.menuUpdate_API.menuAction())
        self.menuOther.addAction(self.actionAdd_Trade)
        self.menuAutoTrade.addAction(self.actionOn)
        self.menuAutoTrade.addAction(self.actionOFF)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuIndicators.menuAction())
        self.menubar.addAction(self.menuOther.menuAction())
        self.menubar.addAction(self.menuAutoTrade.menuAction())

        # select the default tabs on the GUI 
        self.retranslateUi(LazyTrader)
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.Widget_bot_right.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(LazyTrader)

        #################################################
        #
        # DYNAMIC GRAPH EXAMPLE
        #################################################
        # layout = QtWidgets.QVBoxLayout(self.frame_8)
        # #static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        
        # fig = plt.figure()
        # fig.patch.set_facecolor((0.20, 0.20, 0.20))


        # static_canvas = FigureCanvas(fig)
        # layout.addWidget(static_canvas)
        # self.addToolBar(NavigationToolbar(static_canvas, self))

        # self._dynamic_ax = static_canvas.figure.subplots()
        # self._timer = static_canvas.new_timer(100, [(self._update_canvas, (), {})])
        # self._timer.start()

        #################################################
        #
        # STATIC GRAPH EXAMPLE
        #################################################
        # layout = QtWidgets.QVBoxLayout(self.frame_8)
        # fig = plt.figure(figsize=(200, 120))
        # fig.patch.set_facecolor((0.20, 0.20, 0.20))
        # static_canvas = FigureCanvas(fig)
        # layout.addWidget(static_canvas)
        # self.addToolBar(NavigationToolbar(static_canvas, self))
        # self.addToolBar(QtCore.Qt.BottomToolBarArea,NavigationToolbar(static_canvas, self))
        # data = quandl.get("BITSTAMP/USD")
        # plt.style.use('dark_background')
        # plt.plot(data['Low'])
        # plt.title('Bitcoin Low price')

    def _update_canvas(self):
        self._dynamic_ax.clear()
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._dynamic_ax.plot(t, np.sin(t + time.time()))
        self._dynamic_ax.figure.canvas.draw()



    def retranslateUi(self, LazyTrader):
        _translate = QtCore.QCoreApplication.translate
        LazyTrader.setWindowTitle(_translate("LazyTrader", "LazyTrader"))
        self.btn_update_stop_action.setText(_translate("LazyTrader", "UPDATE STOP LOSS"))
        self.btn_pyramid_action.setText(_translate("LazyTrader", "PYRAMID"))
        self.label_unit_action.setText(_translate("LazyTrader", "Units"))
        self.label_stop_action.setText(_translate("LazyTrader", "Stop Price"))
        self.btn_update_open_action.setText(_translate("LazyTrader", "UPDATE OPEN PRICE"))
        self.label_open_action.setText(_translate("LazyTrader", "Opening price"))
        self.label_close_action.setText(_translate("LazyTrader", "Close Price"))
        self.btn_close_action.setText(_translate("LazyTrader", "CLOSE POSITION"))
        self.btn_order_open_action.setText(_translate("LazyTrader", "ORDER OPEN"))
        self.btn_hit_action.setText(_translate("LazyTrader", "ORDER NOT HIT YET"))
        self.btn_auto_action.setText(_translate("LazyTrader", "AUTO"))
        self.btn_select_trade_action.setText(_translate("LazyTrader", "Select Trade"))
        self.label_first_action.setText(_translate("LazyTrader", "UPDATE STOP LOSS TO : $1384"))
        self.label_second_action.setText(_translate("LazyTrader", "Add One Unit to Possition Of Size: $25"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_trade_actions), _translate("LazyTrader", "Trade Actions "))
        self.label_open_action_info.setText(_translate("LazyTrader", "Position Open for: 6 days"))
        self.label_stoploss_action_info.setText(_translate("LazyTrader", "Current StopLoss: $15657"))
        self.label_profit_action_info.setText(_translate("LazyTrader", "Profit / Loss: 4%"))
        self.label_type_action_info.setText(_translate("LazyTrader", "Asset Type: Commodity"))
        self.label_volatility_action_info.setText(_translate("LazyTrader", "N Volatility: 0.25"))
        self.label_system_action_info.setText(_translate("LazyTrader", "System: S1"))
        self.label_entry_point_action_info.setText(_translate("LazyTrader", "Entry Point"))
        self.label_stoploss_dis_action_info.setText(_translate("LazyTrader", "Distance From Stop Loss: 2%"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_trade_info), _translate("LazyTrader", "Trade Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_action), _translate("LazyTrader", "Action (A)"))
        self.label_stop_sug.setText(_translate("LazyTrader", "Stop Loss"))
        self.btn_opn_sug.setText(_translate("LazyTrader", "Open Position"))
        self.label_entry_sug.setText(_translate("LazyTrader", "Entry Price"))
        self.label_id_sug.setText(_translate("LazyTrader", "ID"))
        self.btn_view_chart_sug.setText(_translate("LazyTrader", "View Chart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sugested_pos), _translate("LazyTrader", "Sugested Positions (S)"))
        self.btn_close_pos_open.setText(_translate("LazyTrader", "Close Position"))
        self.btn_search_open.setText(_translate("LazyTrader", "Search Name"))
        self.btn_search_type_open.setText(_translate("LazyTrader", "Search Type"))
        self.btn_view_chart_open.setText(_translate("LazyTrader", "View_chart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_open_pos), _translate("LazyTrader", "Open (O)"))
        self.btn_search_closed.setText(_translate("LazyTrader", "Search"))
        self.btn_export_closed.setText(_translate("LazyTrader", "Export To CSV"))
        self.btn_sort_closed.setText(_translate("LazyTrader", "Sort By ROI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_closed_pos), _translate("LazyTrader", "Closed (C)"))
        self.btn_search_name_all.setText(_translate("LazyTrader", "Search Name"))
        self.btn_search_type_all.setText(_translate("LazyTrader", "Search Type"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_all_pos), _translate("LazyTrader", "All"))
        self.label_stock_name_graph.setText(_translate("LazyTrader", "<stock name>"))
        self.label_signal_graph.setText(_translate("LazyTrader", "Signal"))
        self.btn_vol_graph.setText(_translate("LazyTrader", "Volume"))
        self.btn_rsi_graph.setText(_translate("LazyTrader", "RSI"))
        self.btn_ma_graph.setText(_translate("LazyTrader", "MA"))
        self.btn_bol_bands_graph.setText(_translate("LazyTrader", "Boliger Bands"))
        self.btn_macd_graph.setText(_translate("LazyTrader", "MACD"))
        self.btn_open_pos_graph.setText(_translate("LazyTrader", "Open Position"))
        self.btn_close_position_graph.setText(_translate("LazyTrader", "Close Position"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_price_graph), _translate("LazyTrader", "Stock Price Viewer (V)"))
        self.label_unit_size_port.setText(_translate("LazyTrader", "Unit Size: $25"))
        self.label_open_port.setText(_translate("LazyTrader", "Positions Open: 10"))
        self.label_los_pos_port.setText(_translate("LazyTrader", "Losing Positions:"))
        self.label_win_pos_port.setText(_translate("LazyTrader", "Winning Positions:"))
        self.label_avg_loss_port.setText(_translate("LazyTrader", "Average Lose:"))
        self.label_avg_win_port.setText(_translate("LazyTrader", "Average Win: "))
        self.label_edge_port.setText(_translate("LazyTrader", "Current Edge:"))
        self.label_equity_port.setText(_translate("LazyTrader", "Current Equity:"))
        self.label_daily_profit_port.setText(_translate("LazyTrader", "Daily Profit Loss: "))
        self.label_units_used_port.setText(_translate("LazyTrader", "Units Used"))
        self.label_tot_profit_port.setText(_translate("LazyTrader", "Total Profit Loss: "))
        self.label_month_profit_port.setText(_translate("LazyTrader", "Monthly Profit Loss:"))
        self.btn_acc_growth_port.setText(_translate("LazyTrader", "Account Growth"))
        self.btn_acc_volatility_port.setText(_translate("LazyTrader", "Account Volatility"))
        self.btn_win_lose_port.setText(_translate("LazyTrader", "Win/Lose"))
        self.btn_pos_open_port.setText(_translate("LazyTrader", "Position Open"))
        self.btn_s1_s2_port.setText(_translate("LazyTrader", "S1 VS S2"))
        self.btn_correlation_port.setText(_translate("LazyTrader", "Correlation"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_portfolio_graph), _translate("LazyTrader", "Portfolio Tracker (P)"))
        self.btn_buy_notes.setText(_translate("LazyTrader", "Buy"))
        self.btn_sell_notes.setText(_translate("LazyTrader", "Sell"))
        self.btn_prediction_notes.setText(_translate("LazyTrader", "Prediction"))
        self.btn_submit_notes.setText(_translate("LazyTrader", "Submit"))
        self.btn_search_notes.setText(_translate("LazyTrader", "Search"))
        self.btn_save_notes.setText(_translate("LazyTrader", "Save Notes To FIle"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_notes), _translate("LazyTrader", "Notes (N)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_backtest), _translate("LazyTrader", "Systematic Algorithmic Backtesting Performace"))
        self.label_action_required.setText(_translate("LazyTrader", "Actions Required"))
        self.label_last_updated.setText(_translate("LazyTrader", "Current Date: Sunday 10th January"))
        self.label_update_time.setText(_translate("LazyTrader", "Last Updated: 2 Days, 3 Hours and 30 Mins ago"))
        self.btn_update_df.setText(_translate("LazyTrader", "UPDATE SYSTEM (U)"))
        self.btn_copy_logs.setText(_translate("LazyTrader", "Copy Logs"))
        self.btn_print_acc_sum.setText(_translate("LazyTrader", "Print Account Summary"))
        self.btn_save_logs.setText(_translate("LazyTrader", "Save Logs"))
        self.Widget_bot_right.setTabText(self.Widget_bot_right.indexOf(self.tab_console), _translate("LazyTrader", "Console (C)"))
        self.label_indices_man.setText(_translate("LazyTrader", "Indices"))
        self.label_type_man.setText(_translate("LazyTrader", "Comodity/Stock/Crypto"))
        self.btn_search_man.setText(_translate("LazyTrader", "Search"))
        self.rb_short_man.setText(_translate("LazyTrader", "Short"))
        self.label_price_man.setText(_translate("LazyTrader", "Price"))
        self.rb_long_man.setText(_translate("LazyTrader", "Long"))
        self.label_position_type.setText(_translate("LazyTrader", "Position Type"))
        self.btn_indices_man.setText(_translate("LazyTrader", "Select"))
        self.label_stoploss_man.setText(_translate("LazyTrader", "Calculate Stoploss"))
        self.btn_calc_stop_man.setText(_translate("LazyTrader", "Calculate"))
        self.btn_submit_man.setText(_translate("LazyTrader", "Submit"))
        self.Widget_bot_right.setTabText(self.Widget_bot_right.indexOf(self.tab_man_trade), _translate("LazyTrader", "Manual Add Trade (M)"))
        self.Widget_bot_right.setTabText(self.Widget_bot_right.indexOf(self.tab_autotrade_action), _translate("LazyTrader", "AutoTrade Actions (L)"))
        self.Widget_bot_right.setTabText(self.Widget_bot_right.indexOf(self.tab_autotrade_log), _translate("LazyTrader", "Auto Trade Logs (L)"))
        self.Widget_bot_right.setTabText(self.Widget_bot_right.indexOf(self.tab_http_codes), _translate("LazyTrader", "HTTP Requests Status Codes"))
        self.Widget_bot_right.setTabText(self.Widget_bot_right.indexOf(self.tab_shortcuts), _translate("LazyTrader", "Display Shortcuts"))
        self.menuFile.setTitle(_translate("LazyTrader", "File"))
        self.menuIndicators.setTitle(_translate("LazyTrader", "Indicators"))
        self.menuMoving_Average.setTitle(_translate("LazyTrader", "Moving Average"))
        self.menuWeekly.setTitle(_translate("LazyTrader", "Weekly"))
        self.menuDaily.setTitle(_translate("LazyTrader", "Daily"))
        self.menuMonthly.setTitle(_translate("LazyTrader", "Monthly"))
        self.menuRSI.setTitle(_translate("LazyTrader", "RSI"))
        self.menuDay.setTitle(_translate("LazyTrader", "day"))
        self.menuWeek.setTitle(_translate("LazyTrader", "week"))
        self.menuMonth.setTitle(_translate("LazyTrader", "month"))
        self.menuOther.setTitle(_translate("LazyTrader", "Other"))
        self.menuUpdate_API.setTitle(_translate("LazyTrader", "Update API"))
        self.menuAutoTrade.setTitle(_translate("LazyTrader", "AutoTrade"))
        self.actionQuit.setText(_translate("LazyTrader", "Quit"))
        self.actionBolinger_Bands.setText(_translate("LazyTrader", "Bolinger Bands"))
        self.actionMACD.setText(_translate("LazyTrader", "MACD"))
        self.action10.setText(_translate("LazyTrader", "10"))
        self.action15.setText(_translate("LazyTrader", "15"))
        self.action20.setText(_translate("LazyTrader", "20"))
        self.action30.setText(_translate("LazyTrader", "30"))
        self.action40.setText(_translate("LazyTrader", "40"))
        self.action50.setText(_translate("LazyTrader", "50"))
        self.action60.setText(_translate("LazyTrader", "60"))
        self.action70.setText(_translate("LazyTrader", "70"))
        self.action80.setText(_translate("LazyTrader", "80"))
        self.action90.setText(_translate("LazyTrader", "90"))
        self.action100.setText(_translate("LazyTrader", "100"))
        self.action120.setText(_translate("LazyTrader", "120"))
        self.action150.setText(_translate("LazyTrader", "150"))
        self.action200.setText(_translate("LazyTrader", "200"))
        self.action10_2.setText(_translate("LazyTrader", "10"))
        self.action20_2.setText(_translate("LazyTrader", "20"))
        self.action30_2.setText(_translate("LazyTrader", "30"))
        self.action40_2.setText(_translate("LazyTrader", "40"))
        self.action50_2.setText(_translate("LazyTrader", "50"))
        self.action60_2.setText(_translate("LazyTrader", "60"))
        self.action70_2.setText(_translate("LazyTrader", "70"))
        self.action80_2.setText(_translate("LazyTrader", "80"))
        self.action90_2.setText(_translate("LazyTrader", "90"))
        self.action100_2.setText(_translate("LazyTrader", "100"))
        self.action120_2.setText(_translate("LazyTrader", "120"))
        self.action150_2.setText(_translate("LazyTrader", "150"))
        self.action200_2.setText(_translate("LazyTrader", "200"))
        self.action10_3.setText(_translate("LazyTrader", "10"))
        self.action20_3.setText(_translate("LazyTrader", "20"))
        self.action30_3.setText(_translate("LazyTrader", "30"))
        self.action40_3.setText(_translate("LazyTrader", "40"))
        self.action50_3.setText(_translate("LazyTrader", "50"))
        self.action60_3.setText(_translate("LazyTrader", "60"))
        self.action70_3.setText(_translate("LazyTrader", "70"))
        self.action80_3.setText(_translate("LazyTrader", "80"))
        self.action90_3.setText(_translate("LazyTrader", "90"))
        self.action100_3.setText(_translate("LazyTrader", "100"))
        self.action12.setText(_translate("LazyTrader", "120"))
        self.action150_3.setText(_translate("LazyTrader", "150"))
        self.action200_3.setText(_translate("LazyTrader", "200"))
        self.action10_4.setText(_translate("LazyTrader", "10"))
        self.action11.setText(_translate("LazyTrader", "11"))
        self.action12_2.setText(_translate("LazyTrader", "12"))
        self.action13.setText(_translate("LazyTrader", "13"))
        self.action15_2.setText(_translate("LazyTrader", "14"))
        self.action15_3.setText(_translate("LazyTrader", "15"))
        self.action16.setText(_translate("LazyTrader", "16"))
        self.action17.setText(_translate("LazyTrader", "17"))
        self.action18.setText(_translate("LazyTrader", "18"))
        self.action19.setText(_translate("LazyTrader", "19"))
        self.action20_4.setText(_translate("LazyTrader", "20"))
        self.action10_5.setText(_translate("LazyTrader", "10"))
        self.action11_2.setText(_translate("LazyTrader", "11"))
        self.action12_3.setText(_translate("LazyTrader", "12"))
        self.action13_2.setText(_translate("LazyTrader", "13"))
        self.action14.setText(_translate("LazyTrader", "14"))
        self.action15_4.setText(_translate("LazyTrader", "15"))
        self.action16_2.setText(_translate("LazyTrader", "16"))
        self.action17_2.setText(_translate("LazyTrader", "17"))
        self.action18_2.setText(_translate("LazyTrader", "18"))
        self.action19_2.setText(_translate("LazyTrader", "19"))
        self.action20_5.setText(_translate("LazyTrader", "20"))
        self.action1.setText(_translate("LazyTrader", "10"))
        self.action11_3.setText(_translate("LazyTrader", "11"))
        self.action12_4.setText(_translate("LazyTrader", "12"))
        self.action13_3.setText(_translate("LazyTrader", "13"))
        self.action14_2.setText(_translate("LazyTrader", "14"))
        self.action15_5.setText(_translate("LazyTrader", "15"))
        self.action16_3.setText(_translate("LazyTrader", "16"))
        self.action17_3.setText(_translate("LazyTrader", "17"))
        self.action18_3.setText(_translate("LazyTrader", "18"))
        self.action19_3.setText(_translate("LazyTrader", "19"))
        self.action20_6.setText(_translate("LazyTrader", "20"))
        self.actionQuandl.setText(_translate("LazyTrader", "Quandl"))
        self.actionIEX.setText(_translate("LazyTrader", "IEX"))
        self.actionSave_Trade_History.setText(_translate("LazyTrader", "Save Trade History"))
        self.actionAdd_Trade.setText(_translate("LazyTrader", "Add Trade"))
        self.actionOn.setText(_translate("LazyTrader", "ON"))
        self.actionOFF.setText(_translate("LazyTrader", "OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    LazyTrader = QtWidgets.QMainWindow()
    ui = Ui_LazyTrader()
    ui.setupUi(LazyTrader)
    LazyTrader.show()
    sys.exit(app.exec_())
