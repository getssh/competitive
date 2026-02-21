/**
 * @param {number[][]} img
 * @return {number[][]}
 */
var imageSmoother = function(img) {
    const m = img.length;
    const n = img[0].length;
    const result = new Array(m).fill().map(() => new Array(n).fill(0));

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let sum = 0;
            let count = 0;
            
            for (let r = -1; r <= 1; r++) {
                for (let c = -1; c <= 1; c++) {
                    const newRow = i + r;
                    const newCol = j + c;
                    
                    if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n) {
                        sum += img[newRow][newCol];
                        count++;
                    }
                }
            }
            
            result[i][j] = Math.floor(sum / count);
        }
    }
    
    return result;
};