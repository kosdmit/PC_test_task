## Note
This is a documentation for API which was developed for job test task

## Getting Started

If you're interested just in test this, you can work with online server: <a href="http://kosdmitsmr.pythonanywhere.com</a>

Below is instruction on setting up this project locally.
To get a local copy up and running follow these simple steps.

### Prerequisites
_Let's check if we are ready._

* This project uses Python 3.11. Check your python version:
  ```sh
  python --version
  ```
  *work on earlier versions is not guaranteed*

### Installation

_Let`s start._

1. Clone the repo
   ```sh
   git clone https://github.com/kosdmit/PC_test_task.git
   ```
2. Create and activate a virtual environment
   ```sh
   cd yourrepository
   virtualenv venv
   source venv/bin/activate
   ```
   If you are on Unix or MacOS, run this for activate virtual environment:  
   ```sh
   source venv\Scripts\activate
   ```

3. Install required Python packages
   ```sh
   pip install -r requirements.txt
   ```
   
4. Create and apply migrations
   ```sh
   python mange.py makemigrations
   python manage.py migrate
   ```
   
5. That`s it! Run the Django server and use how you want!
   ```sh
   python manage.py runserver
   ```

# API Documentation

## Overview

The API provides an interface for managing and querying CSV data files. It supports essential CRUD operations on data files and offers advanced filtering and sorting capabilities on the data within the files. The API also integrates token-based authentication to ensure secure access.

## Base URL
All API endpoints are based on:

```sh
{{base_url}}/api/
```

Replace `{{base_url}}` with the actual server domain or IP address and port.

## Authentication
The API uses token-based authentication. Clients must first obtain a token and then include it in the header of subsequent requests.

### Get Auth Token

**URL:** `{{base_url}}/api/api-token-auth/`

**Method:** `POST`

**Headers:** `None`

**Body:**
```sh
username (string): User's username
password (string): User's password
```

**Example:**

```sh
{
    "username": "admin",
    "password": "password123"
}
```

Once you have the token, include it in the header of subsequent requests:

```sh
Authorization: Token your_token_key_here
```

## Endpoints

### 1. List Data Files
**URL:** `{{base_url}}/api/files/`

**Method:** `GET`

**Headers:** `Authorization: Token your_token_key_here`


### 2. Upload Data File
**URL:** `{{base_url}}/api/files/`

**Method:** `POST`

**Headers:** `Authorization: Token your_token_key_here`

**Body (formdata):**
`file: The CSV file to upload`

### 3. Retrieve Data File Detail
**URL:** `{{base_url}}/api/files/{{pk}}/`

**Method:** `GET`

**Headers:** `Authorization: Token your_token_key_here`

Replace `{{pk}}` with the actual primary key of the DataFile instance.

### 4. Delete Data File
**URL:** `{{base_url}}/api/files/{{pk}}/`

**Method:** `DELETE`

**Headers:** `Authorization: Token your_token_key_here`

Replace `{{pk}}` with the actual primary key of the DataFile instance.

### 5. Get Data from a Data File
**URL:** `{{base_url}}/api/files/{{pk}}/get_data/`

**Method:** `GET`

**Headers:** `Authorization: Token your_token_key_here`

Replace `{{pk}}` with the actual primary key of the DataFile instance.

#### Optional Query Parameters:
`filter_by (string)`: Column name by which to filter the data.

`filter_value (string)`: Value to use for filtering the specified column.

`sort_by (string)`: Column name by which to sort the data.

For example, to filter data by the "COUNTRY" column with a value of "Avon", and then sort the results by "UUID", you would use:
```sh
{{base_url}}/api/files/{{pk}}/get_data/?filter_by=COUNTRY&filter_value=Avon&sort_by=UUID
```


## Thank you for attention!