import rclpy # allows you to used the ROS2 functionlity in this script
from rclpy.node import Node
from std_msgs.msg import String

# Inherits the Node Class
class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__("simple_subscriber")
        self.sub = self.create_subscription(String, "chatter", self.msgCallback, 10)

    def msgCallback(self, msg):
        self.get_logger().info(f"I heard { msg.data} ")

def main():
    rclpy.init()
    simple_subscriber = SimpleSubscriber()
    # Keeps the node active and continiously processing incoming events
    rclpy.spin(simple_subscriber)
    # If you press CTRL+C then you will stop the spin and then you can destroy the node
    simple_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()



