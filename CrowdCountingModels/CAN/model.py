from CrowdCountingModels.VGG16 import extract_features
import keras


def can_prediction(features):
    model = keras.models.load_model('CrowdCountingModels/CAN/can_model.h5')
    pred = model.predict(features)
    return int(pred[0][0])
