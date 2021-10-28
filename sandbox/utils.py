def getFeatures(path):
    image = face_recognition.load_image_file(path)
    face_features = face_recognition.face_encodings(image)
    if len(face_features):
        print(f'Features found on {file}')
        features = {}
        for i, feat in enumerate(face_features[0]):
            features[f'feat_{i}'] = feat
        return features
    return False