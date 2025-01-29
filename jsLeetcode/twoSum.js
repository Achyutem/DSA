// https://leetcode.com/problems/two-sum/

function twoSum(nums, target) {
    const hash = new Map()

    for(i=0;i<nums.length;i++){
        const diff = target - nums[i]

        if(hash.has(diff)) {
            return [hash.get(diff), i]
        }

        hash.set(nums[i], i)
    }

    return []
};
