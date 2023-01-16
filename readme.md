## Mini python app

- This is a python flask app

- requirements
    - ensure you have python and pip installed on your server/machine
    - ensure you have a stable internet to install flask

- setup virtual environment

```bash
    py -3 -m venv venv

    #activate the virtual environment
    venv\Scripts\activate
    #this will append (venv) on the command to identify that virtual environment is active

    # install flask
    pip install Flask

```
- running the application

```bash
    #run the app on debug to be able to view debug logs
    flask --app app --debug run
```

- deactivate virtual environment
    - press `ctrl` + `c` to cancle application running
    - enter the command `deactivate` to exit virtual environment
