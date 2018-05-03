import keras

def pred(x_test):
    model = keras.models.load_model('ambient_code')
    
    predictions = model.predict([x_test])
    print (predictions)
    return predictions

if __name__ == "__main__":
	test_value = int(input("Give a value..."))
	pred(test_value)