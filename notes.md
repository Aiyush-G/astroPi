# Plan of Action

### Preprocessing
1. Crop Image to circle - remove the edges

___


## Stages
### First
1. Take an image and convert it to NDVI
2. Return what percentage of the image is life
3. Calculate the land coverage per image

### Second
---
1. Itterate over an existing dataset to create NDVI values
2. Split the images created in an array of numbers (1>10) that represent how "green" a pixel is, this can then be used in the predictive algorihtm. 

---
### Astro Pi Possible Measurements
Existing NDVI dataset: https://neo.gsfc.nasa.gov/view.php?datasetId=MOD_NDVI_M&year=2001

Location of Pi Given time: https://rhodesmill.org/skyfield/

- time	
- humidity	
- temperature	
- pressure	
- gyro_pitch	
- gyro_roll	
- gyro_yaw	
- accel_pitch	accel_roll	
- accel_yaw	
- accel_x	
- accel_y	
- accel_z	
- magnet_x	
- magnet_y	
- magnet_z	
- Lat_deg	
- lat_min	
- lat_sec	
- long_deg	
- long_min	
- long_sec

---
# Research and Further Notes

## Machine Learning


### Idea 1 - LSTMs

Using Keras for next frame video predictions, I will experiment with this method using a model based approach. The input will be a time generated NDVI and the output will be the next predicted frame - representing the next year given the previous data.
For this to work: 1. The images taken on the ISS need to be mapped onto a 360 degree world map / view 2. An existing dataset of highly detailed NDVI. 

Model based reinforcement learning, state action next frame pairs, used with convolutional LSTMs. 

Google colab of the animated minst: https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/ipynb/conv_lstm.ipynb#scrollTo=VCeXHV7RXAgy 

https://www.youtube.com/watch?v=P5yv8HDFc_M 

### Cons with this method
1. With a lack of understanding of how the model works, it becomes very hard to finetune. In addition, the dataset that we have access to is very limited which makes it more apealing to low-shot prediction models instead. The issue is, there aren't many around, we will probably have to build our own. 


### Idea - 2 - Regression
This is where we look at how a single variable X varies with values A, B, C. This would work quite well since there are many existing model. However, after further research I found that this would not be suitable due to a single variable comparison, ie [-0.1 - 1, where 999 is black]:

[Over 10 Years]
```
{   YR   Val
    [1, 0.1],
    [2, 0.1],
    [3, 0.2],
    [4, 0.3],
    [5, 0.2],
    [6, 0.4],
    [7, 0.4],
    [8, 0.5],
    [9, 0.2],
    [10, 0.4],
    
}
```
The variable that we are predicting is the Val of NDVI "green-ness" however, the only other variable that we can compare against is the time as a number, representing the year. 
Now, this causes issues, since the year has no direct correlation on the value. Ie. just because it is year [200]6 doen't mean that the NDVI value was 0.4 due to the year, it just happened to be coincidence at this pixel. Therefore, this method won't work since it requires correlation between variables.

### Idea - 3 - Timeseries
I'd never heard of timeseries before researching the regression modelling. It seems that timeseries allows us to predict the next value in a list given when that number was recorded. Ie. predicting the number of subscribers that a youtube channel has.

#### ➡️ Example Workflow - https://towardsdatascience.com/announcing-pycarets-new-time-series-module-b6e724d4636c 



