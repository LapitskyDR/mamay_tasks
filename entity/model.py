import keras
from keras import layers


class Model:
    def __init__(self, input_shape = 10, encoding_size=32, output_shape=4):
        input_layer = keras.Input(shape=(input_shape,))
        encoded = layers.Dense(encoding_size, activation='relu')(input_layer)
        decoded = layers.Dense(output_shape, activation='relu')(encoded)
        self.autoencoder = keras.Model(input_layer, decoded)
        self.encoder = keras.Model(input_layer, encoded)
        encoded_input = keras.Input(shape=(encoding_size,))
        decoder_layer = self.autoencoder.layers[-1]
        self.decoder = keras.Model(encoded_input, decoder_layer(encoded_input))
        self.autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

    def fit(self):


    def predict(self):
