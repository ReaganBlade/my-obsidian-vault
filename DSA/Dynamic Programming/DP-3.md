Given, Maximum sum without adjacent elements

a -> 2, 3, 4, -8, 2
b -> -5, 8, 3, 1, -4

condition 1:
    Only 1 element from 1 column at max

condition 2:
    No two selected elements should be adjacent diagonally or horizontally


here dp[1] => 2
then dp[2] => 8
then dp[3] => max(max(dp[1] + 4, dp[1] + 3), dp[2]) => 8
