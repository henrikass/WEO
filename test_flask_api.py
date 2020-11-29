
from flask_api import app
from flask import json

def test_api():        
    response = app.test_client().get(
        '/weo',
        data=json.dumps({'Total investment' : 123333,
        'General government revenue' : 345,
       'General government total expenditure' : 2342.43,
       'General government primary net lending/borrowing' : 3.43,
       'General government gross debt': 2342.34}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    
