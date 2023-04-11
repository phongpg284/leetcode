function minFallingPathSum(matrix: number[][]): number {
    let dp = new Array(matrix.length)
    for (let i =0 ;i < matrix.length; i++) {
        dp[i] = new Array(matrix[0].length)
        for(let j = 0; j< matrix[0].length; j++) {
            if(i > 0){
                if(j === 0)
                    dp[i][j] = Math.min(dp[i-1][j], dp[i-1][j+1])+matrix[i][j]
                else if(j===matrix[0].length-1)
                    dp[i][j] = Math.min(dp[i-1][j-1], dp[i-1][j])+matrix[i][j]
                else
                dp[i][j] = Math.min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])+matrix[i][j]
            }
            else 
                dp[i][j] = matrix[i][j];
        }
    }
    return Math.min(...dp[matrix.length-1]);
};