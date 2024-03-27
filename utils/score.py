from utils.utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def add_score(username, difficulty):
    try:
        try:
            # Read scores from file
            with open(SCORES_FILE_NAME, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []

        # Update score for the specified user
        updated = False
        score_delta = (difficulty * 3) + 5
        new_score = score_delta
        for i, line in enumerate(lines):
            user, score = line.strip().split(',')
            if user == username:
                new_score = int(score) + score_delta
                lines[i] = f"{user},{new_score}\n"
                updated = True
                break

        if not updated:
            # If user not found, add new user with score
            lines.append(f"{username},{new_score}\n")

        # Write updated scores back to file
        with open(SCORES_FILE_NAME, 'w') as file:
            file.writelines(lines)

        print("Score updated successfully.")
        return new_score

    except Exception as e:
        print(f"Error: {e}")
        return BAD_RETURN_CODE


def read_scores(username=None):
    try:
        # Read scores from file
        with open(SCORES_FILE_NAME, 'r') as file:
            lines = file.readlines()
        scores = {}

        # read score for the specified user
        for i, line in enumerate(lines):
            user, score = line.strip().split(',')
            scores[user] = int(score)

        if username is not None:
            # read score for the specified user
            if username in scores:
                return {username: scores[username]}
            else:
                raise Exception(f"username {username} not found.")
        else:
            # read score for all users
            return scores

    except FileNotFoundError:
        err = f"Error: File '{SCORES_FILE_NAME}' not found."
        return {BAD_RETURN_CODE: err}
    except Exception as e:
        err = f"Error: {e}"
        return {BAD_RETURN_CODE: err}
