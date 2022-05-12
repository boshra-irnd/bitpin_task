# bitpin_task


This project is done with Django rest framework.

<img src="https://miro.medium.com/max/700/1*kR89JbQQK9aAkNVyxE63pg.png" width="400" height="250" />

> Django REST framework is an open source, flexible and fully-featured library  with modular and customizable architecture that aims at building sophisticated  web APIs and uses Python and Django.

In this project, the user can view the list of articles and rate them from 1 to 5, also the user can see what rating he gave to the article and how many users rated the article and see the average score of the article.

### URLs on localhost:

List of articles
```
http://127.0.0.1:8000/
```
to give score
```
http://127.0.0.1:8000/article_id/score
```

Signup with email using JWT
```
http://127.0.0.1:8000/auth/users/
```
Signin using JWT
```
http://127.0.0.1:8000/auth/jwt/create/
```
Note: You must use the modheader extension
