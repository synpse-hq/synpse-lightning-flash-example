from flash.image import ImageClassifier

model = ImageClassifier.load_from_checkpoint("./image_classification_model.pt")
model.serve(host="0.0.0.0")