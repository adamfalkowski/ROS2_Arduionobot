import rclpy
from rclpy.node import Node
from arduinobot_messages.srv import AddTwoInts

class SimpleServiceServer(Node):
    def __init__(self):
        super().__init__("simple_service_server")

        # As a convention, message interfaces (types) are placed in a different package then where we developed the robots functionality
        # The service name "add_two_ints" will be used by the client to poll the server
        self.service_ = self.create_service(AddTwoInts, "add_two_ints", self.serviceCallback)
        self.get_logger().info("Service adding two ints is ready")

    def serviceCallback(self, req, res):
        self.get_logger().info(f"New msg received a: {req.a} b: {req.b}")
        res.sum = req.a + req.b 
        self.get_logger().info(f"Returning sum {res.sum}")
        return res
    
    
def main():
    rclpy.init()
    simple_service_server = SimpleServiceServer()
    rclpy.spin(simple_service_server)
    simple_service_server.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()


    
