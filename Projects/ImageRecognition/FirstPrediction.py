from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath( execution_path + "\resnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.loadModel()


predictions =  prediction.predictImage(r"C:\Users\Personal\Downloads\sample.jpg", result_count=5)
percentage_probabilities = prediction.predictImage(r"C:\Users\Personal\Downloads\sample.jpg", result_count=5)
for index in range(len(predictions)):
    print(predictions[index] , " : " , percentage_probabilities[index])