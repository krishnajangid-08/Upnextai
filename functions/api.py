from app import app as application
import serverless_wsgi

# Handle the Lambda event
def handler(event, context):
    return serverless_wsgi.handle_request(application, event, context)
