This handles only POST request

TODO : implement authentication and get user from the authentication

url : http://127.0.0.1:8000/primary/voteup/

body : 

{
    "user" : 1,
    "category" : 2,
    "category_name" : "Tollywood"
}

result : 

{
    "message": "Created/Updated the Object"
}

info : This creates if the user and the category is not present else updates the database