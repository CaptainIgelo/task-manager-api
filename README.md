# task-manager-api
A RESTful  Tast Manager API built with Django REST Framework 

Eine RESTful API zur Aufgabenverwaltung, gebaut mit **Django** und **Django REST Framework**.

## Features 

- Aufgaben erstellen, lesen, updaten und löschen (CRUD) 
- Status-Tracking (`todo`, `in_progress`, `done`)
- Automatische Zeitstempel (`create_at`, `updated_at`)
- Browsable API via Django REST Framework 

## Tech Stack 
- **Python 3.12.1** 
- **Django 6.0.3**
- **Django REST Framework** 

## Installation & Setup

```bash 
# Repository klonen 
git clone https://github.com/CaptainIgelo/task-manager-api.git
cd task-manager-api

# Virtuelles Enviroment erstellen 
python -m venv venv 
source venv/bin/activate

# Abhängigkeiten Installieren 
pip install -r requirements.txt 

# Datenbank migrieren 
python manage.py migrate

# Server starten 
python manage.py runserver
``` 

## API Endpunkte

| Method | Endpunkt | Beschreibung |
|--------|----------|--------------|
| GET | `/api/tasks/` | Alle Tasks abrufen |
| POST | `/api/tasks/` | Neuen Task erstellen |
| GET | `/api/tasks/{id}/` | Einzelnen Task abrufen |
| PUT | `/api/tasks/{id}/` | Task komplett updaten |
| PATCH | `/api/tasks/{id}/` | Task teilweise updaten |
| DELETE | `/api/tasks/{id}/` | Task löschen |

## Beispiel 
```Json
{
    "id": 1,
    "title": "Mein erster Task", 
    "description": "Erste funktionierende API",
    "status": "todo", 
    "created_at": "2026-03-31T13:49:00",
    "updated_at": "2026-03-31T13:49:00"
}
```

## Filtering & Suche

Die API unterstützt Filterung, Suche und Sortierung:

| Parameter | Beispiel | Beschreibung |
|-----------|----------|--------------|
| `status` | `/api/tasks/?status=todo` | Nach Status filtern |
| `search` | `/api/tasks/?search=Meeting` | In Titel & Beschreibung suchen |
| `ordering` | `/api/tasks/?ordering=-created_at` | Ergebnisse sortieren |

**Verfügbare Status-Werte:** `todo` · `in_progress` · `done`