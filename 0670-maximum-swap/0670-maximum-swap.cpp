class Solution {
public:
    int maximumSwap(int num) {
        string numstr = to_string(num);
        vector<int>lastindex(10,-1);
        for(int i = 0 ;i<numstr.size();i++){
            lastindex[numstr[i]-'0']=i;
            
        }
        for(int i = 0;i<numstr.size();i++){
            for(int d=9;d>numstr[i]-'0';d--){
                if(lastindex[d]>i){
                    swap(numstr[i],numstr[lastindex[d]]);
                    return stoi(numstr);
                }
            }   
        }
        return num;
        
    }
};