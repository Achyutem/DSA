//https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal

function areAlmostEqual(s1, s2){
    let mismatch = []

    for(let i=0;i<s1.length;i++){
        if(s1[i] !== s2[i]){
            mismatch.push([s1[i], s2[i]])
        }
    }

    if(mismatch.length === 0){
        return true
    } else if (mismatch.length === 2){
        return (mismatch[0][0] === mismatch[1][1] &&
        mismatch[0][1] === mismatch[1][0])
    }

    return false
}
