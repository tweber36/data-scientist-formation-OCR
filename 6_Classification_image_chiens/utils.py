import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix


def load_images(path, n_breeds=2, std_size=(100, 100)):
    images = []
    labels = []
    for idx, breed in enumerate(os.listdir(path)[:n_breeds]):
        for image in os.listdir(path + breed):
            img_orig = cv2.imread(path + breed + "/" + image)
            img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY) 
            img = cv2.resize(img, std_size)
            images.append(img)
            labels.append(breed.split("-")[1])
        print(
            f"Loaded {idx + 1}/{n_breeds}: {len(os.listdir(path + breed))} "
            f"images for breed: {breed.split('-')[1]}"
        )
    return images, labels


def extract_features(generator, feature_size, batch_size, n_classes, model=None):
    features = np.zeros(shape=(generator.n, feature_size[0], feature_size[1], feature_size[2]))
    if n_classes > 2:
        labels = np.zeros(shape=(generator.n, n_classes))
    else: 
        labels = np.zeros(shape=(generator.n))
    i = 0 
    for inputs_batch, labels_batch in generator:
        if model:
            features_batch = model.predict(inputs_batch)
        else:
            features_batch = inputs_batch
        if generator.batch_index != 0:
            features[i * batch_size : (i + 1) * batch_size] = features_batch
            labels[i * batch_size : (i+ 1) * batch_size] = labels_batch
        elif generator.batch_index == 0:
            features[i * batch_size:] = features_batch
            labels[i * batch_size:] = labels_batch
        i += 1
        if i * batch_size >= generator.n:
            break
    return features, labels


def plot_confusion_matrix(
    y_true, y_pred, classes, normalize=False, title=None, cmap=plt.cm.Blues
):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = "Normalized confusion matrix"
        else:
            title = "Confusion matrix"

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation="nearest", cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(
        xticks=np.arange(cm.shape[1]),
        yticks=np.arange(cm.shape[0]),
        # ... and label them with the respective list entries
        xticklabels=classes,
        yticklabels=classes,
        title=title,
        ylabel="True label",
        xlabel="Predicted label",
    )

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = ".2f" if normalize else "d"
    thresh = cm.max() * 0.75
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(
                j,
                i,
                format(cm[i, j], fmt),
                ha="center",
                va="center",
                color="white" if cm[i, j] > thresh else "black",
            )
    fig.tight_layout()
    return ax


def plot_accuracy_and_loss(history):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs[0].plot(history.history["acc"], label="Training accuracy")
    axs[0].plot(history.history["val_acc"], label="Validation accuracy")
    axs[0].set_title("Training and validation accuracy")
    axs[0].legend()

    axs[1].plot(history.history["loss"], label="Training loss")
    axs[1].plot(history.history["val_loss"], label="Validation loss")
    axs[1].set_title("Training and validation loss")
    axs[1].legend()

    plt.show()


def smooth_curve(points, factor=0.8):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            smoothed_points.append(point)
    return smoothed_points


def plot_smoothed_acc_and_loss(history, factor=0.8):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs[0].plot(
        smooth_curve(history.history["acc"], factor=factor), label="Training accuracy"
    )
    axs[0].plot(
        smooth_curve(history.history["val_acc"], factor=factor),
        label="Validation accuracy",
    )
    axs[0].set_title("Smoothed training and validation accuracy")
    axs[0].legend()

    axs[1].plot(
        smooth_curve(history.history["loss"], factor=factor), label="Training loss"
    )
    axs[1].plot(
        smooth_curve(history.history["val_loss"], factor=factor),
        label="Validation loss",
    )
    axs[1].set_title("Smoothed training and validation loss")
    axs[1].legend()

    plt.show()
