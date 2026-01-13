"""Dialogues pour l'interface utilisateur."""
from PyQt6.QtWidgets import (
    QDialog, QFormLayout, QLineEdit, QPushButton,
    QHBoxLayout, QMessageBox
)

class ContactDialog(QDialog):
    """Dialogue pour ajouter/modifier un contact."""
    
    def __init__(self, parent=None, contact=None):
        super().__init__(parent)
        self.contact = contact
        self.setup_ui()
    
    def setup_ui(self):
        self.setWindowTitle("Ajouter un contact" if not self.contact else "Modifier")
        self.setMinimumWidth(400)
        
        layout = QFormLayout()
        
        self.nom_input = QLineEdit()
        self.prenom_input = QLineEdit()
        self.telephone_input = QLineEdit()
        self.courriel_input = QLineEdit()
        
        if self.contact:
            self.nom_input.setText(self.contact[1])
            self.prenom_input.setText(self.contact[2])
            self.telephone_input.setText(self.contact[3] or "")
            self.courriel_input.setText(self.contact[4] or "")
        
        layout.addRow("Nom *:", self.nom_input)
        layout.addRow("Prénom *:", self.prenom_input)
        layout.addRow("Téléphone:", self.telephone_input)
        layout.addRow("Courriel:", self.courriel_input)
        
        button_layout = QHBoxLayout()
        save_button = QPushButton("Enregistrer")
        cancel_button = QPushButton("Annuler")
        
        save_button.clicked.connect(self.validate_and_accept)
        cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addRow(button_layout)
        
        self.setLayout(layout)
    
    def validate_and_accept(self):
        if not self.nom_input.text().strip() or not self.prenom_input.text().strip():
            QMessageBox.warning(self, "Erreur", "Nom et prénom obligatoires!")
            return
        self.accept()
    
    def get_data(self):
        return (
            self.nom_input.text().strip(),
            self.prenom_input.text().strip(),
            self.telephone_input.text().strip(),
            self.courriel_input.text().strip()
        )
