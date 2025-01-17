---
layout: page
title: FastAPI Guide
permalink: /guides/fastapi
exclude_from_header: true
---

### Designing your API
---
<div id="good-ref-archs" class="flash">
  {% octicon bookmark %} 
  <strong><a class="nostyle" href="#good-ref-archs">What are some good reference architectures?</a></strong>
</div>
See: \
[Using FastAPI to Build Python Web APIs](https://realpython.com/fastapi-python-web-apis/) \
[Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql) \
[Up and running with fastapi series](https://www.jeffastor.com/blog/refactoring-our-react-ui-into-composable-hooks-part-ii)

<div id="user-reg-auth" class="flash">
  {% octicon bookmark %} 
  <strong><a class="nostyle" href="#user-reg-auth">How do I do user registration/login, e-mail verification, password resets, etc... with fastapi?</a></strong>
</div>
See: \
[Handle Registration in FastAPI and Tortoise ORM](https://levelup.gitconnected.com/handle-registration-in-fastapi-and-tortoise-orm-a661162d27f1) \
[Handling Email Confirmation During Registration in Flask](https://realpython.com/handling-email-confirmation-in-flask/#models) \
[Flask Rest API -Part:5- Password Reset](https://dev.to/paurakhsharma/flask-rest-api-part-5-password-reset-2f2e) \
[E-commerce API with FastAPI | Sending Verification Emails | FastAPI-Mail](https://www.youtube.com/watch?v=gdKBn5cp3TM)

<div id="star-in-method" class="flash">
  {% octicon bookmark %} 
  <strong><a class="nostyle" href="#star-in-method">What does a star(*) mean in a method parameter?</a></strong>
</div>
It simply allows you to order your arguments so those without default values can be placed ahead of those that can.  It also ensures that 
keyword arguments are used everywhere (which may or may not be desirable when refactoring code).  I usually find it unnecessary except in places where I'm using 
`BackgroundTasks` or a depency injected argument somewhere, for example:

```python
@app.get("/")
def get_username(*, db: Session = Depends(get_db), user_id: int) -> str:
    return db.query(User).get(user_id).username
```
See: \
[What does a star(*) mean in a method parameter?](https://github.com/tiangolo/fastapi/issues/817#issuecomment-569799896) \
[Order the parameters as you need, tricks](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#order-the-parameters-as-you-need-tricks)


### Working with Pydantic objects
---
<div id="pydantic-cast" class="flash" style="margin-bottom:5px;">
  {% octicon bookmark %} 
  <strong><a class="nostyle" href="#pydantic-cast">How to cast one pydantic object into another?</a></strong>
</div>

```python
MyModel(**my_model_from.dict())
```


### Dockerizing a FastAPI application
- - -
<div id="how-to-dockerize" class="flash">
  {% octicon bookmark %} 
  <strong><a class="nostyle" href="#how-to-dockerize">How can I Dockerize my app?</a></strong>
</div>
See: \
[How to Dockerize a Python App with FastAPI](https://www.docker.com/blog/video-how-to-dockerize-a-python-app-with-fastapi/) \
[An Extremely Simple Docker, Traefik, and Python FastAPI Example](https://kleiber.me/blog/2021/03/23/simple-docker-traefik-python-fastapi-example/)


### Dealing with common errors
- - -
<div id="error-unprocessable-entity-422" class="flash flash-error">
  {% octicon bookmark %} 
  <strong><a class="nostyle" href="#error-unprocessable-entity-422">I get an Unprocessable Entity (422) error when I post/put to my API</a></strong>
</div>
It usually means the body of your request doesn't mesh with what your API method is expected.  Make sure that the object your passing in matches what you've
specified, including using the `Body(...[,embed=True])` types correctly

See: \
[Body - Multiple Parameters](https://fastapi.tiangolo.com/tutorial/body-multiple-params/?h=embed) \
[Python: FastApi (Unprocessable Entity) error](https://stackoverflow.com/questions/62384392/python-fastapi-unprocessable-entity-error)

<div id="error-coroutine-has-no-attribute" class="flash flash-error">
  {% octicon bookmark %} 
  <strong><a class="nostyle" href="#error-coroutine-has-no-attribute">AttributeError: 'coroutine' object has no attribute 'X'</a></strong>
</div>
Usually means you are missing “await” from async method (fastapi/python)

<div id="error-postgresql-returning-nada" class="flash flash-error">
  {% octicon bookmark %} 
  <strong><a class="nostyle" href="#error-postgresql-returning-nada">I'm using [Encode Databases](https://github.com/encode/databases) against a postgres database, but my `RETURNING` statements don't return all the columns I specify</a></strong>
</div>
`RETURNING` statements work okay with `fetch_one`/`fetch_all`.  If you are using `execute`, it won't work \
See: [Support for RETURNING](https://github.com/encode/databases/issues/98#issuecomment-499875112) 

<div id="error-nginx-reverse-proxy-https" class="flash flash-error" style="margin-bottom:5px;">
  {% octicon bookmark %} 
  <strong><a class="nostyle" href="#error-nginx-reverse-proxy-https">When I deploy using Nginx reverse-proxy, I get mixed content errors like the one below...</a></strong>
</div>
```
Mixed Content: The page at 'https://page.com' was loaded over HTTPS, but requested an insecure 
XMLHttpRequest endpoint 'http://page.com?filter=xxxx'. 
This request has been blocked; the content must be served over HTTPS.
```
If you add a trailing slash (/) in your API requests it will fix the problem ***BUT*** a much easier solution is to 
the correct proxy headers for Uvicorn.  They should look something like this:
```
upstream api_server {
    server ${API_HOST}:${API_PORT} fail_timeout=0;
  }
...
server {
  ...
  location ~ /api/ {
    proxy_set_header   Host $host;
    proxy_set_header   X-Real-IP $remote_addr;
    proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header   X-Forwarded-Host $server_name;
    proxy_pass http://api_server;
  }
```
See the following resources: \
[Failure to load any static files when deploying with HTTPS](https://github.com/tiangolo/fastapi/issues/2611#issuecomment-755436758) \
[fastapi-react nginx.conf](https://github.com/vikramgulia/fastapi-react/blob/master/ui/nginx/nginx.conf) \
[Add option for adding a trailing slash automatically](https://github.com/axios/axios/issues/757) \
[Ajax Product Filter does not work in https - Fixed](https://support.yithemes.com/hc/en-us/articles/115002851847-Ajax-Product-Filter-does-not-work-in-https-Fixed) 

- - -