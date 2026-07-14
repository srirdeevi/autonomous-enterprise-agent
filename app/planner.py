import json

from llm import LLM
from prompts import PLANNER_PROMPT


class Planner:

    def __init__(self):
        self.llm = LLM()


    def create_plan(self, request):

        prompt = PLANNER_PROMPT.format(
            request=request
        )

        response = self.llm.generate(prompt)

        print("\nPlanner Decision:")
        print(response)


        try:
            data = json.loads(response)

            return self.convert_plan(data)


        except Exception:

            print(
                "LLM failed structured output. "
                "Using fallback planner."
            )

            return self.fallback_plan(request)



    def convert_plan(self, data):

        tasks = data.get(
            "tasks",
            []
        )


        descriptions = {

            "employee":
                "Retrieve employee information",

            "rag":
                "Search company knowledge base",

            "ticket":
                "Retrieve ticket information",

            "summary":
                "Generate final summary"

        }


        return [

            {
                "tool": task,
                "description": descriptions.get(
                    task,
                    "Execute tool"
                )
            }

            for task in tasks

        ]



    def fallback_plan(self, request):

        request = request.lower()

        plan = []


        if (
                "pto" in request
                or "john" in request
                or "employee" in request
        ):

            plan.append(
                {
                    "tool": "employee",
                    "description":
                        "Retrieve employee information"
                }
            )



        if (
                "policy" in request
                or "remote" in request
                or "company" in request
        ):

            plan.append(
                {
                    "tool": "rag",
                    "description":
                        "Search company knowledge base"
                }
            )



        if (
                "report" in request
                or "summary" in request
        ):

            plan.append(
                {
                    "tool": "summary",
                    "description":
                        "Generate final summary"
                }
            )


        return plan
