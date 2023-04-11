function maxArea(height: number[]): number {
    return max_area(height)
};

function max_area (height) {
    let start = 0;
    let end = height.length - 1
    let area = 0;
    
    while (start< end) {
        area = Math.max(area, Math.min(height[start], height[end])*(end-start))
        if (height[start] < height[end])
            start = start + 1
        else
            end = end - 1
    }
    return area
}
