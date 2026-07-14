# from planner import Planner
# from tools import ToolExecutor
# from memory import Memory
#
#
# def main():
#
#     planner = Planner()
#
#     request = (
#         "Prepare a report about John's PTO and the company remote work policy."
#     )
#
#     plan = planner.create_plan(request)
#     executor = ToolExecutor()
#     results = executor.execute(plan)
#     memory = Memory()
#
#     memory.add(
#         "user",
#         request
#     )
#     memory.add(
#         "agent",
#         str(results)
#     )
#
#     print("\nUser Request:")
#     print(request)
#
#     print("\nExecution Plan:")
#     print("-" * 50)
#
#     print("\nTool Results")
#     print("-" * 50)
#
#     print("\nConversation Memory")
#     print("-" * 50)
#
#     print(memory.get_history())
#
#     for index, step in enumerate(plan, start=1):
#         print(f"{index}. {step['tool']}")
#         print(f"   {step['description']}")
#
#     for key, value in results.items():
#         print(f"\n{key.upper()}")
#         print(value)
#
#
# if __name__ == "__main__":
#     main()
from agent import Agent



def main():


    agent = Agent()


    request = (
        "Prepare a report about John's PTO "
        "and the company remote work policy."
    )


    response = agent.run(
        request
    )


    print("\nFinal Response")
    print("-" * 50)


    for key, value in response.items():

        print(
            f"\n{key.upper()}"
        )

        print(value)



if __name__ == "__main__":

    main()

