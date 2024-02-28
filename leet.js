let nums = [2, 6, 7, 8, 9]
let target = 10

function twosum(nums) {
    for (i = 0; i < nums.length; i++)
        if (nums[i] + nums[i + 1] == target) {
            console.log(nums[i])
        }
}

console.log(twosum(nums))