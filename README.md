# DJANGO REPORT APPLICATION
![pypi](https://img.shields.io/pypi/v/ahlev-django-report) ![pypi](https://img.shields.io/pypi/status/ahlev-django-report)

This django application is used to create report.

## prerequisites
The instructions below assume that you have a django project already set up; and a python virtual environment already installed and activated. 

## styles
All ahlev-django applications are using styles from [mdbootstrap.com](https://mdbootstrap.com), so please make sure you install [ahlev-django-css-js](https://github.com/ohahlevahlev-django-css-js.git) first.

## install from this repository
### clone
```
git clone https://github.com/ohahlev/ahlev-django-report.git
```

### go to directory ahlev-django-report
```
cd ahlev-django-report
```

### create installer package
```
python3 setup.py sdist
```

### go to project directory
```
pip install dist/ahlev-django-report-0.0.1.tar.gz
```

## install from pypi
[ahlev-django-report](https://pypi.org/project/ahlev-django-report/)

## project configuration
### update settings.py as the following
```
INSTALLED_APPS = [
    'report', # add this line
    ...
]
```

### add these lines to the end of settings.py if they don't exist yet
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/medias/'
```

## screenshots
### backend: report management
![](screenshot/report_backend1.png)

### backend: list all report type
![](screenshot/report_backend2.png)

### backend: edit a report
![](screenshot/report_backend3.png)
