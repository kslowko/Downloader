# First, we import the necessary modules:
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog


# sys is used to interact with the Python interpreter. QtWidgets is used to create the application window and user interface. Qt is used to set the alignment of the widgets in the interface. QFileDialog is used to allow the user to browse for a download directory.

# We define the YouTubeDownloader class:
class YouTubeDownloader(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # URL input
        self.url_label = QtWidgets.QLabel('Enter YouTube video URL:')
        self.url_entry = QtWidgets.QLineEdit()

        # Destination directory input
        self.destination_label = QtWidgets.QLabel('Select download destination:')
        self.destination_entry = QtWidgets.QLineEdit()
        self.browse_button = QtWidgets.QPushButton('Browse')
        self.browse_button.clicked.connect(self.browse_directory)

        # Download button
        self.download_button = QtWidgets.QPushButton('Download as Video')
        self.download_button.clicked.connect(self.download_video)

        # Download as mp3 button
        self.download_mp3_button = QtWidgets.QPushButton('Download as audio')
        self.download_mp3_button.clicked.connect(self.download_as_audio)

        # Log output
        self.log_label = QtWidgets.QLabel('Log:')
        self.log_text_edit = QtWidgets.QTextEdit()
        self.log_text_edit.setReadOnly(True)

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_entry)
        layout.addWidget(self.destination_label)
        destination_layout = QtWidgets.QHBoxLayout()
        destination_layout.addWidget(self.destination_entry)
        destination_layout.addWidget(self.browse_button)
        layout.addLayout(destination_layout)
        layout.addWidget(self.download_button)
        layout.addWidget(self.download_mp3_button)
        layout.addWidget(self.log_label)
        layout.addWidget(self.log_text_edit)
        self.setLayout(layout)

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('YouTube Video Downloader')
        self.show()

    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.destination_entry.setText(directory)

    def download_video(self):
        # Get video URL and destination directory
        url = self.url_entry.text()
        destination_directory = self.destination_entry.text()

        # Download the video
        self.log('Downloading video...')
        os.system(f'yt-dlp -o "{destination_directory}/%(title)s.%(ext)s" {url}')
        self.log('Download completed!')

    def download_as_audio(self):
        # Get video URL and destination directory
        url = self.url_entry.text()
        destination_directory = self.destination_entry.text()

        # Pobierz plik audio w formacie MP3
        self.log('Downloading audio as MP3...')
        os.system(f'yt-dlp -x --audio-format mp3 -o "{destination_directory}/%(title)s.%(ext)s" {url}')
        self.log('Download completed!')

    def log(self, message):
        """Log a message to the log window"""
        self.log_text_edit.append(message)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    downloader = YouTubeDownloader()
    sys.exit(app.exec_())

