use anyhow::{Ok, Result};

fn score(t: &u64, d: u64) -> Result<u64> {
    Ok((0..*t).filter(|speed| ((t - speed) * speed > d)).count() as u64)
}

fn part1(input: &str) -> Result<u64> {
    let lines = aoc::read_one_per_line::<String>(input)?;

    let get_parsed_vec = |pos: usize| -> Vec<u64> {
        lines
            .get(pos)
            .unwrap()
            .split_ascii_whitespace()
            .skip(1)
            .map(|i| i.parse().unwrap())
            .collect()
    };

    let time = get_parsed_vec(0);
    let dist = get_parsed_vec(1);

    let val = time
        .iter()
        .zip(dist)
        .map(|(t, d)| score(t, d).unwrap())
        .filter(|x| x.gt(&0))
        .product();

    Ok(val)
}

fn part2(input: &str) -> Result<u64> {
    let lines = aoc::read_one_per_line::<String>(input)?;

    let get_combined_num = |pos: usize| -> u64 {
        lines
            .get(pos)
            .unwrap()
            .split_ascii_whitespace()
            .skip(1)
            .map(|i| i.parse().unwrap())
            .fold(0, |acc, num: u64| {
                acc * 10_u64.pow(num.to_string().len() as u32) + num
            })
    };

    let time = get_combined_num(0);
    let dist = get_combined_num(1);

    let val = score(&time, dist)?;

    Ok(val)
}

fn main() -> Result<()> {
    println!("Part 1: {}", part1(&aoc::data_contents("06.input"))?);
    println!("Part 2: {}", part2(&aoc::data_contents("06.input"))?);

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq;
    use rstest::rstest;

    #[rstest]
    #[case::part1_example(part1, &aoc::data_contents("06.example"), 288)]
    #[case::part1_input(part1, &aoc::data_contents("06.input"), 32076)]
    #[case::part2_example(part2, &aoc::data_contents("06.example"), 71503)]
    #[case::part2_input(part2, &aoc::data_contents("06.input"), 34278221)]
    fn parts<F>(#[case] func: F, #[case] input_str: &str, #[case] expected: u64)
    where
        F: Fn(&str) -> Result<u64>,
    {
        assert_eq!(func(input_str).unwrap(), expected);
    }

    #[rstest]
    #[case(7, 9, 4)]
    #[case(15, 40, 8)]
    #[case(30, 200, 9)]
    fn test_score(#[case] time: u64, #[case] dist: u64, #[case] expected: u64) {
        assert_eq!(score(&time, dist).unwrap(), expected);
    }
}
