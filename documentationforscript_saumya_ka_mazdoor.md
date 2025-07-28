filter_kickstarter_data Documentation
Overview
The filter_kickstarter_data function processes a JSONL file containing Kickstarter project data, filters for successful Technology projects, and saves the results to a new JSON file. It extracts specific fields and computes additional information like days left until the funding deadline.
Function Signature
def filter_kickstarter_data(input_file: str, output_file: str) -> None

Parameters

input_file (str): Path to the input JSONL file containing Kickstarter project data.
output_file (str): Path to the output JSON file where filtered project data will be saved.

Functionality

Initialization:

Initializes empty lists and counters for projects, successful projects, and total processed projects.
Captures the current date and time using datetime.now() for calculating days left.


File Reading:

Opens the input JSONL file with UTF-8 encoding.
Processes the file line by line to handle large datasets efficiently.


Data Processing:

Skips empty or whitespace lines.
Parses each line as JSON, expecting a nested 'data' field containing project details.
Filters projects based on:
Category parent ID (parent_id == 16 for Technology).
Success status (state == 'successful' or percent_funded >= 100).


Extracts relevant fields:
Project name
Image URL (photo.ed)
Video URL (video.base, if available)
Funding amount (converted_pledged_amount)
Funding percentage (percent_funded)
Deadline timestamp


Computes derived fields:
Formats funding amount with commas and dollar sign (e.g., $1,234).
Formats funding percentage with two decimal places (e.g., 123.45%).
Calculates days left until deadline (if state == 'live') or marks as 'Expired'.
Converts deadline timestamp to a formatted date string (YYYY-MM-DD).




Progress Tracking:

Prints progress updates every 1,000 projects processed.
Logs errors for invalid JSON lines or other processing issues without stopping execution.


Output:

Saves filtered projects to the specified output JSON file with proper indentation.
Prints final statistics, including total projects processed, successful Technology projects found, and number of projects saved.



Error Handling

Skips invalid JSON lines and logs errors.
Handles missing or malformed fields gracefully (e.g., missing 'data' or 'category').
Catches and logs file I/O errors during reading or writing.
Continues processing even if individual lines fail.

Example Input
A sample line from kickstarter_dataset.json might look like:
{"data": {"name": "Tech Gadget", "category": {"parent_id": 16}, "state": "successful", "photo": {"ed": "http://example.com/image.jpg"}, "video": {"base": "http://example.com/video.mp4"}, "converted_pledged_amount": 50000, "percent_funded": 125.5, "deadline": 1767225600}}

Example Output
The filtered_kickstarter_projects.json file might contain:
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

Usage
if __name__ == '__main__':
    input_file = 'kickstarter_dataset.json'
    output_file = 'filtered_kickstarter_projects.json'
    filter_kickstarter_data(input_file, output_file)

Notes

The function assumes the input JSONL file has a specific structure with a nested 'data' field.
The parent_id of 16 is hardcoded for the Technology category.
The output JSON file is written with UTF-8 encoding and formatted with indentation for readability.
The function is designed to handle large datasets by processing line by line and providing progress updates.
