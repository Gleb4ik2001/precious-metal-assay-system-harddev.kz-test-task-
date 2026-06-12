import random
import time

import requests

from app.core.config import settings


API_URL = settings.API_URL

OPERATORS = [
    "Ivanov",
    "Petrov",
    "Sidorov"
]


def generate_sample(index: int) -> dict:
    return {
        "sample_code": f"SAMPLE-{index:04d}",
        "weight": round(random.uniform(1.0, 100.0), 2),
        "operator": random.choice(OPERATORS)
    }


def send_sample(sample_data: dict) -> None:
    response = requests.post(
        API_URL,
        json=sample_data,
        timeout=10
    )

    response.raise_for_status()

    print(
        f"Created sample: "
        f"{sample_data['sample_code']} "
        f"(status={response.status_code})"
    )


def main() -> None:
    for i in range(1, 21):

        sample_data = generate_sample(i)

        try:
            send_sample(sample_data)

        except requests.RequestException as exc:
            print(
                f"Error while sending sample "
                f"{sample_data['sample_code']}: {exc}"
            )

        time.sleep(2)


if __name__ == "__main__":
    main()