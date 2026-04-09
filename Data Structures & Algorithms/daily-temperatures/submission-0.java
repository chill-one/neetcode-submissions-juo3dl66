class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        for(int i = 0; i < n; i++){
            int temp = temperatures[i];
            for(int j = i; j < n; j++){
                if(temp < temperatures[j]){
                    res[i] = (j - i);
                    break;
                }
            }
        }

        return res;
    }
}
