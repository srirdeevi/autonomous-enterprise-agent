import requests


class ToolExecutor:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"

    def execute(self, plan):

        results = {}

        for step in plan:

            tool = step["tool"]

            if tool == "employee":

                results["employee"] = (
                    "John has 12 PTO days remaining."
                )

            elif tool == "ticket":

                results["ticket"] = (
                    "No open tickets."
                )

            elif tool == "rag":

                response = requests.get(
                    f"{self.base_url}/search",
                    params={
                        "question": "What is the company remote work policy?"
                    }
                )

                # results["rag"] = response.json()["answer"]
            elif tool == "summary":

                 results["summary"] = self.create_summary(results)

        return results

    def create_summary(self, results):

        summary = "Employee Report\n\n"

        if "employee" in results:
            summary += (
                    "Employee Information:\n"
                    + results["employee"]
                    + "\n\n"
            )


        if "rag" in results:
            summary += (
                    "Company Policy:\n"
                    + results["rag"]
            )


        return summary
