# Poc.dev - Django Rest Framework API Proof of Concept
### Description:

This is a proof of concept project demonstrating the implementation of an API using Django Rest Framework. The project was developed as part of a test and includes additional features, such as the integration of tests to ensure code quality.

### Key Features:

Implementation of an API using Django Rest Framework
Inclusion of tests to ensure code reliability and robustness
Execution Instructions:

### 1 - Virtual Environment Setup:

```bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
````

### 2 - Dependencies Installation using Poetry:
```bash
Copy code
poetry install
```

### 3 - Running the Application:
```bash
Copy code
poetry run python manage.py runserver
```

### 4 - Running Tests:
```bash
Copy code
poetry run python manage.py test
Additional Notes:

```

### 5 - Endpoints:


```bash
# GET
http://localhost:8000/
```

```Json
[
    {
        "id": 1,
        "username": "igribeiro",
        "created_datetime": "2024-02-21 06:05:30.292900",
        "title": "Lorem",
        "content" "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    },
    ...
]
```


```bash
# POST
http://localhost:8000/
```

```Json

    {
        "username": "igribeiro",
        "title": "Lorem",
        "content" "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    }
```


```bash
# PATCH
http://localhost:8000/${pk}
```

```Json
    {
        "title": "Lorem Ipsum",
        "content" "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been."
    }
```


```bash
# DELETE
http://localhost:8000/${pk}
```

```Json
    {}
```




Ensure the virtual environment is set up before installing dependencies.
Tests can be executed to verify that the API is functioning as expected.


# It would be a pleasure to work with you CodeLeap.
