class RetryManager:


    def should_retry(
            self,
            evaluation,
            attempt
    ):


        max_attempts = 2


        if attempt >= max_attempts:
            return False


        return (
                evaluation["status"]
                == "FAIL"
        )
