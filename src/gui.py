import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFileDialog, QComboBox, QMessageBox, QPlainTextEdit, QGridLayout
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
from utils.image_utils import load_image, save_image
from algorithms.lsb import encode_lsb, decode_lsb
from algorithms.lsbm import encode_lsbm, decode_lsbm
from algorithms.rlsb import encode_rlsb, decode_rlsb

class SteganographyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Steganography App')
        self.setWindowIcon(QIcon('icon.png'))  # Add an appropriate icon file if available
        self.setGeometry(100, 100, 800, 600)

        layout = QGridLayout()

        # Action selection
        action_label = QLabel('Action:')
        self.action_combo = QComboBox()
        self.action_combo.addItem('Encode')
        self.action_combo.addItem('Decode')
        self.action_combo.currentIndexChanged.connect(self.update_ui)
        layout.addWidget(action_label, 0, 0)
        layout.addWidget(self.action_combo, 0, 1)

        # Algorithm selection
        algorithm_label = QLabel('Algorithm:')
        self.algorithm_combo = QComboBox()
        self.algorithm_combo.addItem('LSB')
        self.algorithm_combo.addItem('LSBM')
        self.algorithm_combo.addItem('RLSB')
        layout.addWidget(algorithm_label, 1, 0)
        layout.addWidget(self.algorithm_combo, 1, 1)

        # Input image
        input_image_label = QLabel('Input Image:')
        self.input_image_edit = QLineEdit()
        self.input_image_button = QPushButton('Browse...')
        self.input_image_button.clicked.connect(self.browse_input_image)
        layout.addWidget(input_image_label, 2, 0)
        layout.addWidget(self.input_image_edit, 2, 1)
        layout.addWidget(self.input_image_button, 2, 2)

        # Output image (only for encoding)
        self.output_image_label = QLabel('Output Image:')
        self.output_image_edit = QLineEdit()
        self.output_image_button = QPushButton('Browse...')
        self.output_image_button.clicked.connect(self.browse_output_image)
        layout.addWidget(self.output_image_label, 3, 0)
        layout.addWidget(self.output_image_edit, 3, 1)
        layout.addWidget(self.output_image_button, 3, 2)

        # Message/Seed
        self.message_label = QLabel('Message:')
        self.message_edit = QPlainTextEdit()
        layout.addWidget(self.message_label, 4, 0)
        layout.addWidget(self.message_edit, 4, 1, 1, 2)

        # Process button
        self.process_button = QPushButton('Process')
        self.process_button.clicked.connect(self.process)
        layout.addWidget(self.process_button, 5, 0, 1, 3)

        # Image preview
        self.input_image_preview = QLabel()
        self.input_image_preview.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.input_image_preview, 0, 3, 4, 2)

        self.output_image_preview = QLabel()
        self.output_image_preview.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.output_image_preview, 4, 3, 2, 2)

        self.setLayout(layout)

        self.update_ui()

    def browse_input_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Input Image", "", "Images (*.png *.jpg *.bmp)", options=options)
        if file_name:
            self.input_image_edit.setText(file_name)
            self.input_image_preview.setPixmap(QPixmap(file_name).scaled(200, 200, Qt.KeepAspectRatio))

    def browse_output_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Select Output Image", "", "Images (*.png *.jpg *.bmp)", options=options)
        if file_name:
            self.output_image_edit.setText(file_name)

    def update_ui(self):
        action = self.action_combo.currentText()
        if action == 'Encode':
            self.output_image_label.setVisible(True)
            self.output_image_edit.setVisible(True)
            self.output_image_button.setVisible(True)
            self.message_label.setText('Message:')
            self.message_edit.setReadOnly(False)
        elif action == 'Decode':
            self.output_image_label.setVisible(False)
            self.output_image_edit.setVisible(False)
            self.output_image_button.setVisible(False)
            self.message_label.setText('Seed (for RLSB):')
            self.message_edit.setReadOnly(True)

    def process(self):
        action = self.action_combo.currentText().lower()
        algorithm = self.algorithm_combo.currentText().lower()
        input_image_path = self.input_image_edit.text()
        output_image_path = self.output_image_edit.text()
        message_or_seed = self.message_edit.toPlainText()

        if not input_image_path:
            QMessageBox.warning(self, 'Warning', 'Please fill in the input image field.')
            return

        try:
            if action == 'encode':
                if not message_or_seed:
                    QMessageBox.warning(self, 'Warning', 'Please enter a message to encode.')
                    return
                message = message_or_seed
                if not output_image_path:
                    QMessageBox.warning(self, 'Warning', 'Please enter an output image path.')
                    return
                if algorithm == 'lsb':
                    self.encode_lsb_mode(input_image_path, output_image_path, message)
                elif algorithm == 'lsbm':
                    self.encode_lsbm_mode(input_image_path, output_image_path, message)
                elif algorithm == 'rlsb':
                    seed = int(message_or_seed) if message_or_seed.isdigit() else 12345
                    self.encode_rlsb_mode(input_image_path, output_image_path, message, seed)
                else:
                    QMessageBox.warning(self, 'Warning', f'Unknown algorithm: {algorithm}')
                    return
            elif action == 'decode':
                seed = int(message_or_seed) if algorithm == 'rlsb' and message_or_seed.isdigit() else 12345
                if algorithm == 'lsb':
                    self.decode_lsb_mode(input_image_path)
                elif algorithm == 'lsbm':
                    self.decode_lsbm_mode(input_image_path)
                elif algorithm == 'rlsb':
                    self.decode_rlsb_mode(input_image_path, seed)
                else:
                    QMessageBox.warning(self, 'Warning', f'Unknown algorithm: {algorithm}')
                    return

            self.output_image_preview.setPixmap(QPixmap(output_image_path).scaled(200, 200, Qt.KeepAspectRatio) if output_image_path else QPixmap())
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))
            return

    def encode_lsb_mode(self, input_image_path, output_image_path, message):
        input_image = load_image(input_image_path)
        encoded_image = encode_lsb(input_image, message)
        save_image(encoded_image, output_image_path)
        QMessageBox.information(self, 'Success', f'Message encoded using LSB and saved to {output_image_path}')

    def decode_lsb_mode(self, input_image_path):
        input_image = load_image(input_image_path)
        message = decode_lsb(input_image)
        QMessageBox.information(self, 'Success', f'Decoded message using LSB: {message}')

    def encode_lsbm_mode(self, input_image_path, output_image_path, message):
        input_image = load_image(input_image_path)
        encoded_image = encode_lsbm(input_image, message)
        save_image(encoded_image, output_image_path)
        QMessageBox.information(self, 'Success', f'Message encoded using LSBM and saved to {output_image_path}')

    def decode_lsbm_mode(self, input_image_path):
        input_image = load_image(input_image_path)
        message = decode_lsbm(input_image)
        QMessageBox.information(self, 'Success', f'Decoded message using LSBM: {message}')

    def encode_rlsb_mode(self, input_image_path, output_image_path, message, seed):
        input_image = load_image(input_image_path)
        encoded_image = encode_rlsb(input_image, message, seed)
        save_image(encoded_image, output_image_path)
        QMessageBox.information(self, 'Success', f'Message encoded using RLSB with seed {seed} and saved to {output_image_path}')

    def decode_rlsb_mode(self, input_image_path, seed):
        input_image = load_image(input_image_path)
        message = decode_rlsb(input_image, seed)
        QMessageBox.information(self, 'Success', f'Decoded message using RLSB with seed {seed}: {message}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SteganographyApp()
    ex.show()
    sys.exit(app.exec_())
