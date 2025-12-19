
from flask import *
from database import *
import uuid 
from database import *
from datetime import *
from core import *
from models import Model
from depression_detection_tweets import DepressionDetection
from TweetModel import process_message
import os
from em import *

staff = Blueprint('staff', __name__)

# Staff Home Page
@staff.route('/staff_home')
def staff_home():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data={}
        qry="select * from staff where staff_id='%s'" %(session['sli'])
        res=select (qry)
        data['view']=res
        return render_template('staff_home.html',data=data)

# Update and View Profile
@staff.route('/staff_view_profile', methods=['get', 'post'])
def staff_view_profile():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data = {}
        qry = "select * from staff where staff_id='%s'" % (session['sli'])
        res = select(qry)
        session['img']=res[0]['s_photo']
        session['resu']=res[0]['s_resume']
        session['certi']=res[0]['s_certificate']
        data['view'] = res
        print(res)
        des=data['view'][0]['designation_id']
        q1="select * from designation where designation_id='%s'"%(des)
        data['des']=select(q1)
        qry4="select * from p_address inner join c_address using (username) where username='%s'"%(session['lid'])
        res4=select(qry4)
        print(res4)
        data['add']=res4
        
        if 'submit' in request.form:
            a_phone_no=request.form['a_phone_no']
            a_email=request.form['a_email']
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
            certificate=request.files['certificate']
            path1='static/assets/certiresume/'+str(uuid.uuid4())+certificate.filename
            certificate.save(path1)
            path2='static/assets/certiresume/'+str(uuid.uuid4())+resume.filename
            resume.save(path2)
            qry2 = "update p_address set address_line1='%s',address_line2='%s',landmark='%s',pincode='%s',city='%s',state='%s',country='%s' where username='%s'" % (p_address_line_1,p_address_line_2,landmark,pincode,city,state,country,session['lid'])  
            update(qry2)   
            qry3 = "update c_address set c_address_line1='%s',c_address_line2='%s',c_landmark='%s',c_pincode='%s',c_city='%s',c_state='%s',c_country='%s' where username='%s'" %(c_address_line_1,c_address_line_2,clandmark,cpincode,ccity,cstate,ccountry,session['lid']) 
            update(qry3)
            qry4 = "update staff set s_resume='%s',s_certificate='%s', as_email_id='%s',as_phone_no='%s' where staff_id='%s'" % (path2,path1,a_email,a_phone_no, session['sli'])
            update(qry4)

            # Profile picture
            if profile:
                path='static/assets/img/profile/'+str(uuid.uuid4())+profile.filename
                profile.save(path)
                qry5 = "update staff set s_photo='%s' where staff_id='%s'" % (path,session['sli'])
                update(qry5)
            else:
                qry5 = "update staff set s_photo='%s' where staff_id='%s'" % (session['img'],session['sli'])
                update(qry5)
            return '''<script>alert("Profile Updated Successfully");window.location='/staff_view_profile'</script>'''
        return render_template('staff_view_profile.html', data=data)

# Change Password
@staff.route('/staff_change_password', methods=['get', 'post'])
def staff_change_password():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
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
                    flash("")
                    return '''<script>alert("Password Updated Successfully!!");window.location='/staff_change_password'</script>'''
                else:
                    return '''<script>alert("Password doesnot Match!!");window.location='/staff_change_password'</script>'''
            else:
                return '''<script>alert("Incorrect password!!");window.location='/staff_change_password'</script>'''
        return render_template('staff_change_password.html')

#View Health Care Team Details for staff
@staff.route('/staff_more_health_team_detail', methods=['get', 'post'])
def more_health_team_detail():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data = {}
        if 'action' in request.args:
            action = request.args['action']
            id = request.args['id']
        else:
            action = None
            
        if action=='view':
            qq="select * from health_care_team where health_id='%s'"%(id)
            qq1="select * from c_address inner join health_care_team using (username) where health_id='%s'"%(id)
            qq2="select * from p_address inner join health_care_team using (username) where health_id='%s'"%(id)
            data['basic']=select(qq)
            data['caddr']=select(qq1)
            data['paddr']=select(qq2)
        return render_template('staff_more_health_team_detail.html', data=data)

# Notification
@staff.route('/staff_view_notification', methods=['get', 'post'])
def staff_view_notification():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data = {}
        qry = "select * from notification where user_type='admin'"
        res = select(qry)
        data['view'] = res
        qry = "select * from notification where user_type='health'"
        res = select(qry)
        data['view1'] = res
        return render_template('staff_view_notification.html', data=data)

# Complaints and Response
@staff.route('/staff_send_complaint', methods=['get', 'post'])
def staff_send_complaint():
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
            return '''<script>alert("Grievance Send Successfully");window.location='/staff_send_complaint'</script>'''
        qry = "select * from complaints where username='%s'" % (session['lid'])
        res = select(qry)
        data['view'] = res
        return render_template('staff_send_complaint.html', data=data)

# Appointment Booking and Status check
@staff.route('/staff_make_appointment', methods=['get', 'post'])
def staff_make_appointment():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data = {}
        q1 = "select * from health_care_team"
        res = select(q1)
        data['view'] = res
        if 'submit' in request.form:
            date = request.form['a_date']
            # date = datetime.strptime(date,'%Y-%m-%d').strftime('%d-%m-%Y')
            doctor = request.form['health']
            q = "insert into appointment(date,status,health_id,staff_id) values('%s','Confirmation Pending','%s','%s')" % (
                date, doctor, session['sli'])
            res = insert(q)
            return '''<script>alert("Booking Succesfully, Wait for Confirmation!!");window.location='/staff_make_appointment'</script>'''
        q2 = "select * from appointment where staff_id='%s'" % (session['sli'])
        res1 = select(q2)
        data['v'] = res1
        return render_template('staff_make_appointment.html', data=data)

# About doctors
@staff.route('/staff_know_doctor', methods=['get','post'])
def staff_know_doctor():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        item={}
        if 'searchbtn' in request.form:
            search=request.form['search']
            category=request.form['category']
            
            if category=='all' and ( search=='' or search!=""):
                qryy="select * from health_care_team"
                ress=select(qryy)
                item['view']=ress
            elif category=='name' and search!=' ':
                qryy="select * from health_care_team where h_fname LIKE '%s%s'"%(search,'%')
                ress=select(qryy)
                item['view']=ress
            elif category=='namee' and search!=' ':
                qryy="select * from health_care_team where h_lname LIKE '%s%s'"%(search,'%')
                ress=select(qryy)
                item['view']=ress
        return render_template('staff_know_doctor.html',item=item)

# View Medication
@staff.route('/staff_take_medication', methods=['get', 'post'])
def staff_take_medication():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        data = {}
        if 'action' in request.args:
            action = request.args['action']
            id = request.args['id']
        else:
            action = None
        
        if action == 'medication':
            q1 = "select * from medication where appointment_id='%s' order by medication_id" % (id)
            res = select(q1)
            data['view'] = res
        return render_template('staff_take_medication.html', data=data)

# Take Test
@staff.route("/take_test_ins")
def take_test_ins():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        return render_template('take_test_ins.html')

# Phase 1
@staff.route("/take_test")
def take_test():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        return render_template("index1.html")

# Questionnaire Based Test
@staff.route('/predict', methods=["POST"])
def predict():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        q1 = int(request.form['a1'])
        q2 = int(request.form['a2'])
        q3 = int(request.form['a3'])
        q4 = int(request.form['a4'])
        q5 = int(request.form['a5'])
        q6 = int(request.form['a6'])
        q7 = int(request.form['a7'])
        q8 = int(request.form['a8'])
        q9 = int(request.form['a9'])
        q10 = int(request.form['a10'])

        values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
        model = Model()
        classifier = model.svm_classifier()
        prediction = classifier.predict([values])
        
        if prediction[0] == 0:
                session['r1']=prediction[0]
                return redirect(url_for('staff.sentiment')) 
                
        if prediction[0] == 1:
                session['r1']=prediction[0] 
                return redirect(url_for('staff.sentiment'))
        
        if prediction[0] == 2:
                session['r1']=prediction[0] 
                return redirect(url_for('staff.sentiment'))
        
        if prediction[0] == 3:
                session['r1']=prediction[0] 
                return redirect(url_for('staff.sentiment'))
        
        if prediction[0] == 4:
                session['r1']=prediction[0] 
                return redirect(url_for('staff.sentiment'))

# Phase 2
@staff.route("/sentiment")
def sentiment():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        return render_template("sentiment.html")

# Sentiment Based Test
@staff.route("/predictSentiment",  methods=['get', 'post'])
def predictSentiment():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        message = request.form['form10']
        pm = process_message(message)
        result = DepressionDetection.classify(pm, 'bow') or DepressionDetection.classify(pm, 'tf-idf')
        session['r2']=result
        return redirect(url_for("staff.voice_change"))
    
@staff.route('/voice_change',methods=['get','post'])
def voice_change():
    data={}
    if 'submit' in request.form:
        message=request.form['sen']
        print("****************************** :::")
        print(message)
        pm = process_message(message)
        result = DepressionDetection.classify(pm, 'bow') or DepressionDetection.classify(pm, 'tf-idf')
        session['r3']=result
        return redirect(url_for('staff.camera'))
    return render_template('upload_voice.html',data=data)

# Phase 3
# Real Time Camera Based Test
@staff.route("/camera")
def camera():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        # from em import camclick
        q=camclick()
        session['r4']=q
        print("rrrrrrrrrrrrrrrrrrrrrr",session['r4'])
        return redirect(url_for('staff.add_result'))

# Successful
@staff.route("/test_completed")
def test_completed():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        return render_template('test_completed.html')

# Result Entering Process       
@staff.route('/add_result',methods=['get','post'])
def add_result():
    if session.get('lid') is None:
        return redirect (url_for('public.login'))
    else:
        result1=session['r1']
        result2=session['r2']
        result3=session['r3']
        print("sssssssssssssssssssssssssssss",session['r3'])
        result4=session['r4']
        
        

        print("result1 : ",result1)
        print("result2 : ",result2)
        print("result3 : ",result3)
        print("result4 : ",result4)

        if result4 == 'neutral':
            result4=3
        if result4 == 'happy':
            result4=0
        if result4 == 'surprise':
            result4=0   
        if result4 == 'sad':
            result4=4
        if result4 == 'fear':
            result4=4
        if result4 == 'disgust':
            result4=1
        if result4 == 'angry':
            result4=2
        
        if result4:
            qa="select * from result where staff_id='%s' and date=curdate()"%(session['sli'])
            ra=select(qa)
            if ra:
                qa="update result set r1='%s',r2='%s',r3='%s',r4='%s' where staff_id='%s'"%(result1,result2,result3,result4,session['sli'])
                update(qa)
                
            else:
                q="INSERT INTO result(r1,r2,r3,r4,staff_id,date) VALUES('%s','%s','%s','%s','%s',curdate())"%(result1,result2,result3,result4,session['sli'])
                res=insert(q)
                    
                print(res)
        return redirect(url_for('staff.test_completed'))
    

# @staff.route('/staff_view_result', methods=['get', 'post'])
# def staff_view_result():
#     num=""
#     if session.get('lid') is None:
#         return redirect(url_for('public.login'))
#     else:
#         data = {}
#         # id = request.args['id']
#         qry = "SELECT * FROM result INNER JOIN staff USING (staff_id) WHERE staff_id='%s'" % session['sli']
#         res = select(qry)
        
#         re1 = float(res[0]['r1'])
#         re2 = float(res[0]['r2'])
#         re3 = float(res[0]['r3'])
#         re4 = float(res[0]['r4'])
        
#         print("re1:", re1, "\nre2:", re2, "\nre3:", re3, "\nre4:", re4)
       
        
        
#         if re1 == 4 and re4 == 3 and re2 == 1 and re3 == 0:
#             v = 'Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='1'
#         elif re1 == 4 and re4 == 3 and re2 == 0 and re3 == 1:
#             v = 'Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='1'
#         elif re1 == 4 and re4 == 3 and re2 == 0 and re3 == 0:
#             v = 'Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='1'
#         elif re1 == 4 and re4 == 2 and re2 == 1 and re3 == 1:
#             v = 'Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='1'
#         elif re1 == 4 and re4 == 2 and re2 == 1 and re3 == 0:
#             v = 'Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='1'
#         elif re1 == 4 and re4 == 2 and re2 == 0 and re3 == 1:
#             v = 'Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='1'
#         elif re1 == 4 and re4 == 2 and re2 == 0 and re3 == 0:
#             v = 'Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='1'
#         elif re1 == 4 and re4 == 1 and re2 == 1 and re3 == 1:
#             v = 'Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='1'
#         elif re1 == 4 and re4 == 1 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='2'
#         elif re1 == 4 and re4 == 1 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='2'
#         elif re1 == 4 and re4 == 1 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='2'
#         elif re1 == 4 and re4 == 0 and re2 == 1 and re3 == 1:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
            
#             num='2'
#         elif re1 == 4 and re4 == 4 and re2 == 1 and re3 == 0:
#             v = 'No Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 4 and re4 == 4 and re2 == 1 and re3 == 1:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)     
#             num='2'
#         elif re1 == 4 and re4 == 4 and re2 == 0 and re3 == 1:
#             v = 'No Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 4 and re4 == 4 and re2 == 0 and re3 == 0:
#             v = 'No Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 4 and re4 == 4 and re2 == 0 and re3 == 1:
#             v = 'No Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'    
#         elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 1:
#             v = 'Moderately Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='4'
#         elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
#             v = 'Moderately Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='4'
#         elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
#             v = 'Moderately Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='4'
#         elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression' 
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'   
#         elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 1:
#             v = 'Moderately Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='4'
#         elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
#             v = 'Moderately Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='4'
#         elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
#             v = 'Moderately Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='4'
#         elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 3 and re2 == 1 and re3 == 1:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 3 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 2 and re2 == 1 and re3 == 1:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 2 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 1:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 0 and re2 == 1 and re3 == 1:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 0 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='3'
#         elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
#             v = 'Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='1'
#         elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
#             v = 'Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='1'
#         elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
#             v = 'Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='1'
#         elif re1 == 2 and re4 == 4 and re2 == 1 and re3 == 1:
#             v = 'Moderately Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='4'
#         elif re1 == 2 and re4 == 4 and re2 == 1 and re3 == 0:
#             v = 'Moderately Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='4'
#         elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 1:
#             v = 'Moderately Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='4'
#         elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 0:
#             v = 'Moderately Severe Depression'
#             qry6="insert into predicted_result values(null,'%s','%s',curdate())"%(v,session['sli'])
#             insert(qry6)
#             num='4'
#         elif re1 == 2 and re4 == 3 and re2 == 1 and re3 == 1:
#             v = 'Moderately Severe Depression'
#             num='4'
#         elif re1 == 2 and re4 == 3 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 2 and re4 == 2 and re2 == 1 and re3 == 1:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 2 and re4 == 2 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 1:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 2 and re4 == 0 and re2 == 1 and re3 == 1:
#             v = 'Mild Depression'
#             num='5'
#         elif re1 == 2 and re4 == 0 and re2 == 1 and re3 == 0:
#             v = 'Mild Depression'
#             num='5'
#         elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 1:
#             v = 'Mild Depression'
#             num='5'
#         elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 0:
#             v = 'Mild Depression'
#         elif re1 == 1 and re4 == 4 and re2 == 1 and re3 == 1:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 1 and re4 == 4 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 1 and re4 == 4 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 1 and re4 == 4 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 1 and re4 == 3 and re2 == 1 and re3 == 1:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 1 and re4 == 3 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 1 and re4 == 3 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 1 and re4 == 3 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#             num='3'
#         elif re1 == 1 and re4 == 2 and re2 == 1 and re3 == 1:
#             v = 'Mild Depression'
#         elif re1 == 1 and re4 == 2 and re2 == 1 and re3 == 0:
#             v = 'Mild Depression'
#         elif re1 == 1 and re4 == 2 and re2 == 0 and re3 == 1:
#             v = 'Mild Depression'
#         elif re1 == 1 and re4 == 2 and re2 == 0 and re3 == 0:
#             v = 'Mild Depression'
#         elif re1 == 1 and re4 == 1 and re2 == 1 and re3 == 1:
#             v = 'Mild Depression'
#         elif re1 == 1 and re4 == 1 and re2 == 1 and re3 == 0:
#             v = 'Mild Depression'
#         elif re1 == 1 and re4 == 1 and re2 == 0 and re3 == 1:
#             v = 'Mild Depression'
#         elif re1 == 1 and re4 == 1 and re2 == 0 and re3 == 0:
#             v = 'Mild Depression'
#         elif re1 == 0 and re4 == 4 and re2 == 1 and re3 == 1:
#             v = 'Moderate Depression'
#         elif re1 == 0 and re4 == 4 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#         elif re1 == 0 and re4 == 4 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#         elif re1 == 0 and re4 == 4 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#         elif re1 == 0 and re4 == 3 and re2 == 1 and re3 == 1:
#             v = 'Moderately Severe Depression'
#         elif re1 == 0 and re4 == 3 and re2 == 1 and re3 == 0:
#             v = 'Moderately Severe Depression'
#         elif re1 == 0 and re4 == 3 and re2 == 0 and re3 == 1:
#             v = 'Moderately Severe Depression'
#         elif re1 == 0 and re4 == 3 and re2 == 0 and re3 == 0:
#             v = 'Moderately Severe Depression'
#         elif re1 == 0 and re4 == 2 and re2 == 1 and re3 == 1:
#             v = 'Moderately Severe Depression'
#         elif re1 == 0 and re4 == 2 and re2 == 1 and re3 == 0:
#             v = 'Moderately Severe Depression'
#         elif re1 == 0 and re4 == 2 and re2 == 0 and re3 == 1:
#             v = 'Mild Depression'
#         elif re1 == 0 and re4 == 2 and re2 == 0 and re3 == 0:
#             v = 'Mild Depression'
#         elif re1 == 0 and re4 == 1 and re2 == 1 and re3 == 1:
#             v = 'Mild Depression'
#         elif re1 == 0 and re4 == 1 and re2 == 1 and re3 == 0:
#             v = 'Mild Depression'
#         elif re1 == 0 and re4 == 1 and re2 == 0 and re3 == 1:
#             v = 'No Depression'
#         elif re1 == 0 and re4 == 1 and re2 == 0 and re3 == 0:
#             v = 'No Depression'
#         elif re1 == 0 and re4 == 0 and re2 == 1 and re3 == 1:
#             v = 'No Depression'
#         elif re1 == 0 and re4 == 0 and re2 == 1 and re3 == 0:
#             v = 'No Depression'
#         elif re1 == 0 and re4 == 0 and re2 == 0 and re3 == 1:
#             v = 'No Depression'
#         elif re1 == 0 and re4 == 0 and re2 == 0 and re3 == 0:
#             v = 'No Depression' 
#         elif re1 == 4 and re4 == 0 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#         elif re1 == 4 and re4 == 0 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#         elif re1 == 4 and re4 == 0 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 3 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 2 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 1:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 0:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 1:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 0:
#             v = 'Moderate Depression'
#         elif re1 == 3 and re4 == 0 and re2 == 1 and re3 == 0:
#             v = 'Mild Depression'
#         elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 1:
#             v = 'Mild Depression'
#         elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 0:
#             v = 'Mild Depression'

#         elif re1 == 2 and re4 == 4 and re2 == 1 and re3 == 0:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 1:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 0:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 3 and re2 == 1 and re3 == 0:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 1:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 0:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 2 and re2 == 1 and re3 == 0:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 1:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 0:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 1:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 0:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 1:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 0:
#             v = 'Moderately Severe Depression'
#         elif re1 == 2 and re4 == 0 and re2 == 1 and re3 == 0:
#             v = 'Severe Depression'
#         elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 1:
#             v = 'Severe Depression'
#         elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 0:
#             v = 'Severe Depression'
#         else:
#             v = 'No Depression' 
                               
#         data['view'] = res
#         return render_template('staff_view_result.html',data=data,v=v,num=num)


@staff.route('/staff_view_result', methods=['get', 'post'])
def staff_view_result():
    if session.get('lid') is None:
        return redirect(url_for('public.login'))

    data = {}
    qry = "SELECT * FROM result INNER JOIN staff USING (staff_id) WHERE staff_id='%s'" % session['sli']
    res = select(qry)

    re1, re2, re3, re4 = float(res[0]['r1']), float(res[0]['r2']), float(res[0]['r3']), float(res[0]['r4'])
    print("re1:", re1, "\nre2:", re2, "\nre3:", re3, "\nre4:", re4)
    avg_re=float(re1+re2+re3+re4)/4
    print(avg_re)

    depression_levels={
    # Severe Depression
    (4, 1, 2, 0): 'Severe Depression',
    (3, 4, 0, 1): 'Severe Depression',
    (4, 2, 2, 0): 'Severe Depression',
    (4, 0, 2, 1): 'Severe Depression',
    (3, 3, 0, 2): 'Severe Depression',
    (4, 1, 0, 2): 'Severe Depression',
    (3, 0, 2, 2): 'Severe Depression',
    (3, 1, 2, 1): 'Severe Depression',
    (4, 2, 1, 1): 'Severe Depression',
    (3, 0, 1, 3): 'Severe Depression',
    (3, 1, 1, 3): 'Severe Depression',
    (3, 1, 1, 3): 'Severe Depression',
    
    
    

    # Moderate Depression
    (2, 3, 2, 0): 'Moderate Depression',
    (3, 2, 2, 1): 'Moderate Depression',
    (2, 2, 1, 2): 'Moderate Depression',
    (2, 2, 2, 1): 'Moderate Depression',
    (3, 1, 2, 2): 'Moderate Depression',
    (2, 1, 1, 3): 'Moderate Depression',
    (3, 0, 3, 0): 'Moderate Depression',
    (2, 3, 0, 2): 'Moderate Depression',
    (2, 1, 2, 2): 'Moderate Depression',
    (3, 1, 1, 2): 'Moderate Depression',

    # Mild Depression
    (2, 1, 2, 0): 'Mild Depression',
    (1, 2, 2, 1): 'Mild Depression',
    (2, 2, 1, 1): 'Mild Depression',
    (1, 1, 2, 2): 'Mild Depression',
    (2, 0, 3, 1): 'Mild Depression',
    (1, 2, 1, 2): 'Mild Depression',
    (2, 1, 0, 3): 'Mild Depression',
    (1, 1, 1, 3): 'Mild Depression',
    (2, 2, 0, 2): 'Mild Depression',
    (1, 0, 2, 2): 'Mild Depression',

    # No Depression
    (0, 1, 2, 1): 'No Depression',
    (1, 0, 3, 0): 'No Depression',
    (0, 2, 1, 2): 'No Depression',
    (1, 3, 0, 0): 'No Depression',
    (0, 0, 2, 1): 'No Depression',
    (1, 1, 0, 3): 'No Depression',
    (0, 3, 1, 0): 'No Depression',
    (1, 0, 2, 0): 'No Depression',
    (0, 2, 0, 1): 'No Depression',
    (1, 1, 2, 0): 'No Depression',
    
    # Default case
    (0, 0, 0, 0): 'No Depression'
}


    conditions = (re1, re2, re3, re4)
    print(conditions)
    v = depression_levels.get(conditions, 'Unknown Depression Level')
    print("]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]",v)
    qry="select * from predicted_result where staff_id='%s' and date=curdate()"%(session['sli'])
    re1=select(qry)
    if re1:
        qry7="update predicted_result set p_result='%s'"%(v)
        update(qry7)
    else:
        qry6 = "insert into predicted_result values(null,'%s','%s',curdate(),'%s')" % (v, session['sli'],avg_re)
        insert(qry6)
    

        

    num = 'Unknown'
    if v == 'Severe Depression':
        num = '1'
    elif v == 'Moderate Depression':
        num = '2'
    elif v == 'Mild Depression':
        num = '3'
    elif v == 'Moderately Severe Depression':
        num = '4'
    elif v == 'No Depression':
        num = '5'

    data['view'] = res
    return render_template('staff_view_result.html', data=data, v=v, num=num)

@staff.route('/staff_view_graph', methods=['get', 'post'])
def staff_view_graph():
    import datetime

    data={}
    current_date = datetime.date.today()
    print(current_date)
    qry="""
    SELECT 
        e.date,
        AVG(e.emotions_score) AS average_score,
        s.staff_id,
        s.first_name,
        s.last_name,
        CASE
            WHEN AVG(e.emotions_score) BETWEEN 0 AND 1 THEN 'angry'
            WHEN AVG(e.emotions_score) BETWEEN 1 AND 2 THEN 'disgust'
            WHEN AVG(e.emotions_score) BETWEEN 2 AND 3 THEN 'fear'
            WHEN AVG(e.emotions_score) BETWEEN 3 AND 4 THEN 'happy'
            WHEN AVG(e.emotions_score) BETWEEN 4 AND 5 THEN 'sad'
            WHEN AVG(e.emotions_score) BETWEEN 5 AND 6 THEN 'surprise'
            WHEN AVG(e.emotions_score) BETWEEN 6 AND 7 THEN 'neutral'
            ELSE 'unknown' -- or handle other cases as needed
        END AS detected_emotion
    FROM 
        emotions e
    JOIN 
        staff s ON e.staff_id = s.staff_id
    WHERE s.staff_id='%s' and e.date='%s'
    GROUP BY 
        e.date, s.staff_id, s.first_name, s.last_name
    
    
"""%(session['sli'],current_date)
    data['em']=select(qry)
    print(data['em'])
    print(qry)  
    
    
    if 'dsubmit' in request.form:
        dateinput=request.form['dinput']
        qry="""
    SELECT 
        e.date,
        AVG(e.emotions_score) AS average_score,
        s.staff_id,
        s.first_name,
        s.last_name,
        CASE
            WHEN AVG(e.emotions_score) BETWEEN 0 AND 1 THEN 'angry'
            WHEN AVG(e.emotions_score) BETWEEN 1 AND 2 THEN 'disgust'
            WHEN AVG(e.emotions_score) BETWEEN 2 AND 3 THEN 'fear'
            WHEN AVG(e.emotions_score) BETWEEN 3 AND 4 THEN 'happy'
            WHEN AVG(e.emotions_score) BETWEEN 4 AND 5 THEN 'sad'
            WHEN AVG(e.emotions_score) BETWEEN 5 AND 6 THEN 'surprise'
            WHEN AVG(e.emotions_score) BETWEEN 6 AND 7 THEN 'neutral'
            ELSE 'unknown' -- or handle other cases as needed
        END AS detected_emotion
    FROM 
        emotions e
    JOIN 
        staff s ON e.staff_id = s.staff_id
    WHERE s.staff_id='%s' and e.date='%s'
    GROUP BY 
        e.date, s.staff_id, s.first_name, s.last_name
    
    
"""%(session['sli'],dateinput)
    data['din']=select(qry)
    print(data['din'])
    print(qry)  
        
    if 'msubmit' in request.form:
        monthinput = request.form['monthYearInput']

        # Split the month and year
        selected_month, selected_year = monthinput.split()

        # Map month names to their corresponding numbers
        month_mapping = {
            'January': '01',
            'February': '02',
            'March': '03',
            'April': '04',
            'May': '05',
            'June': '06',
            'July': '07',
            'August': '08',
            'September': '09',
            'October': '10',
            'November': '11',
            'December': '12'
        }

        # Use the mapping to get the numeric month
        selected_month_numeric = month_mapping[selected_month]

        # Calculate start and end dates for the selected month
        start_date = f'{selected_year}-{selected_month_numeric}-01'
        end_date = f'{selected_year}-{selected_month_numeric}-31'  # Assuming the last day of the month

        qry = """
        SELECT 
            s.staff_id,
            s.first_name,
            s.last_name,
            AVG(e.emotions_score) AS average_score,
            CASE
                WHEN AVG(e.emotions_score) BETWEEN 0 AND 1 THEN 'angry'
                WHEN AVG(e.emotions_score) BETWEEN 1 AND 2 THEN 'disgust'
                WHEN AVG(e.emotions_score) BETWEEN 2 AND 3 THEN 'fear'
                WHEN AVG(e.emotions_score) BETWEEN 3 AND 4 THEN 'happy'
                WHEN AVG(e.emotions_score) BETWEEN 4 AND 5 THEN 'sad'
                WHEN AVG(e.emotions_score) BETWEEN 5 AND 6 THEN 'surprise'
                WHEN AVG(e.emotions_score) BETWEEN 6 AND 7 THEN 'neutral'
                ELSE 'unknown' -- or handle other cases as needed
        
            END AS detected_emotion
        FROM 
            emotions e
        JOIN 
            staff s ON e.staff_id = s.staff_id
        WHERE s.staff_id = '%s' AND e.date BETWEEN '%s' AND '%s'
        GROUP BY 
            s.staff_id, s.first_name, s.last_name
        """ % (session['sli'], start_date, end_date)

        data['min'] = select(qry)
        print(data['min'])
        print(qry)

        
    
        
    
        
        
    return render_template('staff_view_graph.html',data=data)


@staff.route('/staff_view_graphh', methods=['get', 'post'])
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
        
    WHERE s.staff_id='%s'
    GROUP BY 
        e.date, s.staff_id, s.first_name, s.last_name;

        """%(session['sli'])
    data['em']=select(qry)
    print("///////////////////////",data['em'])
    
    return render_template('staff_view_graphh.html',data=data)




# @staff.route("/check_notification")
# def check_notification():
#     # Implement a function to check the database for new complaints
#     new_notification = check_for_new_notification()
#     print("new_complaints: ", new_notification)

#     # Return the result as JSON
#     return jsonify({'new_notification': new_notification})

# def check_for_new_notification():
#     current_time = datetime.now().time()
    
#     # Implement the logic to query the database for new complaints
#     # For example, count the number of pending complaints
#     end_time_str = '12:30:54'  # Remove milliseconds
#     end_time = datetime.strptime(end_time_str, '%H:%M:%S').time()
    
#     q = "SELECT * FROM attendance WHERE staff_id = %s AND DATE = CURDATE()"%(session['sli'])
#     res = select(q)
    
#     if res and current_time > end_time:
        
#         return True
#     else:
#         return False





@staff.route("/check_notification")
def check_notification():
    # Implement a function to check the database for new complaints
    new_notification, message = check_for_new_notification()
    
    # Return the result as JSON
    return jsonify({'new_notification': new_notification, 'message': message})

def check_for_new_notification():
    current_time = datetime.now().time()
    
    # Implement the logic to query the database for new complaints
    # For example, count the number of pending complaints
    end_time_str = '22:30:54'  # Remove milliseconds
    end_time = datetime.strptime(end_time_str, '%H:%M:%S').time()
    
    q = "SELECT * FROM attendance WHERE staff_id = %s AND DATE = CURDATE()"%(session['sli'])
    res = select(q)
    
    if res and current_time > end_time:
        message = "You have new notifications."
        return True, message
    else:
        message = "No new notifications."
        return False, message