class Solution {
    public int change(int amount, int[] arr) {
        // 动态规划
        int[] list = new int[amount + 1];
        list[0] = 1;
        for (int coin : arr) {
            for (int i = 0; i+coin <= amount; i++) {
                list[i+coin] += list[i];
            }
        }
        return list[amount];
    }
}