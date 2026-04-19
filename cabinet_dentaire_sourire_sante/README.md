# Cabinet Dentaire Sourire Sante

Application web Flask pour gerer les patients, dentistes et rendez-vous d'un cabinet dentaire.

## Fonctionnalites
- Authentification: `login` / `signup` / `logout`
- Gestion des patients: ajouter, modifier, supprimer, lister
- Gestion des dentistes: ajouter, modifier, supprimer, lister
- Gestion des rendez-vous: ajouter, modifier, supprimer, filtrer par date
- Gestion des roles:
  - `admin`: acces total
  - `secretaire`: patients + rendez-vous
  - `dentiste`: consultation et mise a jour de ses rendez-vous

## Technologies
- Flask (Python)
- HTML/CSS
- MySQL (Laragon ou XAMPP)

## Installation
1. Ouvrir le dossier du projet:
   - `cd cabinet_dentaire_sourire_sante`
2. Creer un environnement virtuel:
   - `python -m venv .venv`
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
3. Installer les dependances:
   - `pip install -r requirements.txt`
4. Creer la base MySQL:
   - Importer le fichier `schema.sql` dans phpMyAdmin (Laragon/XAMPP),
   - ou executer son contenu depuis MySQL.
5. Configurer les variables d'environnement:
   - Copier `.env.example` en `.env`
   - Ajuster `MYSQL_USER`, `MYSQL_PASSWORD`, etc.
6. Lancer l'application:
   - `flask --app app run --debug`

## Interfaces HTML
- `login.html`
- `signup.html`
- `index.html`
- `patients.html`
- `dentists.html`
- `appointments.html`
- `add_patient.html` / `edit_patient.html`
- `add_dentist.html` / `edit_dentist.html`
- `add_appointment.html` / `edit_appointment.html`

## Notes Laragon
- Hote: `localhost`
- Port MySQL: `3306`
- Utilisateur par defaut: `root`
- Mot de passe: vide (selon configuration)

Si vous utilisez XAMPP, la configuration est similaire (`localhost`, `3306`, `root`).
