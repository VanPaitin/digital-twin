from mangum import Mangum
from server import app

# Create the Lambda handler using Mangum
handler = Mangum(app)
