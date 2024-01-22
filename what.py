from keras.preprocessing.image import ImageDataGenerator

# train data 전처리 옵션 설정
train_datagen = ImageDataGenerator(rescale = 1./255, # 정규화
									# 이미지 증강
                                   rotation_range = 40,
                                   width_shift_range = 0.2,
                                   height_shift_range = 0.2,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip=True,
                                   vertical_flip = True,
                                   fill_mode = 'nearest')