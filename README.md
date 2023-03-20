# BLIP: A Bayesian Belief Network For Generating A Robot's Facial Expression In ROS

![Alt text](/images/diagram.jpg "BLIP Diagram")

# AUTHORS
Henry Ndubuaku\
ndubuakuhenry@gmail.com

# REQUIREMENTS
Catkin with RosPy and Bayesian packages installed.

# USAGE

![Alt text](/images/demo.mp4 "BLIP Demo")

*Move the inner blip folder to your catkin_ws workspace src folder

*Return to the catkin_ws directory using 'cd ..'

*Build the catkin workspace by running "catkin_make" in the directory

*Source with the code ". ~/catkin_ws/devel/setup.bash"

*Make the scripts executable by running the following codes in the scripts directory:
   chmod +x interaction_generator.py
   chmod +x perception_filter.py
   chmod +x robot_controller.py
   chmod +x robot_expression_prediction.py

*Run the launch file using "roslaunch blip human_robot_interaction.launch"
