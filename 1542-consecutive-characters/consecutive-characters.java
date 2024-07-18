class Solution {
    public int maxPower(String s) {
        int count = 1;
        int maxCount = 0;
        for(int i = 1 ;i < s.length() ; i++){
            if(s.charAt(i) == s.charAt( i - 1)){
                count++;
                
            }
            else{
                maxCount = Math.max(count,maxCount);
                count = 1;
            }
        }
        maxCount = Math.max(count,maxCount);
        return maxCount;
    }
}