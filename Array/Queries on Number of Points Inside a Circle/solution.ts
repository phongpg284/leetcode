function countPoints(points: number[][], queries: number[][]): number[] {
    let result = []
    for(let i= 0; i< queries.length;i++) {
            let nums = 0
        for(let j =0; j< points.length;j++) {
            const x = (queries[i][0]-points[j][0])**2;
            const y = (queries[i][1]-points[j][1])**2;
            if(x+y <= queries[i][2]**2)
            nums++;
        }
        result.push(nums);
    }
    return result
};