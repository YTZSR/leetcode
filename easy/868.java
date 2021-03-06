class Solution {
    public int binaryGap(int n) {
        if(n == 0){
            return 0;
        }
        while(n % 2 != 1){
            n /= 2;
        }
        n /= 2;
        int max = 0;
        while(n >= 1){
            int count = 1;
            while(n % 2 == 0){
                count ++;
                n /= 2;
            }
            if(count > max){
                max = count;
            }
            n /= 2;
        }
        return max;
    }
}