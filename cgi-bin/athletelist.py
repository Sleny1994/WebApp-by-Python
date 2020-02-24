#! /usr/local/bin/python3
# -*-coding:utf-8 -*-

def sanitize(time_string):
    if "-" in time_string:
        spliter = "-"
    elif ":" in time_string:
        spliter = ":"
    else:
        return(time_string)
    (mins, secs) = time_string.split(spliter)
    return(mins + "." + secs)

class AthleteList(list):
    def __init__(self, a_name, a_dob = None, a_times = []):
        # list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    # @property 重新指定为一个类属性，使用后会报错
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

    @property
    def clean_data(self):
        return(sorted(set([sanitize(t) for t in self])))

# def get_coach_data(filename):
#     try:
#         with open(filename) as f:
#             data = f.readline()
#         templ = data.strip().split(",")
#         # print(templ)
#         return(AthleteList(templ.pop(0), templ.pop(0), templ))
#     except IOError as ioerr:
#         print("File error: " + str(ioerr))
#         return(None)
