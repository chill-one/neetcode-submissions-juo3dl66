class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] bucket = new List[nums.length+1];
        HashMap<Integer, Integer> counts = new HashMap<>();

        for(int num: nums){
            counts.put(num, counts.getOrDefault(num, 0)+1);
        }

        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            int idx = entry.getValue();
            if(bucket[idx]==null)bucket[idx] = new ArrayList<>();
            bucket[idx].add(entry.getKey());
        }

        int idx = 0;
        int res[] = new int[k];
        for(int i = bucket.length-1; i >= 0; i--){
            if(bucket[i] != null){
                for(int num : bucket[i]){
                    res[idx++] = num;
                    if(idx==k){
                        return res;
                    }
                }
            }
        }
        return res;

    }
}
