# What is an API? What is REST?
* API stands for Application Program Interface.
* Create a service that allows multiple applications to interact with the database, for example.
* Your applications only have to send data, and not worry about the database itself.
# Example API
* API is hosted on: www.mysite.com/api
* Your app is now going to interact with this API, requesting or sending data, and the API is going to the interaction with the database.
* One example of a request, you would ask the API to get something from the database, would be:
    * GET www.mysite.com/api/**user/15fg83bh100**
    * POST www.mysite.com/api/**users/new**
        * id: 188ghfaj87h
        * name: Jose
# What is REST?
* Simply a way to structure these APIs.
* Key feature of REST is "stateless": one API request does not affect the next.
* Another key feature is "resource-based": API structured on a per-resource basis(e.g. students, users, blog_posts), similar to objects in objects-oriented programming.