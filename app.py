
from chalice import Chalice

app = Chalice(app_name='serverlessemail')


@app.route('/')
def index():
    return {'hello': 'Welcome to Nkejen'}

@app.route('/sendemail', methods=['POST'])
def sendemail(_from, _to, _message):
    i = app.current_request.json_body
    instancename = i['instancename'] if "instancename" in i else None
    instanceid = i['instanceid'] if "instanceid" in i else None
    description = i['description'] if "description" in i else None
    return {'hello': 'Welcome to Nkejen'}
