"""
https://leetcode.com/problems/stone-removal-game/

Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.

Alice starts by removing exactly 10 stones on her first turn.
For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
The player who cannot make a move loses the game.

Given a positive integer n, return true if Alice wins the game and false otherwise.

Example 1:
    Input: n = 12
    Output: true
    Explanation:
        - Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
        - Bob cannot remove 9 stones, so Alice wins.

Example 2:
    Input: n = 1
    Output: false
    Explanation:
        - Alice cannot remove 10 stones, so Alice loses.

Constraints:
    1 <= n <= 50
"""

from math import sqrt


class Solution:
    """
    Alice always takes even number of stones, while Bob - only odd.

    """

    def canAliceWin(self, n: int) -> bool:
        """
        Simulation.

        The number of stones removed on each move is fixed: 10,9,8,….
        Neither player has any choice, so we can directly simulate the game.

        Let take be the number of stones to remove on the current move,
        and let k count the completed moves. Initially, take=10 and k=0.
        While the remaining stones satisfy n≥take, the current player can
        make the move: decrease n by take, decrement take by 1, and increment
        k by 1. Repeat this process until there are not enough stones for
        the next move.

        Alice moves first, so she makes the odd-numbered moves and Bob makes
        the even-numbered moves. The player who makes the last successful move
        wins. Therefore, Alice wins if and only if k is odd. If k=0, Alice
        cannot make the first move, which also correctly evaluates to false
        because 0 is even.

        Time complexity: O(1), since n <= 50 and the first 8 moves returned
            10 + 9 + ... + 3 = 52 stones, the loop exectues at most 7 times.
        Space complexity: O(1)
        """
        take = 10
        while n >= take:
            n -= take
            take -= 1
        return take % 2 == 1

    def canAliceWin_approach_2(self, n: int) -> bool:
        """
        Mathematics.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        k = int((21 - sqrt(441 - 8 * n)) / 2)
        return k % 2 == 1


if __name__ == "__main__":
    test_cases = [(12, True), (1, False)]
    s = Solution()

    for n, expected in test_cases:
        actual = s.canAliceWin(n)
        assert actual == expected, (
            f"canAliceWin({n}) returned {actual}, expected {expected}"
        )
        actual_approach_2 = s.canAliceWin_approach_2(n)
        assert actual_approach_2 == expected, (
            f"canAliceWin_approach_2({n}) returned {actual_approach_2}, exepected {expected}"
        )

    print("All tests passed!")
