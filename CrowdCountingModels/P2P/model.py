from CrowdCountingModels.VGG16 import extract_features
import keras


def p2p_prediction(features):
    model = keras.models.load_model('CrowdCountingModels/P2P/p2p_model.h5')
    pred = model.predict(features)
    return int(pred[0][0])
