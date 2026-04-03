from flask import Flask ,render_template,request,redirect,url_for
from models import db,Details
from flask_migrate import Migrate

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sandy4@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.init_app (app)
migrate = Migrate(app , db)

@app.route('/', methods=['GET','POST'])
def details_add():
    
    if request.method == 'POST':
        new_details = Details (name=request.form['name'], role=request.form['role'])
        db.session.add(new_details)
        db.session.commit()
        
        return redirect(url_for('details_list'))
        
    return render_template('details_add.html') 

@app.route('/details/list')
def details_list():
    
    all_details=Details.query.all()
    
    return render_template('details_list.html', Details = all_details)

@app.route('/details/edit/<int:id>',methods=['GET','POST'])

def details_edit(id):
    
    data=Details.query.get(id)
    
    if request.method =='POST' :
        
        data.name = request.form['name']
        data.role = request.form['role']
        
        db.session.commit()
        
        return redirect(url_for('details_list'))
        
    return render_template('details_edit.html',details=data)

@app.route('/details/delete/<int:id>')
def details_delete(id):
    
    data=Details.query.get(id)
    db.session.delete(data)
    db.session.commit()
    
    return redirect(url_for('details_list'))
        
if __name__ == '__main__':
    app.run(debug=True) 