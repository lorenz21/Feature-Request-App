# Engineering Project
---

### Live DEMO
[Heroku App](https://insurance-feature-request.herokuapp.com)

### Feature Request App
Web application that allows users to create "feature requests".


## Requirements

* python 3.6.5
* Flask 1.0.2
* Flask-Bootstrap 3.3.7


## Build Setup

1. Clone the repository
  ```bash
  git clone https://github.com/lorenz21/Feature-Request-App.git
  ```

2. Change Directories into the project
  ```bash
  cd Feature-Request-App
  ```

3. Create venv (Recommended)
  ```bash
  python3 -m venv <virtual_env_name>
  ```

4. Install requirements
  ```bash
  pip install -r requirements.txt
  ```

5. Export environment variables
  ```bash
  export FLASK_APP=featurerequest.py
  ```

6. Build database
  ```bash
  flask db init
  flask db migrate -m"initial build"
  flask db upgrade
  ```

7. run
  ```bash
  flask run  
  # server at http://127.0.0.1:5000/
