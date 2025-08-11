# Filter Kickstarter JSONL Script Documentation

## Overview
The `filter_kickstarter_jsonl.py` script defines the `filter_kickstarter_data` function, which processes a JSONL file containing Kickstarter project data, filters for successful Technology projects (category `parent_id` = 16), and saves the results to a JSON file. It extracts specific fields and computes derived information, such as days left until the funding deadline.

## Function Signature
```python
def filter_kickstarter_data(input_file: str, output_file: str) -> None
```

## Parameters
- **input_file** (`str`): Path to the input JSONL file containing Kickstarter project data.
- **output_file** (`str`): Path to the output JSON file where filtered project data will be saved.

## Functionality
### Initialization
- Initializes empty lists for storing filtered projects and counters for tracking successful and total processed projects.
- Captures the current date and time using `datetime.now()` to calculate days left until deadlines.

### File Reading
- Opens the input JSONL file with UTF-8 encoding.
- Reads and processes the file line by line to efficiently handle large datasets.

### Data Processing
- Skips empty or whitespace lines.
- Parses each line as JSON, expecting a nested `'data'` field with project details.
- Filters projects based on:
  - Category parent ID (`parent_id == 16` for Technology).
  - Success status (`state == 'successful'` or `percent_funded >= 100`).
- Extracts fields:
  - Project name (`name`, defaults to `'Unknown'`)
  - Image URL (`photo.ed`, defaults to empty string)
  - Video URL (`video.base`, defaults to empty string if no video)
  - Funding amount (`converted_pledged_amount`, defaults to `'Unknown'`)
  - Funding percentage (`percent_funded`, defaults to `'Unknown'`)
  - Deadline timestamp (`deadline`, defaults to `None`)
- Computes derived fields:
  - Formats funding amount with commas and dollar sign (e.g., `$1,234`).
  - Formats funding percentage with two decimal places (e.g., `123.45%`).
  - Calculates days left until deadline (if `state == 'live'`) or marks as `'Expired'`.
  - Converts deadline timestamp to a formatted date string (`YYYY-MM-DD`).

### Progress Tracking
- Prints progress updates every 1,000 projects processed, showing the number of total and successful Technology projects.
- Logs errors for invalid JSON lines or processing issues without halting execution.

### Output
- Saves filtered projects to the specified JSON file with UTF-8 encoding and 2-space indentation.
- Prints final statistics, including total projects processed, successful Technology projects found, and number of projects saved.

## Error Handling
- Skips invalid JSON lines and logs errors using `json.JSONDecodeError`.
- Handles missing or malformed fields gracefully (e.g., missing `'data'` or `'category'`).
- Catches and logs file I/O errors during reading or writing.
- Continues processing even if individual lines or operations fail.

## Example Input
A sample line from the input JSONL file:
```json
{"data": {"name": "Tech Gadget", "category": {"parent_id": 16}, "state": "successful", "photo": {"ed": "http://example.com/image.jpg"}, "video": {"base": "http://example.com/video.mp4"}, "converted_pledged_amount": 50000, "percent_funded": 125.5, "deadline": 1767225600}}
```

## Example Output
The output JSON file might contain:
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

## Usage
```python
if __name__ == '__main__':
    input_file = 'kickstarter_dataset.json'
    output_file = 'filtered_kickstarter_projects.json'
    filter_kickstarter_data(input_file, output_file)
```

## Notes
- The script assumes the input JSONL file has a specific structure with a nested `'data'` field.
- The `parent_id = 16` is hardcoded to identify Technology projects.
- The output JSON file is formatted with indentation for readability.
- The script is optimized for large datasets by processing line by line and includes progress updates for user feedback.