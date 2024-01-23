class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int i=0, j=0, s1=str1.size(), s2=str2.size();
        string ans="", temp="";
        for(;i<s1 && j<s2;i++, j++){
            if(str1[i]!=str2[j])return "";
            temp+=str1[i];
            if(s1%(i+1)==0 && s2%(j+1)==0){
                ans=temp;
            }
        }
        int p=0;
        for(i=0;i<s1;i++){
            if(str1[i]!=ans[p])return "";
            p=(p+1)%(ans.size());
        }
        p=0;
        for(j=0;j<s2;j++){
            if(str2[j]!=ans[p])return "";
            p=(p+1)%(ans.size());
        }
        return ans;
    }
};