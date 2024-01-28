# School Lesson Plan Maker

**Preface**

Having gained proficiency in [ORACLE APEX](https://apex.oracle.com/en/platform/apex-oracle-cloud/) for developing systems capable of producing automated reports, we decided to push our boundaries by exploring the possibility of achieving the same functionality exclusively through Python.

Given that Streamlit is a Python framework designed for creating Data Apps and supports HTML injection into the code body, we found it to be a suitable choice for our challenge. Surprisingly, the transition was smoother than anticipated.

# About the repository

## `📁 app/`
Contains all the python scripts

and
### Our landing page  <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" alt="html5" width="20" height="20" style="vertical-align: middle"/> `Home.py`

### `📁 pages/`
___

Contains all the different page and routes.
#### <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" alt="html5" width="20" height="20" style="vertical-align: middle"/> `Make_Lesson_Plan.py`
___

Page that allows you to make lesson plans.

![Alt text|200](app/assets/image.png)

![Alt text|200](app/assets/image-1.png)

#### <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" alt="html5" width="20" height="20" style="vertical-align: middle"/> `Print.py`
___

Allows you to filter the data according to date, class and section and print them in pdfs.

![Alt text](app/assets/image-2.png)

### `📁 utils/`

___

Contains <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" alt="html5" width="20" height="20" style="vertical-align: middle"/>  `essentials.py` which is responsible for -

* Generating Tables - `add_rows(), show_table()`
* Formatting Dates - `convert_to_date_time(), findDay(), date_translate()`
* Reading and Writing into CSV files - `write_to_csv(), read_csv()`

## <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" alt="html5" width="20" height="20" style="vertical-align: middle"/>  `main.py`

Code that runs the entire app

## 🗒️ requirements.txt
Contains all the installation dependencies.

## <img src="https://github.com/iamzehan/FastAPI-Beanie-MongoDB/assets/43857150/1965d7c4-ae5d-46b9-8c5e-fae7466ec91e" alt="html5" width="30" height="32" style="vertical-align: middle;"/> start.sh
Bash script that starts your virtual environment and app altogether. Run it using -
```bash
source start.sh
```

<h2 align = "center"> <img src="https://github.com/iamzehan/FastAPI-Beanie-MongoDB/assets/43857150/1965d7c4-ae5d-46b9-8c5e-fae7466ec91e" alt="html5" width="30" height="30" style="vertical-align: middle;"/> Setting up the Development Environment </h2>

<img src="https://github.com/iamzehan/FastAPI-Beanie-MongoDB/assets/43857150/1965d7c4-ae5d-46b9-8c5e-fae7466ec91e" alt="html5" width="20" height="20" style="vertical-align: middle;"/> Create Virtual Environment

```bash
virtualenv env
```
<img src="https://github.com/iamzehan/FastAPI-Beanie-MongoDB/assets/43857150/1965d7c4-ae5d-46b9-8c5e-fae7466ec91e" alt="html5" width="20" height="20" style="vertical-align: middle;"/> Activate `env`

```bash
source env/Scripts/activate
```

<img src="https://github.com/iamzehan/FastAPI-Beanie-MongoDB/assets/43857150/1965d7c4-ae5d-46b9-8c5e-fae7466ec91e" alt="html5" width="20" height="20" style="vertical-align: middle;"/> Install requirements 

```bash
pip install -r requirements.txt
```

<img src="https://github.com/iamzehan/FastAPI-Beanie-MongoDB/assets/43857150/1965d7c4-ae5d-46b9-8c5e-fae7466ec91e" alt="html5" width="20" height="20" style="vertical-align: middle;"/> Run the project

```bash
python ./main.py
```
or 

```bash
python app/Home.py
```

<h2 align="center"> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://wiki.hornbill.com/images/7/70/Docker_logo.png" alt="linux" width="40" height="40" style="vertical-align: middle"/> </a> Docker </h2>

### <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://wiki.hornbill.com/images/7/70/Docker_logo.png" alt="linux" width="20" height="20" style="vertical-align: middle"/> </a> `build`

```bash
docker build -t school-lp-maker .
```

<h3 align="center">Technologies and Links</h3>

___

<p align="center"> 
<a href="https://streamlit.io/" title="FastAPI" target="_blank"><img src="https://styles.redditmedia.com/t5_7ispo3/styles/communityIcon_kxy2jy8mz8aa1.png" alt="html5" width="40" height="40"/></a> 
<img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" alt="html5" width="40" height="40"/> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://wiki.hornbill.com/images/7/70/Docker_logo.png" alt="linux" width="40" height="40"/> </a>
</p>
