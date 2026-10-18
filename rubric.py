
# Evaluation rubric for financial analysis

EVALUATION_RUBRIC = {
    "factual_accuracy": {
        "max_score": 30,
        "description": (
            "Check whether financial claims are supported "
            "by the provided data and evidence."
        )
    },
    "completeness": {
        "max_score": 20,
        "description": (
            "Check whether the analysis covers the "
            "relevant financial information."
        )
    },
    "risk_assessment": {
        "max_score": 20,
        "description": (
            "Check whether risks and uncertainties "
            "are clearly discussed."
        )
    },
    "clarity": {
        "max_score": 15,
        "description": (
            "Check whether the analysis is clear, "
            "organized, and understandable."
        )
    },
    "relevance": {
        "max_score": 15,
        "description": (
            "Check whether the analysis addresses "
            "the requested stock and task."
        )
    }
}

PASS_THRESHOLD = 80
MAX_REVISIONS = 2


def get_max_score():
    return sum(
        item["max_score"]
        for item in EVALUATION_RUBRIC.values()
    )


if __name__ == "__main__":
    print("Maximum score:", get_max_score())
    print("Passing threshold:", PASS_THRESHOLD)
    print("Maximum revisions:", MAX_REVISIONS)
