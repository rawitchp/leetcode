/**
 * @param {number[]} groupSizes
 * @return {number[][]}
 */
 var groupThePeople = function(groupSizes) {
    let ans = []
    let hashMap = {}
    groupSizes.map((num,i)=>{
        hashMap[num]? hashMap[num].push(i): hashMap[num] = [i]
        if(hashMap[num].length == num){
            ans.push(hashMap[num])
            delete hashMap[num]
        }
    })
    return ans
};