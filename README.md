# BLIP: A Bayesian Belief Network For Generating A Robot's Facial Expression Based On Human Action.0

![Alt text](/images/diagram.jpg "BLIP Diagram")

# AUTHORS
Henry Ndubuaku\
ndubuakuhenry@gmail.com

# REQUIREMENTS
Catkin with RosPy and Bayesian packages installed.

# USAGE
https://user-images.githubusercontent.com/26547576/226372870-314827f3-4643-4dcc-89df-8b84097364a7.mp4

1. Move the inner blip folder to your catkin_ws workspace src folder

2. Return to the catkin_ws directory using 'cd ..'

3. Build the catkin workspace by running "catkin_make" in the directory

4. Source with the code ". ~/catkin_ws/devel/setup.bash"

5. Make the scripts executable by running the following codes in the scripts directory:
   1. chmod +x interaction_generator.py
   2. chmod +x perception_filter.py
   3. chmod +x robot_controller.py
   4. chmod +x robot_expression_prediction.py

6. Run the launch file using "roslaunch blip blip.launch"
