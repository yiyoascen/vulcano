from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
model = load_model('volcano_analysis.h5')
test_datagen = ImageDataGenerator(rescale=1. / 255)

test_generator = test_datagen.flow_from_directory(
    'test_images/',
    target_size=(255, 255),
    color_mode="rgb",
    shuffle=False,
    class_mode='binary',
    batch_size=1)

filenames = test_generator.filenames
nb_samples = len(filenames)

predict = model.predict_generator(test_generator, steps=nb_samples)
print(predict)
