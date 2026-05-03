# Madagascar Project

Build DJANGO application based on Architectural Pattern to organize CRUD and SSR client to Deploy on VPS!

## Introduction & Learning Path

1. Build Virtual Environments: Madagascar[pipenv] & Barokai[conda]
2. Django WebServer Framework
3. What is Database: RDBS vs NoSQL
4. Setup and Migrate SQL database
5. System Design & Patterns
6. Create Madagascar project apps
7. Develop Portfolio\*
8. Organize Frontend standard
9. Integrate project frontend source
10. What is CRUD, Create and Read plans
11. Delete and Update plans
12. What is Kernel & Shell language
13. Deploy project on VPS/VPC

## Project run source

- Install pipenv & create Virtual environment

  ```
  pip install pipenv
  pipenv install --python 3.11
  ```

- Install packages:

  ```
  pipenv install
  pipenv install django==4.2
  ```

- Migrate Database

  ```
  ./manage.py migrate
  ./manage.py showmigrations
  ```

  ```
  ./manage.py dbshell

  CREATE TABLE plan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
  );
  ```

- Run project via activated virtual environment:

  ```
  pipenv shell
  ./manage.py runserver
  ```
