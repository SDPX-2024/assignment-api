## Installation
**Set virtual environment:**
```bash
python3 -m venv .venv
```

**Activate virtual environment:**
- macOS/Linux
```bash
source .venv/bin/activate 
```  

- Windows:
```bash
.venv\Scripts\activate 
```  

**install dependencies:**
```bash
pip install -r requirements.txt 
```

## Run Flask
```bash
python ./flask_api/app.py
```

## Endpoints
- GET /
- GET /user
- GET /user/{id}
- POST /user/new
- PUT /user/{id}
- DELETE /user/{id}