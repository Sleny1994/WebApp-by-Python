import athletemodel
import yate
import glob

data_files = glob.glob("C:/Users/User1/Desktop/Python/Web App/data/*.txt")
athletes = athletemodel.put_to_store(data_files)
print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an athlete from the list to work with:"))

for each_authlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_authlete].name))
print(yate.end_form("Select"))
print(yate.include_footer({"Home": "../index.html"}))