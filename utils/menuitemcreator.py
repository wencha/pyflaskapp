import sys
if len(sys.argv)<2:
    print('Falta el nombre del menu como argumento')
    sys.exit(1)
if len(sys.argv)>2:
    print('Solo un argumento se admite')
    sys.exit(1)

mname = sys.argv[1].lower()
htmlpath = "flask1/templates/menu/{0}.html".format(mname)

import os.path
if os.path.isfile(htmlpath):
    sn = input('El archivo "{0}" ya existe, desea sobreescribirlo? [s/n]:'.format(htmlpath))
    if sn not in ['s','y']:
        print('Chau')
        sys.exit(1)

str=[]
str.append("------------- _menu.html")
str.append("{{{{url_for('main.menu_{0}')}}}}".format(mname))
str.append("")

str.append('''------------- routes.py
@bp.route("/menu/{0}", methods = ['GET', 'POST'])
@login_required
def menu_{0}():
    if request.method == "GET":
        db = get_db()
        DATA = db.query(TABLE).all()
        
        r = make_response(render_template(
            'menu/{0}.html',
            DATA=DATA
        ))
        return r
    else: #request.method == "POST":
        print('post form:',request.form)

        try: checkparams(request.form, ('PARAM1', 'PARAMN'))
        except Exception as e: return str(e), 400

        db = get_db()
        
        pass
        
        db.commit()

        return \'\''''.format(mname))
str.append("")

with open(htmlpath, "w") as f:
    f.write('''{{% extends '_maingui.html' %}}

{{% block content %}}
{{% call forms.card('{}')  %}}

{{% endcall %}}
{{% endblock %}}

{{% block js %}}
<script type="text/javascript">
$(function() {{
    
}});
</script>
{{% endblock %}}
'''.format(mname.upper()))

str.append("------------- {} creado".format(htmlpath))
print('\n'.join(str))