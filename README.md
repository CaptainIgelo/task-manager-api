# task-manager-api
A RESTful API for managing tasks. built to practice backend development with **Django REST Framework**. 


## Features 

- Creat, read, update, and delete (CRUD) 
- Status tracking (`todo`, `in_progress`, `done`)
- Automatic timestamps (`create_at`, `updated_at`)
- Browsable API via Django REST Framework 

## Tech Stack 
- **Python 3.12.1** 
- **Django 6.0.3**
- **Django REST Framework** 

## Getting started

```bash 
# clone repo  
git clone https://github.com/CaptainIgelo/task-manager-api.git
cd task-manager-api

# create virtual enviroment  
python -m venv venv 
source venv/bin/activate

# install requiremantes  
pip install -r requirements.txt 

# migrate DB 
python manage.py migrate

# start server 
python manage.py runserver
``` 

## API Endpoints

| Method | Endpoint | description |
|--------|----------|--------------|
| GET | `/api/tasks/` | List all tasks |
| POST | `/api/tasks/` | Create a task |
| GET | `/api/tasks/{id}/` | Get a task |
| PUT | `/api/tasks/{id}/` | Replace a task |
| PATCH | `/api/tasks/{id}/` | Update a task  |
| DELETE | `/api/tasks/{id}/` | Delete a task |

## Example response  
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

## Filtering

The API supports filtering, searching, and sorting:

| Parameter | Example | Description |
|-----------|----------|--------------|
| `status` | `/api/tasks/?status=todo` | Filter by Status |
| `search` | `/api/tasks/?search=Meeting` | Search title & description |
| `ordering` | `/api/tasks/?ordering=-created_at` | Sort results |

**Status values:** `todo` · `in_progress` · `done`