Create working directory and move there:

`mkdir testapp`

`cd testapp`

In this directory create a virtual environment by:

`virtualenv venv`

Activate the virtual environment (Windows):

`venv\Scripts\activate`

Clone this repository in the directory:

`git clone https://github.com/rannuste/online_store.git`

`cd online_store`

Install all the required dependecies:

`pip install -r requirements.txt`

Run the application:

`python app.py`

Curl commands for testing (I used Advanced REST client for testing)
1. to create a product:
`curl -X POST https://localhost:5000/add -H 'Content-Type: application/json' -d '{"name":"phone","description":"finnish", "attributes": {"key1": "value1", "key2": "value2"}}'`

2. to find it by parameter:
`curl https://localhost:5000/products/attributes/key1/value1`

3. to get details of the found product:
`curl http://localhost:5000/product/6130b514931775f31ddf5ba3`
