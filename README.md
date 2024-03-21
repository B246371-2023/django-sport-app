# Django Login & Register
This a Django project that allows users to login to your website and allows them to register for an account as well! The HTML templates use the [Bootstrap login template](https://getbootstrap.com/docs/4.0/examples/sign-in/) and the user data is stored in a JSON file. You can use this in your website!

## Prerequisites:
* [Python](https://www.python.org/) Installed (I used 3.8.9)
* [Django](https://www.djangoproject.com/) installed. (I used 3.1.2)
* MySQL version higher than 8.0.0
* pandas
* numpy

* A Terminal.

You can install Django with:
```bash
pip install Django==3.1.2
```

2024-3-21

- Successfully built the MySQL connection.

- Added file /app/management/commands/test_data_generate.py

  - Used for generating datasets required for testing. If more tests need to be generated, parameters can be manually modified.

- Added file /app/management/commands/import_csv_to_mysql.py

  - Used to import the generated data into the created MySQL database.

- Added file /migration/services.py

  - Core analysis code of the program, containing analysis of performance data in the database (this function will analyze the heart rate, speed, and shot accuracy of a specific player's last three matches) and provide training suggestions (completed), as well as analysis of health characteristic data (analyzing the stress level and sleep quality of a specific player) and provide corresponding health status assessments (to be completed).

- Added file /templates/Performance_advice.html

  - Used to test whether the advice results output by the analysis code can be called and displayed on the web page. This page can be retained and directly used as a training page, only needing to add some frontend design structures.
  - Test  result：

  - ![image-20240321063225271](C:\Users\14391\AppData\Roaming\Typora\typora-user-images\image-20240321063225271.png)

- random_athlete_data_with_names --data extract

![image-20240321062418152](C:\Users\14391\AppData\Roaming\Typora\typora-user-images\image-20240321062418152.png)

## Running The Server On Localhost

In your Terminal / Command Prompt, type the following:

```bash
python manage.py runserver
```
You would see some logs now. Ignore them. All you have to do is visit [`localhost:8000`](http://localhost:8000) on your browser. To stop the server, return to your terminal and press `CTRL-C`.

## Logging In

Visit the [login page](http://localhost:8000/login/) and try to login! The preloaded user's email is `person1@org.com` and the password is `placeholder`. You can view this in [user_data.json](https://github.com/vismodo/django-login-and-register/blob/master/user_data.json). If you enter incorrect details, you will see a [Bootstrap Alert](https://getbootstrap.com/docs/4.0/components/alerts/). To register with an account, visit the [registration page](http://localhost:8000/register).



## The JSON File

The [JSON File](https://github.com/vismodo/django-login-and-register/blob/master/user_data.json) contains all the emails and passwords of users. Without this file, The project will have no function at all! You may read, remove items and add them from anywhere, but there must be atleast one email and password.

## Next Steps


