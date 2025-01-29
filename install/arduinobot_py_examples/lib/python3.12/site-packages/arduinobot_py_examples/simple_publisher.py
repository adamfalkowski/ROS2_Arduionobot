import rclpy #allows you to use ROS fuctionalities in our script
from rclpy.node import Node 
from std_msgs.msg import String

# Inherit from parent class Node
class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher") 
        # Create a publisher within a ROS Node; 
        # allows to send a message to a given topic
        self.pub_ = self.create_publisher(String, "chatter", 10 ) 
        self.counter_ = 0
        self.frequency_ = 1.0
        self.get_logger().info(f"publishing at {self.frequency_} Hz")
        self.timer_ = self.create_timer(self.frequency_, self.timerCallback)

    def timerCallback(self):
        msg = String() # Create an instance of the String method. 
        # The scope of this instance will be in this method.  
        # The instance will be destroyed once the method is done
        msg.data = f"Hello ROS2 - counter {self.counter_}"
        self.pub_.publish(msg)
        self.counter_ += 1

def main():
   rclpy.init()
   simple_publisher = SimplePublisher()
   rclpy.spin(simple_publisher) 
   simple_publisher.destroy_node()
   rclpy.shutdown()



if __name__ == '__main__':
    main()
