class TimeMap {
    class Value{
        String value;
        int timeStamp;
        public Value(String value, int timeStamp){
            this.value = value;
            this.timeStamp = timeStamp;
        }
    }
    private HashMap<String,List<Value>> map;

    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        Value val = new Value(value, timestamp);
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(val);
    }
    public String get(String key, int timestamp) {
        List<Value> arr = map.get(key);
        if(arr == null) return "";
        int l = 0;
        int r = arr.size() - 1;
        String res = "";
        //  0. 1  2  3. 4. 5. 6
        // [1, 4, 6, 8, 9, 10, 11]
        while(l <= r){
            int mid = l + (r - l) / 2;

            if(arr.get(mid).timeStamp <= timestamp){
                res = arr.get(mid).value;
                l = mid + 1 ;
            }else{
                r = mid - 1;
            }
        }
        return res;
    }
}
