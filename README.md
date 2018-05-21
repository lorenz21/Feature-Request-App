# Engineering Project
---
### Feature Request App
Web application that allows users to create "feature requests".


## Requirements

* python 3.6.5
* Flask 1.0.2
* Flask-Bootstrap 3.3.7


## Build Setup

1. Create venv (Recommended)
  ```bash
  python3 -m venv <virtual_env_name>
  ```

2. Install requirements

  ```bash
  pip install -r requirements.txt
  ```

4. Export environment variables

  ```bash
  export FLASK_APP=featurerequest.py
  ```

5. Build database

  ```bash
  flask db init
  ```
    ```bash
  flask db migrate -m"initial build"
  ```
    ```bash
  flask db upgrade
  ```

6. run

  ```bash
  flask run  
  # server at http://127.0.0.1:5000/
