if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    # Convert the list to a set to remove duplicates, then back to a list
    unique_scores = list(set(arr))

    # Sort the list in descending order
    unique_scores.sort(reverse=True)

    # The runner-up score is the second highest unique score
    runner_up_score = unique_scores[1]

    print(runner_up_score)
