use anyhow::Result;
use std::{env, str::FromStr};

pub fn read_one_per_line<T>(input_str: &str) -> Result<Vec<T>>
where
    T: FromStr,
{
    Ok(input_str
        .lines()
        .filter_map(|line| line.parse::<T>().ok())
        .collect())
}

pub fn data_contents(input_str: &str) -> String {
    std::fs::read_to_string(format!(
        "{}/data/{}",
        env::var("CARGO_MANIFEST_DIR").unwrap(),
        input_str
    ))
    .unwrap()
}
