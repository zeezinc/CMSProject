# CMS
 A Content Management System built using Python and Django by Zeeshan
 
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/zeezinc/CMSProject.git
$ cd CMSProject
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Custom Settings needed in Settings.py:

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = 'home'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

To sync database with the project apply migrations,0020 being the latest:

```sh
(env)$ python manage.py migrate
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/CMSProject/`

In case you want to create admin,run:

```sh
(env)$ python manage.py createsuperuser
```

For Coverage Report:

```sh
(env)$ coverage run --include='./*' manage.py test
```

```sh
(env)$ coverage report
```

For Branch Coverage:

```sh
(env)$ coverage run --include='./*' --branch manage.py test
```
```sh
(env)$ coverage report
```

For Inspecting Coverage:

```sh
(env)$ coverage html
```

```sh
(env)$ http://localhost:63349/AjackusProject/Website/htmlcov/index.html
```

        
<ul>Functionalities:

<li>The system will have 2 types of user role: admin and author.Admin users are created using seeding</li>
<li>Author can register and login using email to the CMS</li>
<li>Admin can view, edit and delete all the contents created by multiple authors</li>
<li>Author can create, view, edit and delete contents created by him</li>
<li>Users can search content by matching terms in title, body, summary and categories</li>

</ul>

<ol>Implementation:
 
<li>Technology - Python</li>
<li>Framework - Django Rest Framework</li>
<li>Authentication - Token/Email based</li>
<li>Applied field level validations</li>
<li>Used Basic TDD</li>

</ol>








 
Some Screenshots:
 
1.Home:![home](https://user-images.githubusercontent.com/35701613/111861196-6f35b580-8972-11eb-9adc-0eedece3244d.png)

2.Login:![login](https://user-images.githubusercontent.com/35701613/111859866-f6326000-8969-11eb-8d29-04c2632ba4d7.png)

3.Register:![register](https://user-images.githubusercontent.com/35701613/111859872-fd596e00-8969-11eb-9b6a-c0782e54dca9.png)

4.Admin:![admin](https://user-images.githubusercontent.com/35701613/111859877-0d714d80-896a-11eb-9624-59fb825bf13c.png)

5.Show Contents/Delete Content![add item](https://user-images.githubusercontent.com/35701613/111859899-27ab2b80-896a-11eb-8328-d2d5b7d65597.png)

6.Add Content:![list](https://user-images.githubusercontent.com/35701613/111859887-17934c00-896a-11eb-8988-196602a77dcb.png)

7.Update Content![update item](https://user-images.githubusercontent.com/35701613/111859905-342f8400-896a-11eb-8d61-2ccc629fcce8.png)

8.Upload File:![upload](https://user-images.githubusercontent.com/35701613/111859921-43aecd00-896a-11eb-8fc2-8af13f90db6f.png)

9.Search Query Return:![search](https://user-images.githubusercontent.com/35701613/111859940-5c1ee780-896a-11eb-9d5c-a9d2c3702664.png)

10.Search Details:![search2](https://user-images.githubusercontent.com/35701613/111859950-6c36c700-896a-11eb-9cff-46e98ccbcde3.png)

11.Coverage Report:![coverage_report](https://user-images.githubusercontent.com/35701613/113508997-dc4f6a80-9570-11eb-98a0-2a88c169bbdf.png)

12.Coverage Branch Report:![coverage_report_branch](https://user-images.githubusercontent.com/35701613/113509007-e6716900-9570-11eb-8a7c-b59c277545ea.png)

13.Coverage HTML Report:![coverage_report_html](https://user-images.githubusercontent.com/35701613/113509028-0012b080-9571-11eb-96e4-865fba1e5f0c.png)
