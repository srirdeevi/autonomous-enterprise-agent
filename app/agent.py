from planner import Planner
from tools import ToolExecutor
from memory import Memory
from evaluator import Evaluator
from retry_manager import RetryManager


class Agent:


    def __init__(self):

        self.memory = Memory()

        self.planner = Planner()

        self.executor = ToolExecutor()
        self.evaluator = Evaluator()
        self.retry_manager = RetryManager()



    def run(self, request):


        # Store user request

        self.memory.add(
            "user",
            request
        )


        # Create execution plan

        plan = self.planner.create_plan(
            request
        )


        print("\nExecution Plan")
        print("-" * 50)


        for step in plan:

            print(
                step["tool"],
                "-",
                step["description"]
            )



        # Execute tools

        attempt = 1


        while True:


            results = self.executor.execute(plan)


            evaluation = self.evaluator.evaluate(
                request,
                results
            )


            if not self.retry_manager.should_retry(
                    evaluation,
                    attempt
            ):

                break


            print(
                "Evaluation failed. Retrying..."
            )


            attempt += 1

        results["evaluation"] = evaluation


        # Store response

        self.memory.add(
            "agent",
            str(results)
        )


        return results
