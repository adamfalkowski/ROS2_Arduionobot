import rclpy # allows you to used the ROS2 functionlity in this script
from rclpy.node import Node
from rclpy.action import ActionClient
from arduinobot_messages.action import Fibonacci

class SimpleActionClient(Node):
    def __init__(self):
        super().__init__('simple_action_client')

        self.action_client = ActionClient(self, Fibonacci, "fibonacci")

        # Wait for the action server to be available with the name fibonacci and the right type of interface
        self.action_client.wait_for_server()

        self.goal = Fibonacci.Goal()
        self.goal.order = 10
        # When we send a goal we also get feedback which will be stores in a future - the future will eventually hold the goal handle
        self.future = self.action_client.send_goal_async(self.goal, feedback_callback= self.feedbackCallback)
        # Callback to call when the action either completes or is stopped (accepted or rejected)
        self.future.add_done_callback(self.responseCallback)

    # Executed after the goal is sent and check if it was accepted or not
    def responseCallback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected")
            return 
        
        self.get_logger().info("Goal accepted")
        self.future = goal_handle.get_result_async()
        self.future.add_done_callback(self.resultCallback)

        # goal_handle.feedback_callback = self.feedbackCallback

    # Executed at the end of the action server execution 
    def resultCallback(self, future):
        result = future.result().result
        self.get_logger().info(f"Result: {format(result.sequence)}")
        rclpy.shutdown()

    # Executed repeatetidly whenever we receive some feedback from the action server
    def feedbackCallback(self, feedback_msg):
        # Print the contents of the action feedback
        self.get_logger().info(f"received feedback: {format(feedback_msg.feedback.partial_sequence)}")


def main():
    rclpy.init()
    simple_action_client = SimpleActionClient()
    rclpy.spin(simple_action_client)


if __name__ == "__main__":
    main()
    