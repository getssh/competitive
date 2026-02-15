/**
 * @param {string[]} words
 * @return {string[]}
 */
var commonChars = function(words) {
    let commonChar = ''
    let control = words[0].split('')
    let index = control.length

    for (let i = 1; i < words.length; i++) {
        let word = words[i].split('')
        let tempCommon = ''
        for (let j = 0; j < control.length && j >= 0; j++) {
            if (word.includes(control[j])) {
                tempCommon += control[j]
                word.splice(word.indexOf(control[j]), 1)
                control.splice(control.indexOf(control[j]), 1)
                j--
            } else {
                control.splice(control.indexOf(control[j]), 1)
                j--
            }
        }
        control = tempCommon.split('')
    }

    return control
};