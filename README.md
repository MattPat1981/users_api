# users_api
toy program built to use cosine similarity between users and an api built to utilize it

### TO SEE THE DATA SCIENCE MODEL WORKING
Please run the MimmicAPILambda.ipynb from the sandbox branch

The API is not currently working as I need to add Lambda Layers to utilize Pandas in my Lambda Function for the last mile.

Once completed, you can access the API by following this link and changing the final number to the desired user_handle:
<a href='https://pok2uapqb2.execute-api.us-west-2.amazonaws.com/users_api_dev/myresource?user_handle=42'>https://pok2uapqb2.execute-api.us-west-2.amazonaws.com/users_api_dev/myresource?user_handle=42</a>

### Application Architecture:
<a href='https://app.cloudcraft.co/view/5fec4251-afee-4f94-b9b6-835acc6b00a0?key=b8beb4cc-f08e-4471-b5ab-cb2780483daa'>3D Rendering of this architecture</a>
![image](https://user-images.githubusercontent.com/28716728/137602995-7f8f9a2f-54e8-4bd6-b6f8-15514cbc37d3.png)

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
- Challenge of aggregating data without overrunning the memory of the instance or machine was overcome by using pivot tables

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
- Watch-Time or number of views might be interesting for a future model but might not be as relevant to an MVP
- How complex can I get and still have useful cosine similarity scores?

### If Time Permits
- I'd like to compare how the Jaccard Score performs using scikit-learn versus the cosine similarity score
- I'd like to figure out how using NLP might let me 
    - Impute probable assessments based on view times
    - Impute probable assessments based on interest tags
    - use the user_assessment_score as the metric by which to compute user similarities
- I'd like to investigate using Reinforcement Learning methods such as an Actor-Critic routine as is demonstrated in this 2020 paper, <a href='https://arxiv.org/pdf/1906.04281v2.pdf'>RACT: Towards Amortized Ranking-Critical Training for Collaborative Filtering, ICLR 2020</a> 



