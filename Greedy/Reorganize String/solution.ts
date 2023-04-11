function reorganizeString(s: string): string {
    let data = s.split("");
    let valid = 1
    for (let  i = 0; i< s.length; i++) {
        if (data[i]===data[i-1]) {
            valid = 0;
            for (let j = -1; j< data.length;j++) {
                if(data[i]!=data[j]&& data[i]!=data[j+1]) {
                    data.splice(j+1,0,data[i])
                    if(j> i ) {
                        data.splice(i,1)
                    }
                    else {
                        data.splice(i+1,1)
                    }
                    valid = 1;
                    break;
                }
            }
            if(valid === 0) 
                return ""
            i--;
        }
    }
    return data.join('');
};