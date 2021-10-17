# users_api
toy program built to use cosine similarity between users and an api built to utilize it


### The goal of this is 

- to build a model that creates a similarity score between users
- to build a RESTful API that can be called using curl or PyCurl
- to build a storage of the transformed dataset in DynamoDB
- to build a model endpoint that will return the most similar users when a user_handle is entered

### Strategy

- I would like to make each course_id its own column
 - Creating a User-Score Matrix
- and then the users' assessment of each course be the data in that column (as a sparse matrix)
- and use that to run a cosine similarity between all users

### Obstacles
- There are not consistent tags offered to connect the actual course_id's to the courses that the students are offering assessment scores of
- Challenge of aggregating data without overrunning the memory of the instance or machine

### Helpful
- The views table has the course_id field, allowing us to know 
    - exactly how long each user viewed a course, and 
    - how often they viewed a course, and 
    - who the author was for that course

### Ideas
- I could also vectorize the interest tags in my User-Score Matrix
- This would give an additional dynamic where
    - Users that showed an interest in x, y, and z vectors (binary) 
    - then scored course n and m with score a and score b
    - Thus creating a user vector that can be measured against the other user vecotrs


![image](https://user-images.githubusercontent.com/28716728/137602995-7f8f9a2f-54e8-4bd6-b6f8-15514cbc37d3.png)

