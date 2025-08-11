# Filter Kickstarter JSONL Documentation

## Overview
The `filter_kickstarter_data` function processes a JSONL file containing Kickstarter project data, filters for successful Technology projects (category `parent_id` = 16), and saves the results to a JSON file. It extracts specific fields and computes additional information, such as days left until the funding deadline.

## Function Signature
```python
def filter_kickstarter_data(input_file: str, output_file: str) -> None
```

## Parameters
- **input_file** (`str`): Path to the input JSONL file containing Kickstarter project data.
- **output_file** (`str`): Path to the output JSON file where filtered project data will be saved.

## Functionality
### Initialization
- Initializes lists and counters for projects, successful projects, and total processed projects.
- Captures the current date and time using `datetime.now()` for calculating days left.

### File Reading
- Opens the input JSONL file with UTF-8 encoding.
- Processes the file line by line to handle large datasets efficiently.

### Data Processing
- Skips empty or whitespace lines.
- Parses each line as JSON, expecting a nested `'data'` field containing project details.
- Filters projects based on:
  - Category parent ID (`parent_id == 16` for Technology).
  - Success status (`state == 'successful'` or `percent_funded >= 100`).
- Extracts fields:
  - Project name (`name`)
  - Image URL (`photo.ed`)
  - Video URL (`video.base`, if available)
  - Funding amount (`converted_pledged_amount`)
  - Funding percentage (`percent_funded`)
  - Deadline timestamp (`deadline`)
- Computes derived fields:
  - Formats funding amount with commas and dollar sign (e.g., `$1,234`).
  - Formats funding percentage with two decimal places (e.g., `123.45%`).
  - Calculates days left until deadline (if `state == 'live'`) or marks as `'Expired'`.
  - Converts deadline timestamp to a formatted date string (`YYYY-MM-DD`).

### Progress Tracking
- Prints progress updates every 1,000 projects processed.
- Logs errors for invalid JSON lines or other processing issues without stopping execution.

### Output
- Saves filtered projects to the specified output JSON file with proper indentation.
- Prints final statistics, including total projects processed,