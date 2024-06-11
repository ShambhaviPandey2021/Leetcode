import java.util.*;
class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        Map<Integer,Integer>freqMap = new HashMap<>();
        for(int num : arr1) {
            freqMap.put(num , freqMap.getOrDefault(num,0)+1);
        }
        List<Integer>resultList = new ArrayList<>();
        for(int num : arr2){
            if(freqMap.containsKey(num)){
                int count  = freqMap.get(num);
                for(int i = 0;i<count;i++){
                    resultList.add(num);
                }
                freqMap.remove(num);
            }
        }
        List<Integer>remaining = new ArrayList<>();
        for(Map.Entry<Integer,Integer>entry : freqMap.entrySet()) {
            int count = entry.getValue();
            for(int i =0;i<count;i++){
                remaining.add(entry.getKey());
                
            }
        }
        Collections.sort(remaining);
        resultList.addAll(remaining);
        int [] resultArray = new int[resultList.size()];
        for(int i = 0;i<resultList.size();i++){
            resultArray[i] = resultList.get(i);
        }
        return resultArray;
        
    }
}