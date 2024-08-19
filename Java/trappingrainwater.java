public class trappingrainwater {
        public int trap(int[] arr) {
            int n = arr.length;
            int l=0;
            int r=n-1;
            int leftmax = 0;
            int rightmax = 0;
            int ans=0;
            while (l<r){
                if (arr[l]<=arr[r]){
                    if(leftmax>arr[l]){
                        ans += (leftmax-arr[l]);
                    }
                    else{
                        leftmax = arr[l];
                    }
                    l++;
                } 
                else{
                    if (rightmax > arr[r]){
                        ans+=(rightmax-arr[r]);
                    }
                    else{
                        rightmax = arr[r];
                    }
                    r--;
                }
            }
            return ans;
        }
    }
