import cgi
import cgitb
import athletemodel
import yate

cgitb.enable()

athletes = athletemodel.get_from_store()
print(athletes)
form_data = cgi.FieldStorage()
print(form_data)
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete:" + athlete_name + ",DOB:" + athletes[athlete_name].dob + "."))
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athletes[athlete_name].top3()))
print(yate.include_footer({"Home":"../index.html", "Select another athlete":"generate_list.py"}))