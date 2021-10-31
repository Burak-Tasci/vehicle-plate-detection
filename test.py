import matplotlib.pyplot as plt
from detecto.utils import read_image
from detecto.visualize import show_labeled_image
from detecto.core import Model
from PIL import Image
import glob

def plot_test_image(img, model):

    labels, boxes, scores = model.predict(img)
    
    print(labels)
    print(boxes)
    print(scores)
    
    show_labeled_image(img,boxes,labels)

def threshold(labels, boxes, scores, threshold=0.75):
    
    indexes = []
    
    for s in scores:
        if s > threshold:
            index = scores.index(s)
            indexes.append(index)
            
    labels = [labels[x] for x in indexes]
    boxes  = [boxes [x] for x in indexes]
    scores = [scores[x] for x in indexes]
    
    return labels, boxes, scores



model = Model.load('model.pth', ['licence'])

for test in glob.glob("./test/*.png") + \
            glob.glob("./test/*.jpg") + \
            glob.glob("./test/*.jpeg"):
    test_image = Image.open(test)
    plot_test_image(test_image, model)














