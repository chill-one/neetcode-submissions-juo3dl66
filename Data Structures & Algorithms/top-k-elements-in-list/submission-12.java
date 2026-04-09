class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        /**
            Go throught the array while counting the number of 
            occurance for the identical elements

            create a array which is the size of our nums array

            using the count from previous search use the count as index (value) 
            place the number inside as an array

            go throught the array from the back after k times until k elements are
            found
        **/

        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(map.get(nums[i])!= null){
                map.put(nums[i],map.get(nums[i])+1);
            }else{
                map.put(nums[i],1);
            }
        }

        List<Integer>[] bucket = new List[nums.length + 1];
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            if(bucket[value] == null) bucket[value] = new ArrayList<>();
            bucket[value].add(key);
        }

        int[] res = new int[k];
        int idx = 0;
        for(int i = bucket.length - 1; i >= 0; i--){
            if(k == 0) break;
            if(bucket[i] != null){
                for(int j = 0; j < bucket[i].size(); j++){
                    if(k == 0) break;
                    res[--k] = bucket[i].get(j);
                }
            }
        }

        return res;
    }
}
