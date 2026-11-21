impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {

        let (m,n) = (matrix.len(), matrix[0].len());
        let (mut lo, mut hi) = (0usize, m*n);

        while lo<hi{
            let mid = lo + (hi - lo)/2;
            match matrix[mid/n][mid%n].cmp(&target){
                Ordering::Equal => return true,
                Ordering::Less => lo = mid +1,
                Ordering::Greater => hi = mid,
            }
        }

        return false
    }
}
