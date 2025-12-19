from flask import *
from database import *
import uuid 
from datetime import datetime

health = Blueprint('health', __name__)

# Health Home Page
@health.route('/health_home')
def health_home():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data={}
        qry="select * from health_care_team where health_id='%s'" %(session['hli'])
        res=select (qry)
        data['view']=res
        return render_template('health_home.html',data=data)

# Update and View Profile
@health.route('/health_view_profile', methods=['get', 'post'])
def health_view_profile():
    data = {}
    qry = "select * from health_care_team where health_id='%s'" % (session['hli'])
    res = select(qry)
    session['img']=res[0]['h_photo']
    data['view'] = res
    qry4="select * from p_address inner join c_address using (username) where username='%s'"%(session['lid'])
    res4=select(qry4)
    data['add']=res4
    
    if 'submit' in request.form:
        p_address_line_1=request.form['addressline1']
        c_address_line_1=request.form['caddressline1']
        p_address_line_2=request.form['addressline2']
        c_address_line_2=request.form['caddressline2']
        landmark=request.form['landmark']
        clandmark=request.form['clandmark']
        pincode=request.form['pincode']
        cpincode=request.form['cpincode']
        city=request.form['city']
        ccity=request.form['ccity']
        state=request.form['state']
        cstate=request.form['cstate']
        country=request.form['country']
        ccountry=request.form['ccountry']
        profile=request.files['file']
        resume=request.files['resume']
        certificate=request.files['credential']
        path1='static/assets/certiresume/'+str(uuid.uuid4())+certificate.filename
        certificate.save(path1)
        path2='static/assets/certiresume/'+str(uuid.uuid4())+resume.filename
        resume.save(path2)
        qry2 = "update p_address set address_line1='%s',address_line2='%s',landmark='%s',pincode='%s',city='%s',state='%s',country='%s' where username='%s'" % (p_address_line_1,p_address_line_2,landmark,pincode,city,state,country,session['lid'])  
        update(qry2)   
        qry3 = "update c_address set c_address_line1='%s',c_address_line2='%s',c_landmark='%s',c_pincode='%s',c_city='%s',c_state='%s',c_country='%s' where username='%s'" %(c_address_line_1,c_address_line_2,clandmark,cpincode,ccity,cstate,ccountry,session['lid']) 
        update(qry3)
        qry6 = "update health_care_team set h_resume='%s',h_credential='%s'  where health_id='%s'" % (path2,path1,session['hli'])
        update(qry6)

        # Profile picture
        if profile :
            path='static/assets/img/profile/'+str(uuid.uuid4())+profile.filename
            profile.save(path)
            qry5 = "update health_care_team set  h_photo='%s' where health_id='%s'" % (path,session['hli'])
            update(qry5)
        else:
            qry5 = "update health_care_team set  h_photo='%s' where health_id='%s'" % (session['img'],session['hli'])
            update(qry5)
        return '''<script>alert("Profile Updated Successfully");window.location='/health_view_profile'</script>'''
    return render_template('health_view_profile.html', data=data)

# Change Password
@health.route('/health_change_password', methods=['get', 'post'])
def health_change_password():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data = {}
        if 'submit' in request.form:
            old_pass = request.form['old_password']
            new_pass = request.form['new_password']
            con_pass = request.form['con_password']
            q = "select * from login where password='%s' and username='%s'" % (
                old_pass, session['lid'])
            res = select(q)
            if res:
                if new_pass == con_pass:
                    q = "update login set password='%s' where username='%s'" % (
                        new_pass, session['lid'])
                    update(q)
                    return '''<script>alert("Password Updated Successfully!!");window.location='/health_change_password'</script>'''
                else:
                    return '''<script>alert("Password doesnot Match!!");window.location='/health_change_password'</script>'''
            else:
                return '''<script>alert("Incorrect password!!");window.location='/health_change_password'</script>'''
        return render_template('health_change_password.html', data=data)

# Notification
@health.route('/health_send_notification', methods=['get', 'post'])
def health_send_notification():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data = {}
        if 'submit' in request.form:
            des = request.form['notification']
            now = datetime.now()
            date = now.strftime('%d-%m-%Y')
            qry1 = "insert into notification(notification_des,date,user_type) values ('%s','%s','health')" % (des,date)
            res = insert(qry1)
            return '''<script>alert("Notification Send Successfully");window.location='/health_send_notification'</script>'''
        qry = "select * from notification"
        res = select(qry)
        data['view'] = res
        
        if 'action' in request.args:
            action = request.args['action']
            id = request.args['id']
        else:
            action = None
        
        if action == 'delete':
            q = "delete from notification where notification_des='%s'" % (id)
            delete(q)
            return '''<script>alert("Notification Deleted Successfully");window.location='/health_send_notification'</script>'''
        return render_template('health_send_notification.html', data=data)


# Appointment
@health.route('/health_view_appointment', methods=['get', 'post'])
def health_view_appointment():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data = {}
        q1 = 'select * from appointment inner join staff using (staff_id) where health_id="%s" order by appointment_id' % (session['hli'])
        print('dddddddddddddddddddddd',q1)
        res = select(q1)
        print(res)
        data['view'] = res
        
        
        if 'action' in request.args:
            action = request.args['action']
            id = request.args['id']
        else:
            action = None
        
        if action == 'confirm':
            q1 = 'update appointment set status="Confirmed" where appointment_id="%s"' % (id)
            update(q1)
            return '''<script>alert("Appointment Confirmed!!");window.location='/health_view_appointment'</script>'''
        
        if action == 'attended':
            q1 = 'update appointment set status="Attended" where appointment_id="%s"' % (id)
            update(q1)
            return '''<script>alert("Appointment Successfully Completed!!");window.location='/health_view_appointment'</script>'''
        
        if action == 'not_attended':
            q1 = 'update appointment set status="Not Attended" where appointment_id="%s"' % (id)
            update(q1)


            return '''<script>alert("Appointment Cancelled!!");window.location='/health_view_appointment'</script>'''
        return render_template('health_view_appointment.html', data=data)


# Medication
@health.route('/health_add_medication', methods=['get', 'post'])
def health_add_medication():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data = {}
        
        if 'action' in request.args:
            action = request.args['action']
            id = request.args['id']
        else:
            action = None
        
        if action == 'add':
            if 'submit' in request.form:
                title = request.form['title']
                description = request.form['description']
                qry = "insert into medication(appointment_id,title,description) values('%s','%s','%s') " % (
                    id, title, description)
                insert(qry)
                q1 = 'update appointment set status="Prescribed" where appointment_id="%s"' % (id)
                update(q1)
                return '''<script>alert("Medication Added Successfully");window.location='/health_add_medication'</script>'''
            return render_template('health_add_medication.html', data=data)
        # return render_template('health_view_appointment.html', data=data)
        # return render_template('health_add_medication.html', data=data)
        return redirect(url_for("health.health_view_appointment"))
    

# Complaints and Response
@health.route('/health_send_complaint', methods=['get', 'post'])
def health_send_complaint():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data = {}

        if 'submit' in request.form:
            des = request.form['complaint']
            now = datetime.now()
            date = now.strftime('%d-%m-%Y')
            qry1 = "insert into complaints(username,complaint_des,date,reply) values ('%s','%s','%s','Please wait for the Response')" % (
                session['lid'], des,date)
            res = insert(qry1)
            return '''<script>alert("Complaint Send Successfully");window.location='/health_send_complaint'</script>'''
        qry = "select * from complaints where username='%s'" % (session['lid'])
        res = select(qry)
        data['view'] = res
        return render_template('health_send_complaint.html', data=data)

# Staff List
@health.route('/health_view_staff',methods=['get','post'])
def health_view_staff():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data={}
        q0="select * from staff inner join result using(staff_id)"
        res=select(q0)
        data['view']=res
        return render_template('health_view_staff.html',data=data)

# Staff Assessment Details
@health.route('/health_view_result', methods=['get', 'post'])
def health_view_result():
    if session.get('lid') is None:
        return redirect(url_for('public.login'))
    else:
        data = {}
        id = request.args['id']
        qry = "SELECT * FROM result INNER JOIN staff USING (staff_id) WHERE staff_id='%s'" % id
        res = select(qry)
        
        re1 = float(res[0]['r1'])
        re2 = float(res[0]['r2'])
        re3 = float(res[0]['r3'])
        re4 = float(res[0]['r4'])
        
        print("re1:", re1, "\nre2:", re2, "\nre3:", re3, "\nre4:", re4)
       
        # if re1 == 0.0 and re2 == 0.0 and re3 == 0.0 and re4 == 0.0:
        #     v = 'No Depression'
        # elif re1 == 0.0 and re2 == 0.0 and re3 != 0.0 and re4 >= 2.0:
        #     v = 'No Depression'
        # elif re1 == 1.0 and re2 == 0.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Mild Depression'
        # elif re1 == 2.0 and re2 == 0.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Mild Depression'
        # elif re1 == 3.0 and re2 == 0.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Moderate Depression'
        # elif re1 == 4.0 and re2 == 0.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Moderate Depression'
        # elif re1 == 0.0 and re2 == 1.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Mild Depression'
        # elif re1 == 1.0 and re2 == 1.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Moderate Depression'
        # elif re1 == 2.0 and re2 == 1.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Moderately Severe Depression'
        # elif re1 == 3.0 and re2 == 1.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Severe Depression'
        # elif re1 == 4.0 and re2 == 1.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Severe Depression'
        # else:
        #     v = 'No Depression'
        
        if re1 == 4 and re4 == 3 and re2 == 1 and re3 == 0:
            v = 'Severe Depression'
        elif re1 == 4 and re4 == 3 and re2 == 0 and re3 == 1:
            v = 'Severe Depression'
        elif re1 == 4 and re4 == 3 and re2 == 0 and re3 == 0:
            v = 'Severe Depression'
        elif re1 == 4 and re4 == 2 and re2 == 1 and re3 == 1:
            v = 'Severe Depression'
        elif re1 == 4 and re4 == 2 and re2 == 1 and re3 == 0:
            v = 'Severe Depression'
        elif re1 == 4 and re4 == 2 and re2 == 0 and re3 == 1:
            v = 'Severe Depression'
        elif re1 == 4 and re4 == 2 and re2 == 0 and re3 == 0:
            v = 'Severe Depression'
        elif re1 == 4 and re4 == 1 and re2 == 1 and re3 == 1:
            v = 'Severe Depression'
        elif re1 == 4 and re4 == 1 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 4 and re4 == 1 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 4 and re4 == 1 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 4 and re4 == 0 and re2 == 1 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 4 and re4 == 4 and re2 == 1 and re3 == 0:
            v = 'No Depression'
        elif re1 == 4 and re4 == 4 and re2 == 1 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 4 and re4 == 4 and re2 == 0 and re3 == 1:
            v = 'No Depression'
        elif re1 == 4 and re4 == 4 and re2 == 0 and re3 == 0:
            v = 'No Depression'
        elif re1 == 4 and re4 == 4 and re2 == 0 and re3 == 1:
            v = 'No Depression'    
        elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'    
        elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 3 and re2 == 1 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 3 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 2 and re2 == 1 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 2 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 0 and re2 == 1 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 0 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
            v = 'Severe Depression'
        elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
            v = 'Severe Depression'
        elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
            v = 'Severe Depression'
        elif re1 == 2 and re4 == 4 and re2 == 1 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 4 and re2 == 1 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 3 and re2 == 1 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 3 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 2 and re4 == 2 and re2 == 1 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 2 and re4 == 2 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 2 and re4 == 0 and re2 == 1 and re3 == 1:
            v = 'Mild Depression'
        elif re1 == 2 and re4 == 0 and re2 == 1 and re3 == 0:
            v = 'Mild Depression'
        elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 1:
            v = 'Mild Depression'
        elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 0:
            v = 'Mild Depression'
        elif re1 == 1 and re4 == 4 and re2 == 1 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 1 and re4 == 4 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 1 and re4 == 4 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 1 and re4 == 4 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 1 and re4 == 3 and re2 == 1 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 1 and re4 == 3 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 1 and re4 == 3 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 1 and re4 == 3 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 1 and re4 == 2 and re2 == 1 and re3 == 1:
            v = 'Mild Depression'
        elif re1 == 1 and re4 == 2 and re2 == 1 and re3 == 0:
            v = 'Mild Depression'
        elif re1 == 1 and re4 == 2 and re2 == 0 and re3 == 1:
            v = 'Mild Depression'
        elif re1 == 1 and re4 == 2 and re2 == 0 and re3 == 0:
            v = 'Mild Depression'
        elif re1 == 1 and re4 == 1 and re2 == 1 and re3 == 1:
            v = 'Mild Depression'
        elif re1 == 1 and re4 == 1 and re2 == 1 and re3 == 0:
            v = 'Mild Depression'
        elif re1 == 1 and re4 == 1 and re2 == 0 and re3 == 1:
            v = 'Mild Depression'
        elif re1 == 1 and re4 == 1 and re2 == 0 and re3 == 0:
            v = 'Mild Depression'
        elif re1 == 0 and re4 == 4 and re2 == 1 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 0 and re4 == 4 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 0 and re4 == 4 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 0 and re4 == 4 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 0 and re4 == 3 and re2 == 1 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 0 and re4 == 3 and re2 == 1 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 0 and re4 == 3 and re2 == 0 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 0 and re4 == 3 and re2 == 0 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 0 and re4 == 2 and re2 == 1 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 0 and re4 == 2 and re2 == 1 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 0 and re4 == 2 and re2 == 0 and re3 == 1:
            v = 'Mild Depression'
        elif re1 == 0 and re4 == 2 and re2 == 0 and re3 == 0:
            v = 'Mild Depression'
        elif re1 == 0 and re4 == 1 and re2 == 1 and re3 == 1:
            v = 'Mild Depression'
        elif re1 == 0 and re4 == 1 and re2 == 1 and re3 == 0:
            v = 'Mild Depression'
        elif re1 == 0 and re4 == 1 and re2 == 0 and re3 == 1:
            v = 'No Depression'
        elif re1 == 0 and re4 == 1 and re2 == 0 and re3 == 0:
            v = 'No Depression'
        elif re1 == 0 and re4 == 0 and re2 == 1 and re3 == 1:
            v = 'No Depression'
        elif re1 == 0 and re4 == 0 and re2 == 1 and re3 == 0:
            v = 'No Depression'
        elif re1 == 0 and re4 == 0 and re2 == 0 and re3 == 1:
            v = 'No Depression'
        elif re1 == 0 and re4 == 0 and re2 == 0 and re3 == 0:
            v = 'No Depression' 
        elif re1 == 4 and re4 == 0 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 4 and re4 == 0 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 4 and re4 == 0 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 3 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 2 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 1:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 0:
            v = 'Moderate Depression'
        elif re1 == 3 and re4 == 0 and re2 == 1 and re3 == 0:
            v = 'Mild Depression'
        elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 1:
            v = 'Mild Depression'
        elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 0:
            v = 'Mild Depression'

        elif re1 == 2 and re4 == 4 and re2 == 1 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 3 and re2 == 1 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 2 and re2 == 1 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 1:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 0:
            v = 'Moderately Severe Depression'
        elif re1 == 2 and re4 == 0 and re2 == 1 and re3 == 0:
            v = 'Severe Depression'
        elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 1:
            v = 'Severe Depression'
        elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 0:
            v = 'Severe Depression'
        else:
            v = 'No Depression' 
                               
        data['view'] = res
        return render_template('health_view_result.html',data=data,v=v)



# New Appointment
@health.route('/health_schedule_appointment',methods=['get','post'])
def health_schedule_appointment():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data={}
        if 'action' in request.args:
            action = request.args['action']
            id = request.args['id']
        else:
            action = None

        if action == 'make':
            if 'submit' in request.form:
                date=request.form['a_date']
                # date = datetime.strptime(date,'%Y-%m-%d').strftime('%d-%m-%Y')
                q1="delete from appointment where staff_id='%s'"%(id)
                delete(q1)
                q = "insert into appointment(health_id,staff_id,status,date) values('%s','%s','Confirmed','%s')" %(session['hli'],id,date)
                res=insert(q)
                print(res)
                return '''<script>alert("Appointment Scheduled Successfully");window.location='/health_schedule_appointment'</script>'''
            
            return render_template('health_schedule_appointment.html', data=data)
        return redirect(url_for("health.health_view_appointment"))