class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> count = new HashMap<>();
        List<Integer>[] freq = new List[nums.length + 1];

        //initilizes all the list in freq
        for(int i = 0; i < freq.length; i++){
            freq[i] = new ArrayList<>();
        }

        //For every element in nums, we create or 
        //update a existing key value pair
        for( int n : nums){
            count.put(n, count.getOrDefault(n,0) + 1);
        }
        
        //Using entrySet we can grab each pair
        //We use the value:count as the index and key as the element for it
        for(Map.Entry<Integer, Integer> entry : count.entrySet()){
            freq[entry.getValue()].add(entry.getKey());
        }

        //We search for element for the end if its not empty we grab it
        //until the index == k
        int[] res = new int[k];
        int index = 0;
        for(int i = freq.length - 1; i > 0 && index < k; i--){
            for(int n : freq[i]){
                res[index++] = n;
                if(index ==k){
                    return res;
                }
            }
        }
        return res;
        
    }
        
}
