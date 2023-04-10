function generateParenthesis(n: number): string[] {
    return dp("", 0, 0, n)
};

function dp(s, open, cur, max) {
    if (cur === max) 
        return [s]
    if (open === 0) {
        return [...dp(s + "(", open + 1, cur, max)]
    }
    
    if (open + cur === max) {
        return [...dp(s + ")", open - 1, cur + 1, max)]
    }
    
    return [...dp(s + "(", open + 1, cur, max), ...dp(s + ")", open - 1, cur + 1, max)]
}