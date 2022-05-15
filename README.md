# pogdotearth-bot WIP
The bot consist out of 2 parts, the part of detecting touches of grass and the interaction with twitter.

## How to let a computer know that you are touching grass?
We aproch this problem in muliple layers of questions. Just like you do with data and multiple if statments. Here is the design and what testing needs to be done to get the most accurate results.
The need of multiple steps is to minimise errors and have it accurate as possible.

### 1\# Detecting the presents of a hand. And get a croped version. 
I would test 2 methods to detect if a hand in the picture.

1. DIY with OpenCV and just some math.
2. With the Hands model from mediapipe a cross-platfrom customizable ML solutions.

Then we procede with a croped image for further analysis.
(Reducing not necessary data.)

### 2\# Is there even someting "grassy" to begin with.
This is a simple process where we are going to check if there is grass to find on a color perspective?
So at what colors are we searching for. Mainly green, but you have to know that not all grass ist just plain green, there are exeptions when the grass is realy dried out.

To specify we are looking for are range of colors.
![Image of a Color Wheel Chart from https://www.allbusinesstemplates.com/es/template/TE8VS/printable-color-wheel-chart/](/images/docs/color-wheel-chart.png)

To be precise from Orange-red to Green.

There are many ways to check if a color is present in a picture. => 

to read through: 
https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image#:~:text=Python%20Imaging%20Library%20has%20method%20getcolors%20on%20Image,that%20and%20see%20if%20it%20performs%20any%20better.
https://www.alanzucconi.com/2015/05/24/how-to-find-the-main-colours-in-an-image/
https://stackoverflow.com/questions/2270874/image-color-detection-using-python
https://stackoverflow.com/questions/7772510/main-color-detection-in-python

### 3\# Run a machine learning model on it.
This part is going to get only the green parts of the second method. And gets ran through an self trained model that decides if the green stuff is actually comparable of grass.

the take on this one is maybe just train it with a black and white image of outlines from detail pictures, beacuse then the model can focus on the structual parts. (Allways lines orientet in straight lines, maybe some flower looking things)
But this needs to get benchmarked with a couple of versions.
