from flask import Flask, render_template, request
from keras.models import load_model
from PIL import Image
import tensorflow as tf
import numpy as np

# create an app object using Flask class.
app = Flask(__name__)

# load the trained deep learning model.
best_model = load_model('model_regnet_Binary_balanced_new_dropout.h5')

# getting a prediction by passing image to the model.
def predict_label(img_path):
	imaget = Image.open(img_path)
	imaget = imaget.resize((112, 112))
	x_train_mean = 156.96441011306865
	x_train_std = 46.79450254580003
	img_array = tf.keras.utils.img_to_array(imaget)
	img_batch = np.expand_dims(img_array, axis=0)
	img_batch = (img_batch - x_train_mean)/x_train_std
	return best_model.predict(img_batch)


# utilizing route decorator to trigger the home page.
@app.route("/", methods = ['GET', 'POST'])
def home():
	show_result = False
	return render_template("index.html", show_result = show_result)


# form handling and result.
@app.route("/result", methods = ['GET', 'POST'])
def run_model():
	show_result = True
	if request.method == 'POST':
		img = request.files['test_img']
		img_path = "static/imgs/" + img.filename	
		img.save(img_path)

		prediction = predict_label(img_path)
		if prediction[0][0] > 0.5:
			result_type = "Benign"
			confidence_rate = int((prediction[0][0]*100) * 10 **2) / 10 ** 2
		else:
			result_type = "Malignant"
			confidence_rate = int((prediction[0][1]*100) * 10 **2) / 10 ** 2
		return render_template("index.html", img_path = img_path, type = result_type, confidence = confidence_rate, show_result = show_result)


# run the app object.
if __name__ == "__main__" :
    app.run()
