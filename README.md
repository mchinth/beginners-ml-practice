# Machine Learning Environment Setup

This repository provides a simple setup for creating a Python virtual environment for machine learning development.

## **Setup Instructions**

### **1. Running the Setup Script**
#### **Linux/macOS**
```bash
chmod +x setup.sh  # Make executable
./setup.sh         # Run setup
```

#### **Windows**
```batch
setup.bat
```

### **2. Activating the Virtual Environment**
#### **Linux/macOS**
If the virtual environment exists, the script returns early and provides an activation command:
```bash
source .venv_$(hostname)/bin/activate
```
To deactivate:
```bash
deactivate
```

#### **Windows**
```batch
call .venv_%COMPUTERNAME%\Scripts\activate
```
To deactivate:
```batch
deactivate
```

### **3. Installed Packages**
- `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `scipy`, `seaborn`
- `jupyter`, `ipython`, `notebook`

### **4. Troubleshooting**
- **Slow Setup:** Use a local directory instead of network storage:
  ```bash
  python3 -m venv ~/my_project_venv
  source ~/my_project_venv/bin/activate
  ```
- **Package Installation Issues:** Ensure pip is up-to-date:
  ```bash
  python3 -m ensurepip --upgrade
  python3 -m pip install --upgrade pip setuptools wheel
  ```
- **System Python Conflicts:** Install `venv` properly:
  ```bash
  sudo apt install python3-venv python3-pip -y
  ```
