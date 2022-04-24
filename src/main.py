
import sys
import tensorflow as tf

from tensorflow import keras

if __name__ == "__main__":
    print('args: '+str(sys.argv))
    tf.keras.models.load_model('dnn_model')

    if len(sys.argv) == 1:
        print('NO XLS PATH PROVIDED')
    else:
        xls_path = str(sys.argv[1])
        



