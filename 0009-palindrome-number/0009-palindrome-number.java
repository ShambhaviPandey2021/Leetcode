class Solution {
    public boolean isPalindrome(int x) {

        long org  = x ;
        long  rev = 0 ;
        while( x > 0 ){
            int digit = x % 10; 
            x = x /10;
            rev = rev * 10  + digit; 
        }
        if (org == rev ){
            return  true ;
        }
        else {
            return false;
            }
    }
}