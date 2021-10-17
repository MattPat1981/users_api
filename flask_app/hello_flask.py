from flask import Flask

app = Flask(__name__)

#set sql engine to run 
#engine = somthing

#define sql alcemy class for 'similarily_cluster'
#class SimilarityCluster(base):
#    see sqlalchemy

#imagine a GET/PUT/POST url request as:
# http://myapp/similiarity_cluster?name=SOMEDUDE&range=50
#alternatively (maybe_more_RESTFUL)
# http://myapp/users/USERNAME/similarity_cluster?range=50

@app.route("/")
def hello_world():
    return "<p>You're in the right place!</p>"

@app.route("/similarity_score")
def return_similarity_cluster():
    #look up the paramaters argument for flask

    #create sql instance for simliarty_cluster
    #do you select with user name based on the parameter from you flask request
    #convert that to json
    #return that
    return "<p>Welcome to the Application</p>" 
