class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer>set1 = new HashSet<>();
        for(int num:nums1){
            set1.add(num);
        }
        List<Integer>intersectionList = new ArrayList<>();
        for(int num:nums2){
            if(set1.contains(num)){
                intersectionList.add(num);
                set1.remove(num);
            }
        }
        int[] intersectionArray = new int[intersectionList.size()];
        for(int i=0;i<intersectionList.size();i++){
            intersectionArray[i]=intersectionList.get(i);
            
        }
        return intersectionArray;
    }
}


