import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.applications import VGG16


def _build_vgg_backbone_classifier(num_classes):
    inputs = tf.keras.Input(shape=(224, 224, 3))
    base_model = VGG16(include_top=False, input_tensor=inputs, weights='imagenet')
    base_model.trainable = True

    x = layers.Flatten()(base_model.output)
    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(num_classes, activation='softmax')(x)

    model = tf.keras.Model(inputs, outputs)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def build_vit_model(num_classes):
    # Placeholder implementation retained for compatibility with existing code.
    return _build_vgg_backbone_classifier(num_classes)


def build_cvt_model(num_classes):
    # Placeholder implementation retained for compatibility with existing code.
    return _build_vgg_backbone_classifier(num_classes)
