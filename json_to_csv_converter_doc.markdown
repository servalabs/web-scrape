# JSON to CSV Converter Documentation

## Overview
The `json_to_csv_converter.py` script defines the `json_to_csv` function, which converts a JSON file containing filtered Kickstarter project data into a CSV file. It reads the JSON file, extracts project details, and writes them to a CSV file with predefined headers.

## Function Signature
```python
def json_to_csv(input_file: str, output_file: str) -> None
```

## Parameters
- **input_file** (`str`): Path to the input JSON file containing filtered Kickstarter project data.
- **output_file** (`str`): Path to the output CSV file where the converted data will be saved.

## Functionality
### File Reading
- Opens the input JSON file with UTF-8 encoding.
- Loads the entire JSON file into memory using `json.load()`.

### Data Processing
- Defines CSV headers: `name`, `image_url`, `video_url`, `funding_amount`, `funding_percent`, `days_left`, `end_date`.
- Assumes the JSON file contains a list of project dictionaries with these fields.

### Output
- Writes the project data to the specified CSV file with UTF-8 encoding.
- Includes headers in the CSV file for clarity.
- Processes each project dictionary and writes it as a row in the CSV file.
- Prints progress updates every 1,000 projects processed.
- Prints the total number of projects converted and the output file path.

## Error Handling
- Catches and logs file I/O errors during JSON reading or CSV writing.
- Stops execution if the JSON file cannot be read or if the CSV file cannot be written.

## Example Input
A sample input JSON file:
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

## Example Output
The output CSV file:
```csv
name,image_url,video_url,funding_amount,funding_percent,days_left,end_date
Tech Gadget,http://example.com/image.jpg,http://example.com/video.mp4,$50,000,125.50%,Expired,2026-01-01
```

## Usage
```python
if __name__ == '__main__':
    input_file = 'filtered_kickstarter_projects.json'
    output_file = 'kickstarter_projects.csv'
    json_to_csv(input_file, output_file)
```

## Notes
- Assumes the input JSON file is a list of dictionaries with the expected fields.
- The input JSON file is typically the output of a filtering script (e.g., `filter_kickstarter_jsonl.py` or `filter_kickstarter_to_json_and_csv.py`).
- Writes the CSV file with UTF-8 encoding and includes headers for readability.
- Provides progress updates for large datasets but loads the entire JSON file into memory, which may be memory-intensive for very large files.