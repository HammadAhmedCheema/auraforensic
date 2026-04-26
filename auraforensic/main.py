import sys
from PyQt6.QtWidgets import QApplication
from auraforensic.models.database import init_db
from auraforensic.controllers.main_controller import MainController

def main():
    # Initialize SQLite database
    init_db()
    
    app = QApplication(sys.argv)
    
    # Initialize the primary controller which manages the view
    controller = MainController()
    controller.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
