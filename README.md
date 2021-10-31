# Vehicle Plate Detection
In this repository, i am detecting vehicle plates with detecto which is using pytorch and fasterrcnn_resnet50_fpn.

## Dataset

I combined these two datasets, you can reach it below:<br>
- <a href="https://www.kaggle.com/andrewmvd/car-plate-detection">andrewmvd's car-plate-detection</a><br>
- <a href="https://www.kaggle.com/achrafkhazri/labeled-licence-plates-dataset">achrafkhazri's labeled-licence-plates-dataset</a><br>

## Setup

I wrote 2 different commands to preparing environment with conda and pip<br>
- `conda env update -n [ENVIRONMENT_NAME] --file vplate.yaml`
- `pip install -r requirements.txt`
PS: I recommend to use pip, because detecto has better compatibility in pip version.
