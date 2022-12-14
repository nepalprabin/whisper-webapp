# Stanford NLP Lecture Transcription 

This project transcripted Stanford NLP Lectures using OpenAI's whisper

# Description
This is a web app that shows transcibed NLP lectures. The web application is hosted [here](http://3.14.28.154/).

## Getting Started

### Dependencies
This application uses flask to host the transcripted NLP lectures.

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* Clone the repo:
    ```
    https://github.com/nepalprabin/whisper-webapp.git
    ```
* Install deoendencies
    ``` pip install -r requirements.txt ```
* Run the app
    ``` python app.py``` or ```flask run```


### Deploying the application
If you want to deploy the flask application in AWS EC2 istance then do the following: 

* Create AWS EC2 instance and create key pairs and download it
* SSH into the instance using the key pair
* Clone the repo into the instance
    ``` git clone https://github.com/nepalprabin/whisper-webapp.git ``` 
* Create a virtual environment for python
    ``` python -m venv venv```
* Activate the environment
    ```source venv/bin/activate```
* Install the dependencies inside the virtual environment
    ```pip install -r requirements.txt```
* Install required packages
    ```sudo apt-get update```
    ```sudo apt-get install nginx```
    ```sudo apt-get install gunicorn3```
* Configure nginx settings
    ```sudo nano /etc/nginx/sites-enabled/whisper-app```
* Save the following config file
    ```server {
    listen 80;
    server_name 0.0.0.0;

    location / {
        proxy_pass http://127.0.0.1:8000;
        }
    }
    ```
* Restart nginx
    ```sudo service nginx restart```
* Run gunicorn
    ```gunicorn3 wsgi:app```
* Configure gunicorn service
    ```sudo nano /etc/systemd/system/whisper-webapp.service```
* Enter following config in the gunicorn service
    ```[Unit]
        Description=AWS Flask app
        After=network.target

        [Service]
        User=ubuntu
        Group=www-data
        WorkingDirectory=/home/ubuntu/flask_aws
        ExecStart=/usr/bin/gunicorn3  --bind unix:whisper-webapp.sock wsgi:app```
* Reload the system daemon
    ```sudo systemctl daemon-reload```
* Restart the service
    ```sudo service whisper-webapp restart```
* Change the following in nginx config ```sudo nano /etc/nginx/sites-enabled/whisper-webapp```
    ```
    1)Proxy pass to http://unix:/home/ubuntu/whisper-webapp/whisper-webapp.sock
    2)Server name to <Public IP of EC2 instance>
    ``` 
* Restart nginx
    ```sudo service nginx restart```

We should be able to view our app in EC2 public IP. 