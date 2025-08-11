# Filter Kickstarter to JSON and CSV Documentation

## Overview
The `filter_kickstarter_to_json_and_csv.py` script defines the `filter_kickstarter_data` function, which processes a JSONL file containing Kickstarter project data, filters for successful Technology projects (category `parent_id` = 16), and saves the results to both a JSON file and a CSV file. It extracts specific fields, computes additional information like days left until the funding deadline, and includes progress tracking and validation checks.

## Function Signature
```python
def filter_kickstarter_data(input_file: str, json_output_file: str, csv_output_file: str) -> None
```

## Parameters
- **input_file** (`str`): Path to the input JSONL file containing Kickstarter project data.
- **json_output_file** (`str`): Path to the output JSON file where filtered project data will be saved.
- **csv_output_file** (`str`): Path to the output CSV file where filtered project data will be saved.

## Functionality
### Initialization
- Initializes lists and counters for projects, successful projects, and total processed projects.
- Captures the current date and time using `datetime.now()` for calculating days left.
- Prints a message indicating the filters applied (Technology category and success status).

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
  - Project name (`name`, defaults to `'Unknown'`)
  - Image URL (`photo.ed`, defaults to empty string)
  - Video URL (`video.base`, defaults to `'Expired'` if not available)
  - Funding amount (`converted_pledged_amount`, defaults to `'Unknown'`)
  - Funding percentage (`percent_funded`, defaults to `'Unknown'`)
  - Deadline timestamp (`deadline`, defaults to `None`)
- Computes derived fields:
  - Formats funding amount with commas and dollar sign (e.g., `$1,234`).
  - Formats funding percentage with two decimal places (e.g., `123.45%`).
  - Calculates days left until deadline (if `state == 'live'`) or marks as `'Expired'`.
  - Converts deadline timestamp to a formatted date string (`YYYY-MM-DD`).

### Progress Tracking
- Prints progress updates every 1,000 projects processed, showing total and successful Technology projects.
- Logs errors for invalid JSON lines or other processing issues without stopping execution.

### Output
- Saves filtered projects to the specified JSON file with UTF-8 encoding and 2-space indentation.
- Saves filtered projects to the specified CSV file with headers (`name`, `image_url`, `video_url`, `funding_amount`, `funding_percent`, `days_left`, `end_date`).
- Prints final statistics, including total projects processed, successful Technology projects found, and number of projects saved.
- Issues a warning if fewer than 14,000 successful Technology projects are found, suggesting a check of the dataset.

### Validation
- Checks if the number of successful Technology projects is significantly lower than expected (~14,000) and prints a warning.

## Error Handling
- Skips invalid JSON lines and logs errors using `json.JSONDecodeError`.
- Handles missing or malformed fields gracefully (e.g., missing `'data'` or `'category'`).
- Catches and logs file I/O errors during reading or writing (both JSON and CSV).
- Continues processing even if individual lines or operations fail.

## Example Input
A sample line from the input JSONL file:
```json
{"data": {"name": "Tech Gadget", "category": {"parent_id": 16}, "state": "successful", "photo": {"ed": "http://example.com/image.jpg"}, "video": {"base": "http://example.com/video.mp4"}, "converted_pledged_amount": 50000, "percent_funded": 125.5, "deadline": 1767225600}}
```

## Example Output
### JSON Output
The JSON file might contain:
```json
[
  {
    "name": "Tech Gadget",
    "image_url": "http://example.com/image.jpg",
    "video_url": "http://example.com/video.mp4",
    "funding_amount": "$50,000",
    "funding_percent": "125.50%",
    "days_left": "Expired",
    "end_date": "2026-01-01"
  }
]
```

### CSV Output
The CSV file might contain:
```csv
name,image_url,video_url,funding_amount,funding_percent,days_left,end_date
Tech Gadget,http://example.com/image.jpg,http://example.com/video.mp4,$50,000,125.50%,Expired,2026-01-01
```

## Usage
```python
if __name__ == '__main__':
    input_file = 'kickstarter_dataset.json'
    json_output_file = 'filtered_kickstarter_projects.json'
    csv_output_file = 'kickstarter_projects_FINAL.csv'
    filter_kickstarter_data(input_file, json_output_file, csv_output_file)
```

## Notes
- Assumes the input JSONL file has a nested `'data'` field.
- Hardcodes `parent_id = 16` for the Technology category.
- The JSON output is formatted with indentation, and the CSV output includes headers for readability.
- Optimized for large datasets with line-by-line processing and progress updates.
- Includes a validation check for the expected number of successful projects.