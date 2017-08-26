 
#  REST Image Management

Rest based APIs to server image management for any platform.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## For Demo click [here](https://radiant-tundra-99837.herokuapp.com/images/):

Username: test

Password: test@123

### Functionality:
     1. Get list all images
     
     2. Upload image
     
     3. Update existing image
     
     4. Delete image
     
     5. Token / Basic Authentication

### Prerequisites

What things you need to install the software and how to install them

```
Python 3, Git
```

### Installing

Create virtual environment for the python project setup.

```
virtualenv -p python3 envname
```

And repeat

```
cd envname
source bin/activate
git clone https://github.com/KishanAjudiya/do_select_image_management.git
cd do_select_image_management
```

Now you have to download the requirements for the project.

```
pip install -r requirement.txt
```

After all the requirements has been installed. Run migrations

```
python manage.py migrate
```
For accessing the APIs you have to create superuser. You can create it with following command.
```
python manage.py createsuperuser
```

For running the Project:

```
python manage.py runserver 0.0.0.0:8000
```

Now you can access it form here

[http://localhost:8000/images/](http://localhost:8000/images/)

### For accessing Admin panel
[http://localhost:8000/admin/](http://localhost:8000/admin/)


## Acknowledgments

Thanks.