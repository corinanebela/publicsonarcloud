from flask import request, render_template_string

# /hello?username={{config}} will display the entire flask configuration and potential secrets
@app.route('/hello')
def hello():
    username = request.args.get('username')
    template = f"<p>Hello {username}</p>" # User input is used directly in the string to be rendered
    return render_template_string(template) # Noncompliant
  
  
# from flask import request, render_template_string

# @app.route('/hello')
# def hello():
#     username = request.args.get('username')
#     template = "<p>Hello {{ name }}</p>"
#     return render_template_string(template, name=username) # Compliant


from flask import request

@app.route("/")
def example():
    operation = request.args.get("operation")
    eval(f"product_{operation}()") # Noncompliant
    return "OK"
 

# from flask import request

# @app.route("/")
# def example():
#     allowed = ["add", "remove", "update"]
#     operation = allowed[request.args.get("operationId")]
#     eval(f"product_{operation}()")

#     return "OK"


@app.route('/login')
def login():
    dynamodb = AWS_SESSION.client('dynamodb')

    username = request.args["username"]
    password = request.args["password"]

    dynamodb.scan(
        FilterExpression= "username = " + username + " and password = " + password, # Noncompliant
        TableName="users",
        ProjectionExpression="username"
    )
    
# @app.route('/login')
# def login():
#     dynamodb = AWS_SESSION.client('dynamodb')

#     username = request.args["username"]
#     password = request.args["password"]

#     dynamodb.query(
#         KeyConditionExpression= "username = :u",
#         FilterExpression= "password = :p",
#         ExpressionAttributeValues={
#             ":u": { 'S': username },
#             ":p": { 'S': password }
#         },
#         TableName="users",
#         ProjectionExpression="username"
#     )
