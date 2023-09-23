import matplotlib.pyplot as plt


def show_prediction():
    plt.figure(figsize=(16, 8))
    plt.title('Model')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD($)', fontsize=18)
    plt.plot(train['Close'])
    plt.plot(valid['Close'])
    plt.plot(valid['Predictions'])
    plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
    plt.show()
