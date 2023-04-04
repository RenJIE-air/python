import os, sys
from datetime import datetime
import re

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *
from ui.monkey_export import Ui_MainWindow
from threading import Thread
from PySide2.QtCore import Signal, QObject
import webbrowser

index = 0
cmd_ADB = "adb "
cmd_monkeylog = " pull /data/local/tmp/monkeylog.txt "
cmd_monkeylog_error = " pull /data/local/tmp/monkeylog_error.txt "
cmd_log = " pull "
cmd_bugreport = " bugreport "
SN_list = []
SN_fail_list = []
result = []
devices = []
ui = Ui_MainWindow()
wholeMonkey = True
singleMonkey = False
logPath = "/data/ylog"
outPath = os.getcwd()
exportLog = True
exportBugreport = True
origin_crash = []
origin_anr = []
origin_calendar = []
monkey_calendar = ""
result_crash = {}
result_anr = {}
now_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


class MySignals(QObject):
    text_print = Signal(str)


global_ms = MySignals()


def initWindow():
    setConnectDevices()
    ui.pushButton_3.clicked.connect(setConnectDevices)
    ui.pushButton_3.setStyleSheet("QPushButton{background-color:'lightgreen';}")
    ui.clearButton.clicked.connect(clearMessage)
    ui.LogPathInput.setPlaceholderText("默认路径为：" + logPath)
    ui.OutputPathInput.setPlaceholderText("默认路径为：" + outPath)
    ui.label_2.setVisible(False)
    ui.exportButton.clicked.connect(exportAll)
    ui.stopMonkeyButton.clicked.connect(stopMonkey)
    ui.action.triggered.connect(getHelp)
    ui.action_history.triggered.connect(getHistory)
    ui.action_feedback.triggered.connect(feedback)

def getHelp():
    webbrowser.open("https://gitee.com/renjie-air/monkey-export")

def getHistory():
    webbrowser.open("https://gitee.com/renjie-air/monkey-export/releases")

def feedback():
    webbrowser.open("https://gitee.com/renjie-air/monkey-export/issues")

def getMonkeyLog(SN_list):
    state = 1
    if len(SN_list) == 1:
        if not os.path.exists(outPath + SN_list[0]):
            os.mkdir(outPath + SN_list[0])
        global_ms.text_print.emit(cmd_ADB + cmd_monkeylog + outPath + SN_list[0] + " 正在导出，请稍后...")
        state = os.system(cmd_ADB + cmd_monkeylog + outPath + SN_list[0] + "\\monkeylog.txt")
        if state == 0:
            global_ms.text_print.emit("monkeylog导出成功,文件已保存至[" + outPath + SN_list[0] + "\\monkeylog.txt]")
        else:
            global_ms.text_print.emit("monkeylog导出失败，程序结束，请确认设备是否正常进行了monkey测试。")
    else:
        for SN in SN_list:
            if not os.path.exists(outPath + SN):
                os.mkdir(outPath + SN)
            global_ms.text_print.emit(cmd_ADB + "-s " + SN + cmd_monkeylog + outPath + SN + " 正在导出，请稍后...")
            state = os.system(cmd_ADB + "-s " + SN + cmd_monkeylog + outPath + SN + "\\monkeylog.txt")
            if state == 0:
                global_ms.text_print.emit("monkeylog导出成功,文件已保存至[" + outPath + SN + "\\monkeylog.txt]")
            else:
                SN_fail_list.append(SN)
                global_ms.text_print.emit("monkeylog导出失败，已停止导出设备[" + SN + "]的相关文件，请确认设备是否正常进行了monkey测试。")
    return state


def getMonkeyLogError(SN_list):
    state = 1
    if len(SN_list) == 1:
        global_ms.text_print.emit(cmd_ADB + cmd_monkeylog_error + outPath + SN_list[0] + " 正在导出，请稍后...")
        state = os.system(cmd_ADB + cmd_monkeylog_error + outPath + SN_list[0] + "\\monkeylog_error.txt")
        if state == 0:
            global_ms.text_print.emit("monkeylog_error导出成功,文件已保存至[" + outPath + SN_list[0] + "\\monkeylog_error.txt]")
        else:
            global_ms.text_print.emit("monkeylog_error导出失败，程序结束，请确认设备是否正常进行了monkey测试。")
    else:
        for SN in SN_list:
            global_ms.text_print.emit(cmd_ADB + "-s " + SN + cmd_monkeylog_error + outPath + SN + " 正在导出，请稍后...")
            state = os.system(cmd_ADB + "-s " + SN + cmd_monkeylog_error + outPath + SN + "\\monkeylog_error.txt")
            if state == 0:
                global_ms.text_print.emit("monkeylog_error导出成功,文件已保存至[" + outPath + SN + "\\monkeylog_error.txt]")
            else:
                SN_fail_list.append(SN)
                global_ms.text_print.emit("monkeylog_error导出失败，已停止导出设备[" + SN + "]的相关文件，请确认设备是否正常进行了monkey测试。")
    return state


def monkeylog_analyse(monkeylog_error_path, SN_list):
    global f_log, result_file, f_error, monkey_calendar
    for SN in SN_list:
        origin_crash.clear()
        origin_anr.clear()
        origin_calendar.clear()
        result_crash.clear()
        result_anr.clear()
        monkey_calendar = ""
        global_ms.text_print.emit("开始分析设备：[" + SN + "]monkey结果")
        try:
            tOutPath = monkeylog_error_path + SN + "\\"
            f_log = open(tOutPath + "monkeylog.txt", encoding='utf-8')
            file_log = []
            for line in f_log:
                file_log.append(line.strip())
            f_log.close()
            if wholeMonkey:
                f_error = open(tOutPath + "monkeylog_error.txt", encoding='utf-8')
                file_error = []
                for line in f_error:
                    file_error.append(line.strip())
                f_error.close()
            else:
                file_error = file_log
            with open(tOutPath + "result.txt", "w") as temp:
                temp.write("")
            result_file = open(tOutPath + "result.txt", "a")
            for x in file_log:
                if x != "" and len(x) >= 17:
                    if x[0:17] == "//[calendar_time:":
                        origin_calendar.append(x[17:36])
                if len(origin_calendar) > 1:
                    monkey_calendar = "monkey开始时间：" + origin_calendar[0] + " monkey结束时间：" + origin_calendar[
                        len(origin_calendar) - 1] + " 总运行时长：" + str(round(((datetime.strptime(str(origin_calendar[len(origin_calendar) - 1]), "%Y-%m-%d %H:%M:%S") - datetime.strptime(str(origin_calendar[0]), "%Y-%m-%d %H:%M:%S")).total_seconds()) / 3600, 2)) + "H"
                if monkey_calendar == "":
                    monkey_calendar = "获取monkey时间错误！"
            global_ms.text_print.emit("设备：[" + SN + "]" + monkey_calendar)
            result_file.write("结果分析时间：" + now_time + "\n\n")
            result_file.write(monkey_calendar + "\n\n")

            for x in file_error:
                if x != "":
                    if x[0:9] == "// CRASH:":
                        origin_crash.append(re.split(r"[;, ]", x)[2])
                    if x[0:6] == "ANR in" and len(x) > 6:
                        if re.split(r"[;, ]", x)[2][-1] == "\n":
                            origin_anr.append(re.split(r"[;, ]", x)[2][0:-1])
                        else:
                            origin_anr.append(re.split(r"[;, ]", x)[2])
            for i in origin_crash:
                result_crash[i] = origin_crash.count(i)
            result_file.write("----CRASH结果如下----\n")
            for key, value in result_crash.items():
                result_file.write(key + " " + str(value) + "\n")
            global_ms.text_print.emit("设备：[" + SN + "]CRASH结果统计完成")

            for i in origin_anr:
                result_anr[i] = origin_anr.count(i)
            result_file.write("\n----ANR结果如下----\n")
            for key, value in result_anr.items():
                result_file.write(key + " " + str(value) + "\n")
            result_file.close()
            global_ms.text_print.emit("设备：[" + SN + "]ANR结果统计完成")
            global_ms.text_print.emit("设备：[" + SN + "]结果分析完成，结果已保存至[" + monkeylog_error_path + SN +"\\result.txt]")
        except FileNotFoundError:
            global_ms.text_print.emit("没有找到monkeylog文件！")
    global_ms.text_print.emit("所有设备monkey结果分析结束")


def getLog(outPath, SN_list):
    if not SN_list:
        global_ms.text_print.emit("log-未连接设备，请连接后重试")
    for SN in SN_list:
        if len(SN_list) > 1:
            state = os.system(cmd_ADB + " -s " + SN + cmd_log + logPath + " " + outPath + SN)
            if state == 0:
                global_ms.text_print.emit("设备：[" + SN + "]log导出成功")
            else:
                global_ms.text_print.emit("设备：[" + SN + "]log导出失败")
        elif len(SN_list) == 1:
            state = os.system(cmd_ADB + cmd_log + logPath + " " + outPath + SN)
            if state == 0:
                global_ms.text_print.emit("设备：[" + SN + "]log导出成功")
            else:
                global_ms.text_print.emit("设备：[" + SN + "]log导出失败")
    global_ms.text_print.emit("所有设备导出log完毕")


def getBugreport(outPath, SN_list):
    if not SN_list:
        global_ms.text_print.emit("bugreport-未连接设备，请连接后重试")
    for SN in SN_list:
        if len(SN_list) > 1:
            state = os.system(cmd_ADB + " -s " + SN + cmd_bugreport + " " + outPath + SN)
            if state == 0:
                global_ms.text_print.emit("设备：[" + SN + "]bugreport导出成功")
            else:
                global_ms.text_print.emit("设备：[" + SN + "]bugreport导出失败")
        elif len(SN_list) == 1:
            state = os.system(cmd_ADB + cmd_bugreport + " " + outPath + SN)
            if state == 0:
                global_ms.text_print.emit("设备：[" + SN + "]bugreport导出成功")
            else:
                global_ms.text_print.emit("设备：[" + SN + "]bugreport导出失败")
    global_ms.text_print.emit("所有设备bugreport导出完毕")


def exportAll():
    global index
    index = 0
    global outPath
    getInfo()
    ui.exportButton.setEnabled(False)
    ui.exportButton.setText("正在导出，请稍后...")
    ui.exportButton.setStyleSheet("QPushButton{background-color:'orange';}")
    successMonkey = getMonkeyLog(SN_list)
    if successMonkey == 1:
        ui.exportButton.setEnabled(True)
        ui.exportButton.setText("开始导出")
        ui.exportButton.setStyleSheet("QPushButton{background-color:'#3498db';}")
    if wholeMonkey and successMonkey == 0:
        getMonkeyLogError(SN_list)

    # 分析
    if successMonkey == 0:
        Thread(target=monkeylog_analyse, args=(outPath, SN_list)).start()
    # 结束分析

    if exportLog and successMonkey == 0:
        Thread(target=getLog, args=(outPath, SN_list)).start()
    if exportBugreport and successMonkey == 0:
        Thread(target=getBugreport, args=(outPath, SN_list)).start()

def stopMonkey():
    global SN_list
    if len(SN_list) > 1:
        for SN in SN_list:
            pidResult = []
            pop = os.popen("adb -s " + SN + " shell ps -le |findstr monkey")
            global_ms.text_print.emit("adb -s " + SN + " shell ps -le |findstr monkey")
            read_result = pop.read().split("\n")
            if len(read_result) > 1:
                for result_item in read_result[0].split(" "):
                    if result_item != "":
                        pidResult.append(result_item)
                print(pidResult)
                pop = os.popen("adb -s " + SN + " shell kill -9 " + pidResult[3])
                global_ms.text_print.emit("adb -s " + SN + " shell kill -9 " + pidResult[3])
                pop.close()
                global_ms.text_print.emit("设备[" + SN + "]monkey停止成功")
            else:
                global_ms.text_print.emit("未找到设备[" + SN + "]的monkey pid，已停止或未进行monkey测试")
    if len(SN_list) == 1:
        pidResult = []
        pop = os.popen("adb shell ps -le |findstr monkey")
        global_ms.text_print.emit("adb shell ps -le |findstr monkey")
        read_result = pop.read().split("\n")
        if len(read_result) > 1:
            for result_item in read_result[0].split(" "):
                if result_item != "":
                    pidResult.append(result_item)
            print(pidResult)
            pop = os.popen("adb shell kill -9 " + pidResult[3])
            global_ms.text_print.emit("adb shell kill -9 " + pidResult[3])
            pop.close()
            global_ms.text_print.emit("设备[" + SN_list[0] + "]monkey停止成功")
        else:
            global_ms.text_print.emit("未找到设备[" + SN_list[0] + "]的monkey pid，已停止或未进行monkey测试")
    elif len(SN_list) < 1:
        global_ms.text_print.emit("未连接设备！")

def showMessage(msg):
    global index
    ui.MessageText.append(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "--> " + msg)
    if msg == "所有设备bugreport导出完毕":
        index += 1
    if msg == "所有设备导出log完毕":
        index += 1
    if exportLog == True and exportBugreport == False:
        if msg == "所有设备monkey结果分析结束":
            ui.MessageText.append(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "--> 等待log导出...")
        if index == 1:
            ui.exportButton.setEnabled(True)
            ui.exportButton.setText("重新导出")
            ui.exportButton.setStyleSheet("QPushButton{background-color:'#3498db';}")
            ui.MessageText.append("--程序结束--")
    if exportLog == False and exportBugreport == True:
        if msg == "所有设备monkey结果分析结束":
            ui.MessageText.append(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "--> 等待bugreport导出...")
        if index == 1:
            ui.exportButton.setEnabled(True)
            ui.exportButton.setStyleSheet("QPushButton{background-color:'#3498db';}")
            ui.exportButton.setText("重新导出")
            ui.MessageText.append("--程序结束--")
    if exportLog and exportBugreport:
        if msg == "所有设备monkey结果分析结束":
            ui.MessageText.append(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "--> 等待剩余项目导出...")
        if index == 1 and msg == "所有设备导出log完毕":
            ui.MessageText.append(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "--> 等待bugreport导出...")
        if index == 1 and msg == "所有设备bugreport导出完毕":
            ui.MessageText.append(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "--> 等待log导出...")
        if index == 2:
            ui.exportButton.setEnabled(True)
            ui.exportButton.setText("重新导出")
            ui.exportButton.setStyleSheet("QPushButton{background-color:'#3498db';}")
            ui.MessageText.append("--程序结束--")
    if msg == "所有设备monkey结果分析结束" and exportBugreport == False and exportLog == False:
        ui.exportButton.setEnabled(True)
        ui.exportButton.setText("重新导出")
        ui.exportButton.setStyleSheet("QPushButton{background-color:'#3498db';}")
        ui.MessageText.append("--程序结束--")


global_ms.text_print.connect(showMessage)


def clearMessage():
    ui.MessageText.setPlainText("")


def getInfo():
    global wholeMonkey
    global singleMonkey
    global logPath
    global outPath
    global exportLog
    global exportBugreport
    wholeMonkey = ui.WholeMonkeyRadio.isChecked()
    singleMonkey = ui.SingleMonkeyRadio.isChecked()
    if ui.updateLogPathCheck.isChecked():
        logPath = ui.LogPathInput.text()
    if ui.updateOutPathCheck.isChecked():
        outPath = ui.OutputPathInput.text()
    exportLog = ui.logCheck.isChecked()
    exportBugreport = ui.bugreportCheck.isChecked()
    if outPath[-1] != "\\":
        outPath = outPath + "\\"


def get_devices():
    result.clear()
    SN_list.clear()
    ui.DevicesText.setText("")
    pop = os.popen("adb devices")
    showMessage("adb devices")
    read_result = pop.read().split("\n")
    read_result_index = 0
    for i, s in enumerate(read_result):
        if s == "List of devices attached":
            read_result_index = i
    for i, s in enumerate(read_result):
        if s != "" and (i >= read_result_index):
            result.append(s)
    pop.close()
    if len(result) > 1:
        ui.DevicesText.setPlainText("")
        ui.exportButton.setEnabled(True)
        ui.stopMonkeyButton.setEnabled(True)
        ui.stopMonkeyButton.setStyleSheet("QPushButton{background-color:'#e67e22';}")
        ui.exportButton.setStyleSheet("QPushButton{background-color:'#3498db';}")
        ui.DevicesText.append("已连接[" + str(len(result) - 1) + "]台设备")
        for i in range(1, len(result)):
            ui.DevicesText.append("设备[" + str(i) + "]SN: " + result[i][:-7])
            SN_list.append(result[i][:-7])
        print(SN_list)
    elif len(result) <= 1:
        ui.exportButton.setEnabled(False)
        ui.stopMonkeyButton.setEnabled(False)
        ui.stopMonkeyButton.setStyleSheet("QPushButton{background-color:'lightgray';}")
        ui.exportButton.setStyleSheet("QPushButton{background-color:'lightgray';}")
        ui.DevicesText.setPlaceholderText("未连接设备!请连接设备或检查ADB调试是否开启。")


def setConnectDevices():
    get_devices()


if __name__ == '__main__':
    app = QApplication()
    window = QMainWindow()
    ui.setupUi(window)
    initWindow()
    window.setWindowIcon(QIcon('./ui/favicon.ico'))
    window.setWindowTitle("MonkeyExport-3.4")
    window.show()
    sys.exit(app.exec_())
