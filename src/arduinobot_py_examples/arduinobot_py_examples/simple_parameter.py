import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult # Need to add this library to the package.xml as an external dependency
from rclpy.parameter import Parameter


class SimpleParamter(Node):
    def __init__(self):
        super().__init__("simple_parameter")
        # Method inherited from the parent class Node; used to initialize and declare a paramter for this node (when it starts up)
        self.declare_parameter("simple_int_param",28)
        self.declare_parameter("simple_string_param", "Antonio") 

        # Call back when one or more params that we declared have been changed during runtime
        self.add_on_set_parameters_callback(self.paramChangeCallback)

    def paramChangeCallback(self, params):
        result = SetParametersResult() 
        
        for param in params:
            if param.name == "simple_int_param" and param.type == Parameter.Type.INTEGER:
                self.get_logger().info("INT param changed, new value is %d" % param.value)
                result.successful == True

            if param.name == "simple_string_param" and param.type == Parameter.Type.STRING:
                self.get_logger().info("STRING param changed, new value is %d" % param.value)
                result.successful == True

        return result 
    
def main():
    rclpy.init()
    simple_parameter = SimpleParamter()
    rclpy.spin(simple_parameter)
    simple_parameter.destroy_node()
    rclpy.shutdown()

    
if __name__ == '__main__':
    main()