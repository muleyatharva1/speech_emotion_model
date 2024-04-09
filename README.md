This Github repsotory gives you demonstration of speech emotion recognition system build using Support Vector Machine algorithm in Machine Learning. RAVDESS dataset was used for training this model.
the trained model was tested on raspberry pi 3 model B. 
To run this project on raspberry pi, we need to follow some steps:
1. Connect raspberry pi with your PC and open RealVNC monitor(or any virtual monitor) on which you need to check the output
2. Enter the I.P address set up in the monitor and open the virtal monitor titled with the new established I.P address
3. Download all files from repository and necessar libraries into your system
4. Dump the file named "ml_hardware.py" and "emotion_svm.pkl" in your raspberry pi. Pkl file consist of trained model and py file is the code you nedd to run
5. Connect a USB or bluetooth microphone with raspberry pi
6. Open terminal in the monitor and change the directory to the folder where .py and .pkl files are added
7. enter the command "python file_name" and the code will start to execute
8. "Recording" message will pop up on the terminal. Give voice input to the microphone within 5 seconds
9. "Recoding finished" will now get displayed notifying that the recording is finished
10. After some time, estimated emotion of your voice will be diaplyed on the screen

