"""Point d'entrée de l'application."""
import sys
from PyQt6.QtWidgets import QApplication
from src.database.manager import DatabaseManager
from src.ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    db_manager = DatabaseManager()
    db_manager.connect()
    db_manager.create_table()
    
    window = MainWindow(db_manager)
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
