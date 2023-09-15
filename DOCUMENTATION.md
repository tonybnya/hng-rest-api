# API Documentation

## Overview

This API provides basic CRUD (Create, Read, Update, Delete) operations for managing person records. Users are identified by their names, and the API ensures that the name field only accepts string values.

## Standard Request and Response Formats

All requests should be made with the `Content-Type` header set to `application/json`. All responses will also be in JSON format.

## Endpoints

### Create Person

- **URL**: `/api`
- **Method**: `POST`
- **Request**:
  
  ```json
  {
    "name": "Mark Essien"
  }
  ```
  
  **Response (Success)**:
- **Status Code**: 201
  
  ```json
  {
   'message': 'Person created successfully'
  }
  ```
  
  **Response (Error)**:
- **Status Code**: 500
  
  ```json
  {
   "message": "Error creating person"
  }
  ```

### Read Person

- **URL**: `/api/<id>`
- **Method**: `GET`
  **Response (Success)**:
- **Status Code**: 200
  
  ```json
  {
   "id": 1,
   "name": "Mark Essien"
  }
  ```
  
  **Response (Error)**:
- **Status Code**: 500
  
  ```json
  {
   "message": "Error getting person"
  }
  ```

### Update Person

- **URL**: `/api/<id>`
- **Method**: `PUT`
  **Response (Success)**:
- **Status Code**: 200
  
  ```json
  {
   'message': 'Person updated successfully'
  }
  ```
  
  **Response (Error)**:
- **Status Code**: 500
  
  ```json
  {
   "message": "Error updating person"
  }
  ```

### Delete Person

- **URL**: `/api/<id>`
- **Method**: `DELETE`
  **Response (Success)**:
- **Status Code**: 204
  
  ```json
  {
   'message': 'Person deleted successfully'
  }
  ```
  
  **Response (Error)**:
- **Status Code**: 500
  
  ```json
  {
   "message": "Error deleting person"
  }
  ```
  
  # Sample Usage
  
  Here’s an example of how to use the API with curl:

## Create a new person

```
curl -X POST -H "Content-Type: application/json" -d '{"name": "Mark Essien"}' http://localhost:5000/api
```

## Read a person's details

```
curl http://localhost:5000/api/1
```

## Update a person's details

```
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Mark Essien"}' http://localhost:5000/api/1
```

## Delete a person

```
curl -X DELETE http://localhost:5000/api/1
```

## Get all persons

```
curl http://localhost:5000/api
```

# Limitations and Assumptions

- The API does not handle authentication or authorization. 
- The API does not handle pagination. 
- The API does not handle the length of the name field. 
