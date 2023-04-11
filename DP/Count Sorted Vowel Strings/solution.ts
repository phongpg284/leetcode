function countVowelStrings(n: number): number {
    let dp = [1,0,0,0,0];
    let result = 0;
    for(let i =1; i<=n;i++) {
        for(let j = 1; j <= 4; j++){
            dp[j] = dp[j] + dp[j-1];
            if(i===n) 
            result = result + dp[j]
        }
    }
    return result + 1;
};