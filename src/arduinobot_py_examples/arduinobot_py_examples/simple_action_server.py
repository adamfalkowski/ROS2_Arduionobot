import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from arduinobot_messages.action import Fibonacci
import time

class SimpleActionServer(Node):
    def __init__(self):
        super().__init__("simple_action_server")
        # Event driven execution- you set up the action server in the init method; essentially whenever you need to "set" something up you should do it in the constructor method
         #pass the function as reference instead of executing the function right now; callback wil be called later
        self.action_server = ActionServer(self, Fibonacci, "fibonacci", self.goalCallback)
        self.get_logger().info("Started the action server")

    # The goal handle represent the specific goal request by the action client
    # The goal handle is an object of type ServerGoalHandle, which has several methods it can access like abort or succeed
    def goalCallback(self, goal_handle):
        self.get_logger().info(f"received goal request with order {goal_handle.request.order}")
        # Due to the ROS IDL (interface generation system) there are som build in methods on the action interface, Feedback() being one of them
        # Feedback is like on the interface types (a bit like an underlying interface of the action interface), the action file itself just defined the strucure of the interface 
        feedback_msg = Fibonacci.Feedback()
        feedback_msg.partial_sequence = [0,1]

        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequence.append(feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1] )
            self.get_logger().info(f"Feedback: {feedback_msg.partial_sequence}")
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        # Marks the action as complete 
        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = feedback_msg.partial_sequence
        return result
    
def main():
    rclpy.init()
    simple_action_server = SimpleActionServer()
    rclpy.spin(simple_action_server)
    simple_action_server.destroy_node(simple_action_server)
    rclpy.shutdown()

if __name__ == "__main__":
    main()