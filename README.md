# LyonHacks II Web-Development Workshop
## A to-do list web app made with Flask and HTML/CSS

**See the complete web app at https://lyonhacks-workshop.jimmyliu.dev/**

Made by [Jimmy Liu](https://github.com/ji-mmyliu) and [Vlad Surdu](https://github.com/V1ad20)

To run the site on your local machine, clone the repository and enter the directory

```bash
git clone https://github.com/ji-mmyliu/lyonhacks-web-dev-workshop.git
cd lyonhacks-web-dev-workshop
```

Install all the Python package requirements using
```bash
python3 -m pip install -r requirements.txt
```

Initialize the SQLite database tables by running `python3`, then
```python3
>>> from flask_site import db
>>> from flask_site.models import *
>>> db.create_all()
```

Then run the app using
```bash
python3 run.py
```

You should then be able to access the web app on your browser at http://localhost:5000/.
