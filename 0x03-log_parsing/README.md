# Log Metrics Script

=====================
This script reads input from the standard input (stdin) line by line, processes log entries in a specific format, and computes various metrics. It prints these statistics after every 10 lines or when interrupted using CTRL + C.

## Usage

You can run the script as follows:

```Python
python log_metrics.py
Make sure you have Python installed on your system.
```

## Input Format

The script expects log entries to be in the following format:

```Python
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
If a line does not match this format, it will be skipped.
```

## Metrics Computed

After processing every 10 lines or when interrupted, the script prints the following metrics:

Total File Size: The sum of all previous file sizes.

```arduino
Total File Size: <total size>
Number of Lines by Status Code: The count of log entries grouped by status code. The status codes considered are 200, 301, 400, 401, 403, 404, 405, and 500. Only valid integer status codes are included in the output.

```

Average Response Time: The average time taken for each request made by an IP address. This is calculated from the difference between the start and end

```yaml
Status Code Metrics:
200: <number>
301: <number>
400: <number>
401: <number>
403: <number>
404: <number>
405: <number>
500: <number>
```

Above is an example output for status codes. Each number represents the count of requests with that specific status code.

Status codes are printed in ascending order.

## Example

Suppose you have a log file with the following content:

```arduino
192.168.1.1 - [2023-10-19] "GET /projects/260 HTTP/1.1" 200 100
192.168.1.2 - [2023-10-19] "GET /projects/260 HTTP/1.1" 404 50
192.168.1.3 - [2023-10-19] "GET /projects/260 HTTP/1.1" 200 75
192.168.1.4 - [2023-10-19] "GET /projects/260 HTTP/1.1" 301 60
192.168.1.5 - [2023-10-19] "POST /projects/260 HTTP/1.1" 500 45```

When you run the script and provide this input, after processing every 10 lines or when interrupted, you will get the following output:

```yaml
Total File Size: 100
Status Code Metrics:
200: 2
301: 1
404: 1```

## Author

This script is created by [Marubi N Richard]. For questions or feedback, you can contact me at [richardnyamwamu@gmail.com].
