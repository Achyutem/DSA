//https://leetcode.com/problems/rotate-array/

function rotate(nums, k) {
    k %= nums.length;
    let l = 0
    let r = nums.length - 1

    while(l<r){
        let temp = nums[l];
        nums[l] = nums[r];
        nums[r] = temp;
        l += 1
        r -= 1
    }

    l = 0
    r = k - 1

    while(l<r){
        let temp = nums[l];
        nums[l] = nums[r];
        nums[r] = temp;
        l += 1
        r -= 1
    }

    l = k
    r = nums.length - 1

    while(l<r){
        let temp = nums[l];
        nums[l] = nums[r];
        nums[r] = temp;
        l += 1
        r -= 1
    }
};
