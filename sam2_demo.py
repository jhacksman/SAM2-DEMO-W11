import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QComboBox

class SAM2Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SAM2 DEMO W11")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.start_button = QPushButton("Start Server")
        self.start_button.clicked.connect(self.start_server)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Server")
        self.stop_button.clicked.connect(self.stop_server)
        layout.addWidget(self.stop_button)

        self.mode_label = QLabel("Server Mode:")
        layout.addWidget(self.mode_label)

        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["LAN", "Local-only"])
        self.mode_combo.currentIndexChanged.connect(self.change_mode)
        layout.addWidget(self.mode_combo)

        self.webcam_label = QLabel("Select Webcam:")
        layout.addWidget(self.webcam_label)

        self.webcam_combo = QComboBox()
        self.webcam_combo.addItems(["Webcam 1", "Webcam 2"])  # Placeholder webcams
        self.webcam_combo.currentIndexChanged.connect(self.change_webcam)
        layout.addWidget(self.webcam_combo)

        self.status_label = QLabel("Server Status: Stopped")
        layout.addWidget(self.status_label)

        central_widget.setLayout(layout)

    def start_server(self):
        self.status_label.setText("Server Status: Running")
        print("Server started")

    def stop_server(self):
        self.status_label.setText("Server Status: Stopped")
        print("Server stopped")

    def change_mode(self, index):
        pass

    def change_webcam(self, index):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SAM2Demo()
    window.show()
    sys.exit(app.exec_())
