from flask import Flask, jsonify, request
from uuid import uuid4
from flask_cors import CORS
# hello
app = Flask(__name__)
CORS(app)
persons = []

@app.route('/persons', methods=['GET'])
def get_persons():
     return jsonify(persons)
   
@app.route('/persons', methods=['POST'])
def create_persons():
      data = request.get_json()
      person = {
          'id': str(uuid4()),
          'name': data['name'],
          'age': data['age'],
          'gender': data['gender'],
          'email': data['email']
}
      persons.append(person)
      return jsonify(person)

 

       
@app.route('/persons/<string:id>' ,methods=['GET'])
def get_person(id):
      person =next((person for person in persons if person['id'] == id), None)
      if person:
       return jsonify (person)
      else:
       return jsonify({'error': 'Person not found' })
      
      
# Endpoint to update a specific person object by ID
@app.route('/persons/<string:id>', methods=['PUT'])
def update_person(id):
    person = next((person for person in persons if person['id'] == id), None)
    if person:
        data = request.get_json()
        person.update(data)
        return jsonify(person)
    else:
        return jsonify({'error': 'Person not found'})


@app.route('/persons/<string:id>', methods=[ 'DELETE' ]) 
def delete_person(id) :
      global persons
      persons = [person for person in persons if person['id'] != id]
      return jsonify({'result': True})
if __name__ == '__main__':
 app.run (debug=True, host='0.0.0.0')
