
impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {

        let h = h as u64;

        let can_finish = |k: u64| -> bool{
            let mut hours: u64 =0;
            for &pile in &piles{
                hours += (pile as u64).div_ceil(k);
                if hours > h{
                    return false;
                }
            }
            return true;
        };

        let (mut lo, mut hi) = (1u64, *piles.iter().max().unwrap() as u64);

        while lo<hi{
            let mid = lo +(hi-lo)/2;
            if can_finish(mid){
                hi = mid;
            }else{
                lo = mid +1;
            }
        }


        return lo as i32;
    }
}
