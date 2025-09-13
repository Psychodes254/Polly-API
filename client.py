import requests

BASE_URL = "http://127.0.0.1:8000"

def cast_vote(poll_id: int, option_id: int, token: str):
    """
    Casts a vote on a specific poll.

    Args:
        poll_id: The ID of the poll to vote on.
        option_id: The ID of the option to vote for.
        token: The authentication token for the user.

    Returns:
        The JSON response from the API.
    """
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(
        f"{BASE_URL}/polls/{poll_id}/vote",
        json={"option_id": option_id},
        headers=headers,
    )
    response.raise_for_status()
    return response.json()

def get_poll_results(poll_id: int):
    """
    Retrieves the results for a specific poll.

    Args:
        poll_id: The ID of the poll to get results for.

    Returns:
        The JSON response from the API.
    """
    response = requests.get(f"{BASE_URL}/polls/{poll_id}/results")
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # This is a usage example.
    # Replace with a valid poll ID, option ID, and token.
    POLL_ID = 1
    OPTION_ID = 1
    # You can get a token by using the /login endpoint
    TOKEN = "your_auth_token_here"

    try:
        # Get poll results before voting
        print(f"--- Results for Poll {POLL_ID} (before vote) ---")
        results_before = get_poll_results(POLL_ID)
        print(results_before)

        # Cast a vote
        print(f"\n--- Casting vote on Poll {POLL_ID} for Option {OPTION_ID} ---")
        vote_result = cast_vote(POLL_ID, OPTION_ID, TOKEN)
        print("Vote successful:", vote_result)

        # Get poll results after voting
        print(f"\n--- Results for Poll {POLL_ID} (after vote) ---")
        results_after = get_poll_results(POLL_ID)
        print(results_after)

    except requests.exceptions.HTTPError as e:
        print(f"An HTTP error occurred: {e.response.status_code} {e.response.reason}")
        print(f"Details: {e.response.text}")
    except requests.exceptions.RequestException as e:
        print(f"A network error occurred: {e}")
