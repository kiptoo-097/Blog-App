# BLOG APP

## Author

[Kiptoo Kennedy](https://github.com/kiptoo-o97)

# Description

This is an application that allows users to sign in or sign up and post blogs abroad.It also allows them to comment on the blogs they have created

## User Story

- Comment on the different blogs posted by other users.
- See the blogs posted by other uses.
- See the random quotes on the landing page
- Register to be allowed to log in to the application
- View blogs from the different categories.
- Submit a pitch to a specific category of their choice.

## BDD

| Behaviour             |                Input                |                                                                       Output |
| :-------------------- | :---------------------------------: | ---------------------------------------------------------------------------: |
| Load the page         |          **On page load**           |                               Get all posts, Select between signup and login |
| Select SignUp         | **Email**,**Username**,**Password** |                                                            Redirect to login |
| Select Login          |    **Username** and **password**    | Redirect to page with app blogs based on  commenting section |
| Select comment button |             **Comment**             |                                             Form that you input your comment |
| Click on submit       |                                     |       Redirect to all comments tamplate with your comment and other comments |

## Development Installation

To get the code..

1. Cloning the repository:

```bash
https://github.com/kiptoo-097/Blog-App
```

2. Move to the folder and install requirements

```bash
cd blog-post
pip install -r requirements.txt
```

3. Exporting Configurations

```bash
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
```

4. Running the application

```bash
python3.6 app.py server
```

Open the application on your browser `127.0.0.1:5000`.

## Technology used

- [Python3.8](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [Heroku](https://heroku.com)

## Contact Information

kiptoo097@gmail.com

## Live Link To Project






## License
 
 Licensed under[MIT license](LICENSE.md)