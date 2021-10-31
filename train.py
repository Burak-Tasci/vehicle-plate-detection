import matplotlib.pyplot as plt
from detecto.utils import read_image
from detecto.core import Dataset
from detecto.visualize import show_labeled_image
from detecto.core import Model

    
train_path = "./train/"
val_path = "./val/"

rows = 5
cols = 5
axes=[]
fig=plt.figure(figsize=(15,15))
for a in range(rows*cols):
    sample_path = f"Cars{51+a}.png"
    img = read_image(train_path+sample_path)
    axes.append( fig.add_subplot(rows, cols, a+1) )
    plt.imshow(img) 
plt.show()


train_ds = Dataset(train_path)
val_ds = Dataset(val_path)


image, targets = train_ds[150]
show_labeled_image(image, targets["boxes"], targets["labels"])

labels = ["licence"]
model = Model(labels)

model.fit(train_ds,
          val_dataset=val_ds,
          epochs=5)

model.save('model.pth')




















