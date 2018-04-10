# pythonspot.com
from flask import Flask, render_template, flash, request
import numpy as np
from flask_socketio import SocketIO, emit



# App config.
# DEBUG = True
app = Flask(__name__)
# app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

socketio = SocketIO(app)


@socketio.on('generate',namespace='/')
def generate(ret):
	print(ret)
	emit('myevent','started')
	from keras.models import load_model
	model = load_model('model.h5')
	chars = ['w', 'n', 'q', 'g', 'm', 'v', 'o', 'r', 'k', 's', 'p', 'x', 'h', 't', 'z', 'ï', 'í', 'a', 'é', 'º', 'l', ' ', 'y', 'd', 'ｔ', 'i', 'j', 'ｒ', 'c', 'ı', 'u', 'b', 'è', 'e', 'f', 'ĺ']
	seq_length = 140
	ix_to_char = {ix:char for ix, char in enumerate(chars)}
	char_to_ix = {char:ix for ix, char in enumerate(chars)}	
	VOCAB_SIZE = len(chars)
	ret = list(ret.lower())
	ret = [i for i in ret if i.isalpha() == True]
	ret = ret[:140]
	while len(ret)<140:
		ret = [" "] + ret
	X_sequence = ret
	y_char = []
	X_sequence_ix = [char_to_ix[value] for value in X_sequence]
	input_sequence = np.zeros((140, VOCAB_SIZE))
	for j in range(seq_length):
    		input_sequence[j][X_sequence_ix[j]] = 1
	X = np.append(input_sequence.reshape((1, 140, VOCAB_SIZE)), np.zeros((1, 140, VOCAB_SIZE)),axis =1)
	print(X.shape)
	ix = [char_to_ix[X_sequence[-1]]]
	for i in range(140,280):
        	X[0, i, :][ix[-1]] = 1
        	print(ix_to_char[ix[-1]], end="")
        	ix = np.argmax(model.predict(X[:, :i+1, :])[0], 1)
        	y_char.append(ix_to_char[ix[-1]])
	print("\n")
	ret = ('').join(y_char)
	print(ret)
	print(type(ret))
	socketio.emit('myevent',ret)
	return ret

#@socketio.on('generate',namespace='/')
def gh(message):
    print(message)
    emit('myevent','done')

@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template('hello.html')
 
if __name__ == "__main__":
    socketio.run(app,host='0.0.0.0',port = 8080)
