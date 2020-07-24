# mysql-deploy
Python module to deploy DB in Clusters

## Setup Environment
This python module is compatible with python 3.6
1. Setup python3 environment
2. Install pip
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
Install virtual environment and dependencies 
```
virtualenv venv
pip install -r requirements
```

## Deploy DB Schema
1. Define the databases & Clusters in config
2. Define Cluster endpoints in config
3. Define Current Environment in run_configs.json
4. Execute main.py