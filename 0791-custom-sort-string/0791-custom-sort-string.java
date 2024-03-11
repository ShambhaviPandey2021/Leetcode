import java.util.HashMap;

class Solution {
    public String customSortString(String order, String s) {
        HashMap<Character, Integer> sCount = new HashMap<>();
        for (char c : s.toCharArray()) {
            sCount.put(c, sCount.getOrDefault(c, 0) + 1);
        }

        StringBuilder result = new StringBuilder();
        for (char c : order.toCharArray()) {
            if (sCount.containsKey(c)) {
                int count = sCount.get(c);
                while (count-- > 0) {
                    result.append(c);
                }
                sCount.remove(c);
            }
        }

        for (char c : sCount.keySet()) {
            int count = sCount.get(c);
            while (count-- > 0) {
                result.append(c);
            }
        }
        
        return result.toString();
    }
}

      