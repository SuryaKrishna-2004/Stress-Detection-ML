from flask import *
from database import *

api=Blueprint('api',__name__)

@api.route('/login/',methods=['get','post'])
def login():
	data={}
	username=request.args['username']
	password=request.args['password']
	q="select * from login where  username='%s' and password='%s'" %(username,password)
	res=select(q)
	print("''''''''",res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return  str(data)


@api.route('/hviewprofile/',methods=['get','post'])
def hviewprofile():
	print("///////////////////////////////")
	data={}
	uname=request.args['username']
	print("unameeeeeeeeeee",uname)
	q="select * from health_care_team where username ='%s'" %(uname)
	res=select(q)
	print("/////////////",q)
 

	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewprofile"
	return  str(data)



@api.route('/viewappointment/',methods=['get','post'])
def viewappointment():
	print("///////////////////////////////")
	data={}
	uname=request.args['username']
	print("unameeeeeeeeeee",uname)
	q="select * from appointment inner join staff using (staff_id) where health_id=(select health_id from health_care_team where username='%s') order by appointment_id" % (uname)
	print(q)
	res=select(q)

	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewappoinment"
	return  str(data)



@api.route('/confirmappointment/',methods=['get','post'])
def confirmappointment():
	print("///////////////////////////////")

	ap_id=request.args['appid']
	q1 = 'update appointment set status="Confirmed" where appointment_id="%s"' % (ap_id)
	update(q1)
 
 
@api.route("/addmeddetails")
def addmeddetails():
	data={}
	titles=request.args['title']
	description=request.args['desc']
	appointmentid=request.args['apid']
	print(appointmentid)
	

	qry = "insert into medication values('%s','%s','%s',null) " % (appointmentid, titles, description)
	insert(qry)
	print(qry)
	q1 = 'update appointment set status="Prescribed" where appointment_id="%s"' % (appointmentid)
	update(q1)
	print(q1)
	
	data['status']='success'

	return str(data)



@api.route("/viewprofile")
def viewprofile():
    username=request.args['username']
    data={}
    qry="select * from health_care_team where username='%s'"%(username)
    res=select(qry)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='profile'
    return str(data)


@api.route("/health_update")
def health_update():
    data={}
    fname=request.args['fname']
    lname=request.args['lname']
    phone=request.args['phone']
    email=request.args['email']
    quali=request.args['quali']
    username=request.args['username']
    dob=request.args['dob']
    
    qry="update health_care_team set h_fname='%s',h_lname='%s',h_qualification='%s',h_email_id='%s',h_phone_no='%s',h_dob='%s' where username='%s'"%(fname,lname,quali,email,phone,dob,username)
    res=update(qry)
    if res:
        data['status']='success'
    else:
        data['status']='failed'
    data['method']='update'
    return str(data)



