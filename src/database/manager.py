"""Gestionnaire de base de données SQLite."""
import sqlite3

class DatabaseManager:
    """Gestion des opérations CRUD sur SQLite."""
    
    def __init__(self, db_name="carnet_adresses.db"):
        self.db_name = db_name
        self.connection = None
    
    def connect(self):
        """Établit une connexion à la base de données."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            return True
        except sqlite3.Error as e:
            print(f"Erreur de connexion: {e}")
            return False
    
    def create_table(self):
        """Crée la table contacts si elle n'existe pas."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    prenom TEXT NOT NULL,
                    telephone TEXT,
                    courriel TEXT
                )
            """)
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erreur création table: {e}")
            return False
    
    def add_contact(self, nom, prenom, telephone, courriel):
        """Ajoute un nouveau contact."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO contacts (nom, prenom, telephone, courriel)
                VALUES (?, ?, ?, ?)
            """, (nom, prenom, telephone, courriel))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erreur ajout contact: {e}")
            return False
    
    def get_all_contacts(self):
        """Récupère tous les contacts."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM contacts ORDER BY nom, prenom")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erreur récupération: {e}")
            return []
    
    def update_contact(self, contact_id, nom, prenom, telephone, courriel):
        """Met à jour un contact existant."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE contacts
                SET nom=?, prenom=?, telephone=?, courriel=?
                WHERE id=?
            """, (nom, prenom, telephone, courriel, contact_id))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erreur modification: {e}")
            return False
    
    def delete_contact(self, contact_id):
        """Supprime un contact."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erreur suppression: {e}")
            return False
    
    def close(self):
        """Ferme la connexion."""
        if self.connection:
            self.connection.close()
