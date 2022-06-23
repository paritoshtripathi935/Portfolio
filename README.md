<h1 align="center">Personal Portfolio</h1>

<div align= "center">
  <h4>A Personal Portfolio Website built using Django</h4>
</div>

### :star: Star us on GitHub — it helps!


![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/tsvillain/Twitter-Bot/issues)
[![MIT License](https://img.shields.io/github/license/tsvillain/Twitter-Bot.svg?style=flat-square)](https://github.com/tsvillain/Twitter-Bot/blob/master/LICENSE)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/paritosh-tripathi-social/)

## 🚀&nbsp; Installation

#### Clone the repo
```
$ git clone https://github.com/paritoshtripathi935/Portfolio.git
```
#### Make a Virtual Environment
```
$ python3 -m venv venv
```
#### Activate virtual Envirnoment
```
$ source venv/bin/activate
```
#### Install Requirenments
```
$ pip install -r requirements.txt
```
## :bulb: Working
#### Create a Django Project
```
$ python manage.py startproject personal_portfolio
```
#### Start a app
Here we will be putting our main code.
```
$ python manage.py startapp Portfolio
```

## Deployment
This website has been deployed using heroku.
1 - Add a .gitignore file for Django, Python and Vscode(for me).
2 - Run below command and save a requirements file.
```
$ pip freeze requirements.txt
```
3 - Add a procfile like a above.

4 - change debug = False.

5 - After deploying run below in heroku bash 
```
$ python3 manage.py migrate
```

## For more Refer to this notion page - 

[Documentation](https://www.notion.so/paritoshtripathi/ce6ebac1d3864bdba62038d1c75aee36?v=f407e19208c14f84b68c7c5bb889c821)

## I used these resources - 
[django Gosting](https://realpython.com/django-hosting-on-heroku/#demo-what-youll-build)
[Setup Django](https://realpython.com/get-started-with-django-1/#set-up-your-development-environment)
