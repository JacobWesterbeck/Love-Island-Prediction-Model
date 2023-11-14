def train_val_test(data, label):

    train_szn = [1, 2, 3, 4, 5, 6, 7]
    validate_szn = 8
    test_szn = 9


    train = data[data['Season'].isin(train_szn)]
    validate = data[data['Season'] == validate_szn]
    test = data[data['Season'] == test_szn]

    x_train = train.drop(columns=[label])
    y_train = train[label]

    x_validate = validate.drop(columns=[label])
    y_validate = validate[label]

    x_test = test.drop(columns=[label])
    y_test = test[label]

    print('Train Split: ', x_train.shape, '| Validate Split: ', x_validate.shape, '| Test Split: ', x_test.shape)

    return x_train, y_train, x_validate, y_validate, x_test, y_test