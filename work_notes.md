to test and probe the API for the first time open up the a repl in the CLI

anytime you change your DOT ENV you need to exit and reopen the pipenv shell

if the Linter is throwing red squiggles underneath your import statements, then it might not be installed in the virtual environment, so in the CLI type:
pipenv install pylint --dev
then press enter

in this project, the definition of model is going to be different. We're using the web development definition meaning that model refers to the layout of the data; like a schema.

for build week challenge:
get data
make flask routes
deploy to heroku
know how the ETL pipeline
    works for SQL in relation
    to frontend and backend

for the build week challenge GitHub repo:
get admin access and then make a branch
    not a fork



CREATING THE DS MODEL:
to work out the variables for the LogisticRegression model, it's handy to work it out in flask shell and even run the regression model in there too. from there you can transcribe into the code editor



WHAT I GOT IN THE CLI
after trying the logistic regression
--SOLVED
I changed:
 log_reg = LogisticRegression().fit(embeddings, labels)
to:
 log_reg = LogisticRegression(max_iter=800).fit(embeddings, labels)
```
>>> user2_embeddings = np.array([tweet.embedding for tweet in user2.tweets])
>>> user2_embeddings.shape
(26, 768)
>>> embeddings = np.vstack([user1_embeddings, user2_embeddings])
>>> labels = np.concatenate([np.ones(len(user1.tweets)), np.zeros(len(user2.tweets))])
>>> labels
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0.])
>>> len(labels)
73
>>> log_reg = LogisticRegression().fit(embeddings, labels)
c:\users\sean\.virtualenvs\twitoff-2enivfuo\lib\site-packages\sklearn\linear_model\_logistic.py:764: ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Increase the number of iterations (max_iter) or scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
  extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
```