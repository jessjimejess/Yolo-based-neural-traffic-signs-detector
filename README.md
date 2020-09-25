# Yolo based traffic signs detector
Deep Learning RT traffic signs detector system based on Yolov3. Model trained with RTSD, GTSDB & LISA datasets (94% accuracy). This project uses a RPi as client which send images to a server, which have implemented the neural network.

This projects also uses OpenCV dnn module for network implementation.

![Alt Text](https://media.giphy.com/media/ghXHvvnygVUj3sspsN/giphy.gif)




Full example:
https://www.youtube.com/watch?v=z-ftn4ORei0




Client-Server communication: detection/server.py
Detection functions: detection/detector.py
Datasets Scripts: datasets_scripts
Training chart script: training/draw_chart.py
