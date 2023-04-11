function longestPalindrome(s: string): string {
    const even = longestPalindromeEven(s)
    const odd = longestPalindromeOdd(s)
    return odd.length > even.length ? odd : even;

};

function longestPalindromeOdd(s: string): string {
    const max_length = s.length;
    let result = 1;
    let start = 0;
    let end = 0;
    for (let i = 0; i < max_length; i++) {
        let step = 1;
        let count = 1;
        while (step < max_length / 2) {
            if (i+ step < max_length && i-step >= 0 && s[i + step ] === s[i - step]) {
                count += 2;
                step += 1
            }
            else {
                break
                
            }
        }
        if (count > result) {
            result = count; 
            start = i - (step -1);
            end = i + (step -1 );
        }
    }
    return s.slice(start, end +1);
};

function longestPalindromeEven(s: string): string {
    const max_length = s.length;
    let result = 0;
    let start = 0;
    let end = 0;
    for (let i = 0; i < max_length - 1; i++) {
        let step = 1;
        let count = 1;

        if (s[i+1] !== s[i])
            continue;
        while (step < max_length / 2) {
            if (i + 1 + step < max_length && i - step >= 0 && s[i + 1  + step ] === s[i - step]) {
                count += 2;
                step += 1
            }
            else {
                break                
            }
        }
        if (count > result) {
            result = count; 
            start = i - (step -1);
            end = i  + 1 + (step -1 );
        }
    }
    return s.slice(start, end +1);
};