class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length()!=t.length()){
            return false;
        }
        Map<Character,Integer> s_mapping = new HashMap<>();
        Map<Character,Integer> t_mapping = new HashMap<>();
        for(int i=0;i<s.length();i++){
            s_mapping.put(s.charAt(i), s_mapping.getOrDefault(s.charAt(i),0)+1);
            t_mapping.put(t.charAt(i), t_mapping.getOrDefault(t.charAt(i),0)+1);
        }
        return s_mapping.equals(t_mapping);
    }
}

//Space Complexity: O(1) since hashmap can only have max 26 length from 26 characters