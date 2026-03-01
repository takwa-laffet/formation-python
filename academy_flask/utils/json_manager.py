import json
import os


class JsonManager:
    """Gestionnaire de fichiers JSON pour la persistance des données"""
    
    @staticmethod
    def read(file_path):
        """Lit un fichier JSON et retourne les données"""
        if not os.path.exists(file_path):
            return []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, IOError):
            return []
    
    @staticmethod
    def write(file_path, data):
        """Écrit des données dans un fichier JSON"""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    @staticmethod
    def append(file_path, item):
        """Ajoute un élément à un fichier JSON"""
        data = JsonManager.read(file_path)
        data.append(item)
        JsonManager.write(file_path, data)
    
    @staticmethod
    def update(file_path, item_id, updated_item, id_key='id'):
        """Met à jour un élément dans un fichier JSON"""
        data = JsonManager.read(file_path)
        
        for i, item in enumerate(data):
            if item.get(id_key) == item_id:
                data[i] = updated_item
                break
        
        JsonManager.write(file_path, data)
    
    @staticmethod
    def delete(file_path, item_id, id_key='id'):
        """Supprime un élément d'un fichier JSON"""
        data = JsonManager.read(file_path)
        
        data = [item for item in data if item.get(id_key) != item_id]
        
        JsonManager.write(file_path, data)
    
    @staticmethod
    def find_by_id(file_path, item_id, id_key='id'):
        """Recherche un élément par ID"""
        data = JsonManager.read(file_path)
        
        for item in data:
            if item.get(id_key) == item_id:
                return item
        
        return None
    
    @staticmethod
    def find_all(file_path):
        """Retourne tous les éléments"""
        return JsonManager.read(file_path)
