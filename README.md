# TEEN PATTI
## Detect Card And Classify Hands With YOLO

## About TEEN PATTI
Teen patti is a gambling card game originated in india and popular through south Asia. You can also learn about it and basic rules and ranks through [here.](https://en.wikipedia.org/wiki/Teen_patti)

## Training
The YOLOv8 model was trained on google colab using [this dataset.](https://universe.roboflow.com/augmented-startups/playing-cards-ow27d/dataset/3) for 50 epochs.

## Results
![Demo Video](demo.gif)


## Run Locally
### Clone the project
``` bash
git clone https://github.com/Ritushwar/teen_patti.git

```
### Go to project directory
``` bash
cd teen_patti
```
### Install dependencies
``` bash
pip install -r requirements.txt
```
### Start
```bash
detector.py
```