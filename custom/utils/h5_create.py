import tensorflow as tf


#Defining a tf.keras.Model using Sequential API
#Use it only for single input and single output case

model = tf.keras.Sequential([tf.keras.layers.Dense(200, activation="relu", input_shape=(100,)),
                            tf.keras.layers.Dense(300, activation="relu")])

#Defining a tf.keras.Model using Functional API
#In this method we create layers and call it with appropriate input tensors to get layer outputs
#Can be used to create Model with multiple inputs and outputs

inputs = tf.keras.layers.Input(shape=(100,))
layer_1_out = tf.keras.layers.Dense(200, activation="relu")(inputs)
layer_2_out = tf.keras.layers.Dense(300, activation="relu")(layer_1_out)
layer_3_out = tf.keras.layers.Dense(400, activation="relu")(layer_2_out)
model = tf.keras.Model(inputs=[inputs], outputs=[layer_2_out, layer_3_out])


model.save("mymodel.h5")