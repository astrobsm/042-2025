# MDCAN-DR Project

## Project Structure
- `backend/`: Flask backend (Python)
- `frontend/`: React frontend (Node.js)

## Deployment

### 1. GitHub
- Push the entire project to a GitHub repository.

### 2. Render.com

#### Backend (Flask)
- Set up a new Web Service on Render.
- Use `backend/` as the root directory.
- Set build command: `pip install -r requirements.txt`
- Set start command: `python app.py`
- Add environment variables as needed (e.g., for secrets).

#### Frontend (React)
- Set up a new Static Site on Render.
- Use `frontend/` as the root directory.
- Set build command: `npm install && npm run build`
- Set publish directory: `frontend/build`

## Local Development

### Backend
```
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
python app.py
```

### Frontend
```
cd frontend
npm install
npm start
```

---

For more details, see Render's documentation: https://render.com/docs/deploy-flask, https://render.com/docs/deploy-create-react-app
