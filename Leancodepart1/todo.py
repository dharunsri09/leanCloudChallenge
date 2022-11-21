import datetime
from flask import Flask,Blueprint
from flask_restplus import Resource, Api,fields,apidoc
from werkzeug.utils import cached_property

app = Flask(__name__)
l=str(datetime.datetime.today()).split()[0]

blueprint = Blueprint('api',__name__,url_prefix='/api')
api = Api(blueprint,doc='/documentation')
api = Api(app, version='1.0', title='   TODOS IN YOUR WORK',
    description='Tell your task',
)
app.register_blueprint(blueprint)
a_todo=api.model('TASKS',{'task':fields.String('The task.'),'Due_time':fields.String('the due_time')})

@api.route('/my-resource/<id>')
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):
    def get(self, id):
        return {}

    @api.response(403, 'Not Authorized')
    def post(self, id):
        api.abort(403)

todo=[]

todo.append({'task':'Create a method','id':1,'Due_time':'2022-11-20'})

@api.documentation
def custom_ui():
    return apidoc.ui_for(api)

@api.route('/due')
class Todo(Resource):
    @api.marshal_with(a_todo)
    def get(self):
        return todo
    @api.expect(a_todo)
    def post(self):
        new_todo=api.payload
        new_todo['id']=len(todo)+1
        todo.append(new_todo)
        return {'task':'Task added'}, 201

tim="Due completed"
@api.route('/overtime')
class Todo(Resource):
    def get(self):
        return tim
    
@api.route('/finished')
class Todo(Resource):
    @api.marshal_with(a_todo)
    def get(self):
        return todo


if __name__ == '__main__':
    app.run(debug=True)
