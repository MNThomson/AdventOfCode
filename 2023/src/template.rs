fn part1(input: &str) -> u64 {
    0
}

// fn part2(input: &str) -> u64 {
//     0
// }

fn main() {
    println!("Part 1: {}", part1(&aoc::data_contents("00.input")));
    // println!("Part 2: {}", part2(&aoc::data_contents("00.input")));
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq;
    use rstest::rstest;

    #[rstest]
    #[case::part1_example(part1, &aoc::data_contents("00.example"), 1)]
    // #[case::part1_input(part1, &aoc::data_contents("00.input"), 1)]
    // #[case::part2_example(part2, &aoc::data_contents("00.example"), 1)]
    // #[case::part2_input(part2, &aoc::data_contents("00.input"), 1)]
    fn parts<F>(#[case] func: F, #[case] input_str: &str, #[case] expected: u64)
    where
        F: Fn(&str) -> u64,
    {
        assert_eq!(func(input_str), expected);
    }

    // #[rstest]
    // #[case(1, 2, 3)]
    // fn test_other(#[case] first: u64, #[case] second: u64, #[case] expected: u64) {
    //     assert_eq!(random_func(first, second), expected);
    // }
}
