import cgi
form = cgi.FieldStorage()
x =  form.getvalue("city_name")
y =  form.getvalue("state_abrv")