import rclpy
from rclpy.node import Node
from arduinobot_messages.srv import AddTwoInts
import sys


class SimpleServiceClient(Node):
    def __init__(self, a, b):
        super().__init__("simple_service_client")

        # Allows us to send requests to the server; you declare service client with create_client method that comes from rclpy.client.Client
        self.client_ = self.create_client(AddTwoInts, "add_two_ints")

        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service Not Available , waiting more...")
        
        self.req_ = AddTwoInts.Request()
        self.req_.a = a
        self.req_.b = b
        # Future is a ROS2 wrapper for handling async calls; we dont know when the call will be completed so we call it future
        self.future_ = self.client_.call_async(self.req_)
        self.future_.add_done_callback(self.responseCallback)

    # This method gets called when the future has something
    def responseCallback(self, future):
        self.get_logger().info(f"Service Response {future.result().sum }")

    

def main():
    rclpy.init()
    # Name of the script is always sys.argv[0], thats why you need lenght 3 for the input user arguments
    if len(sys.argv) != 3:
        print("Wrong number of arguments! Usage is simple_service_client A B")
        return -1
    
    simple_service_client = SimpleServiceClient(int(sys.argv[1]), int(sys.argv[2]))
    # Keep the client node running
    rclpy.spin(simple_service_client)
    # If CTRL+C then destroy the node and turn off ROS2
    simple_service_client.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

        