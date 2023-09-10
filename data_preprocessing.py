def train_val_test(data, label):
    #Split data into train,validate,test splits by season

    # features = ['Name', 'Age', 'other features']
    # x =  train.loc[:, features]
    # y = train.loc[:, ['Finalist']]

    train = data[data['Season'] <= 7]
    validate = data[data['Season'] == 8]
    test = data[data['Season'] == 9]

    x_train = train.drop(columns=[label])
    y_train = train[label]

    x_validate = validate.drop(columns=[label])
    y_validate = validate[label]

    x_test = test.drop(columns=[label])
    y_test = test[label]

    print('Train Split: ', x_train.shape, '| Validate Split: ', x_validate.shape, '| Test Split: ', x_test.shape)

    return x_train, y_train, x_validate, y_validate, x_test, y_test