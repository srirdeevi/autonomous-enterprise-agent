class Evaluator:


    def evaluate(
            self,
            request,
            results
    ):


        feedback = []


        # Check employee information

        if "pto" in request.lower():

            if "employee" not in results:

                feedback.append(
                    "Missing employee information"
                )



        # Check policy information

        if "policy" in request.lower():

            if "rag" not in results:

                feedback.append(
                    "Missing policy information"
                )



        # Check summary

        if "summary" not in results:

            feedback.append(
                "Missing final summary"
            )



        if len(feedback) == 0:

            return {
                "status": "PASS",
                "feedback": "Response is complete"
            }


        return {

            "status": "FAIL",

            "feedback": feedback

        }
