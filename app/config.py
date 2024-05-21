import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    PATH_FILES_MASUK = os.getenv('PATH_FILES_MASUK', 'C:\\xampp\\htdocs\\edisposisi\\files')
    PATH_FILES_KELUAR = os.getenv('PATH_FILES_KELUAR', 'C:\\xampp\\htdocs\\edisposisi\\files_keluar')

# Add any other configuration settings you need
