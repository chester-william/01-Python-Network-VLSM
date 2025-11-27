
# VLSM Calculator Flask App

**VLSM Calculator based on Python Flask** with Bootstrap view. This application allows you to calculate VLSM subnets automatically and save the results to an Excel file.

---

## ✅ Main fitur
- Input the number of networks, initial IP, network name, and IP allocation.
- Validate IP format (IPv4).
- Automatic form reset.
- Modern look using Bootstrap.
- The calculation results are displayed in a table and can be downloaded as an Excel file.

---

## 📂 Project Structure 
```
vlsm_app/
│
├── app.py                # Main file
├── templates/
│   ├── index.html        # Form input
│   └── result.html       # View VLSM result 
├── static/
│   └── style.css         # Custom CSS
└── vlsm_result.xlsx      # Result file 
```

---

## 🚀 How deploy in local 

### 1. Clone Repository
```bash
git clone https://github.com/username/vlsm_app.git
cd vlsm_app
```

### 2. Make Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3. Install Dependencies
```bash
pip install flask pandas openpyxl
```

### 4. Run the Application
```bash
python app.py
```

Access via browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 Deploy ke GitHub
1. Make sure all files are in the project folder.
2. Create a repository on GitHub.
3. Push the project:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/vlsm_app.git
git push -u origin main
```

---

## ✅ Notes
- Make sure Python 3.x is installed
- If you wondering deploy **Heroku** or **Railway**, add file `requirements.txt` and `Procfile`.

requirements.txt:
```
flask
pandas
openpyxl
```

Procfile:
```
web: python app.py
```

---

Enjoy using VLSM Calculator!🚀