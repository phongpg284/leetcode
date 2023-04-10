function jump(nums: number[]): number {
    const jump_count = [];
    for (let i = 0; i< nums.length; i++) {
        if ( i === 0) {
            jump_count.push(0)
        }
        else {
            const prev_max_jump = jump_count[i-1]
            let max_jump = -1;
            for (let j = i - 1; j >=0; j--) {
                if (j + nums[j] >= i) {
                    if (max_jump === -1 || (max_jump> jump_count[j] + 1))
                        max_jump = jump_count[j] + 1
                }

                if (max_jump === prev_max_jump) {
                    break;
                }
            }
            jump_count.push(max_jump)
        }
    }
    return jump_count[nums.length - 1]
};