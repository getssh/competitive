/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let commonPrefix = ""
    let control = strs[0]

    function isTheSame(str1, str2, index) {
        return str1[index] === str2[index]
    }


    for (let i = 0; i < control.length; i++) {
        let j = 1
        for (; j < strs.length; j++) {
            if (!isTheSame(control, strs[j], i)) {
                return commonPrefix
            }
        }
        if (j === strs.length) {
            commonPrefix += control[i]
        }
    }

    return commonPrefix
};