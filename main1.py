from flask import *
from database import *
app = Flask(__name__)

@app.route('/', methods=['get', 'post'])
def staff_view_graphh():
    data={}
    qry ="""
    SELECT 
    e.date,
    e.p_value,
    e.p_result,
    s.staff_id,
    s.first_name,
    s.last_name
    
FROM 
    predicted_result e
JOIN 
    staff s ON e.staff_id = s.staff_id
GROUP BY 
    e.date, s.staff_id, s.first_name, s.last_name;

    """
    data['em']=select(qry)
    print(data['em'])
    
    return render_template('graph.html',data=data)


if __name__ == '__main__':
   app.run(debug = True)