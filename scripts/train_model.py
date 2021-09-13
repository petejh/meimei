import os
from datetime import timedelta
from time import time

import deepen
import h5py as h5
import numpy as np

def main():
    data_spec = {
        'datafile': '../meimei/data/data.h5',
        'x_name': 'data_x',
        'y_name': 'data_y',
        'class_name': 'data_class'
    }

    # load data
    here = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(here, data_spec['datafile'])
    with h5.File(data_path, 'r') as f:
        data_x = f[data_spec['x_name']][:]
        data_y = f[data_spec['y_name']][:]
        data_label = f[data_spec['class_name']][:]

    # normalize data
    norm_x = data_x.reshape(data_x.shape[0], -1).T / 255
    norm_y = data_y.reshape(1, data_y.shape[0])

    # partition data
    test_frac = 0.193
    test_cases = int(norm_x.shape[1] * test_frac + 0.5)
    test_index = norm_x.shape[1] - test_cases

    train_x = norm_x[:, 0:test_index]
    train_y = norm_y[:, 0:test_index]
    test_x = norm_x[:, test_index:]
    test_y = norm_y[:, test_index:]

    # sanity checks
    # assume 259 labelled examples of 64px by 64px RGB images (64*64*3 == 12288)
    assert(train_x.shape == (12288, 209))
    assert(train_y.shape == (1, 209))
    assert(test_x.shape == (12288, 50))
    assert(test_y.shape == (1, 50))

    # define model
    classifier = deepen.Model(layer_dims=[12288, 20, 7, 5, 1])

    # train model
    np.random.seed(1)
    print("Training model...", end='')
    start = time()
    progress = classifier.learn(train_x, train_y, iterations=2500)
    end = time()
    print("done.")
    print("Time to train: %s" %  str(timedelta(seconds=(end - start))))

    for i, (params, cost) in enumerate(progress):
        if i % 100 == 0:
            print("Cost at iteration %i: %f" % (i, cost))

    train_pred = classifier.predict(train_x)
    train_accuracy = np.sum(train_pred == train_y) / train_y.shape[1]
    print("Training accuracy: %3.3f" % train_accuracy)

    # test model
    test_pred = classifier.predict(test_x)
    test_accuracy = np.sum(test_pred == test_y) / test_y.shape[1]
    print("Test accuracy: %3.3f" % test_accuracy)

    # save model
    save_path = os.path.join(here, '../meimei/models/model.h5')
    classifier.save(save_path)

if __name__ == '__main__':
    main()
