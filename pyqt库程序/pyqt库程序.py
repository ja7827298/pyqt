import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('待办事项列表')
        self.setGeometry(100, 100, 400, 300)

        # 创建布局
        layout = QVBoxLayout()

        # 创建待办事项输入框
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("输入待办事项")
        layout.addWidget(self.todo_input)

        # 创建待办事项列表
        self.todo_list = QListWidget()
        layout.addWidget(self.todo_list)

        # 创建按钮
        self.add_button = QPushButton('添加')
        self.add_button.clicked.connect(self.add_todo)
        layout.addWidget(self.add_button)

        self.delete_button = QPushButton('删除')
        self.delete_button.clicked.connect(self.delete_todo)
        layout.addWidget(self.delete_button)

        # 设置布局
        self.setLayout(layout)

    def add_todo(self):
        todo = self.todo_input.text()
        if todo:
            self.todo_list.addItem(todo)
            self.todo_input.clear()
        else:
            QMessageBox.warning(self, "警告", "请输入待办事项内容！")

    def delete_todo(self):
        selected_items = self.todo_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "警告", "请选择要删除的待办事项！")
        else:
            for item in selected_items:
                self.todo_list.takeItem(self.todo_list.row(item))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToDoApp()
    ex.show()
    sys.exit(app.exec_())
