import random

class Sorting:
    def __init__(self):
        # Preset cybersecurity logs
        self.logs = [
            "Unauthorized login attempt on WebApp1 (Alert: Username unknown)",
            "Malware detected in system files (Alert: Quarantine initiated)",
            "Database access denied on MySQL Server (Warning: Invalid credentials)",
            "Firewall blocked incoming request from suspicious IP (Notice: Access restricted)",
            "New SSL certificate issued for WebApp2 (Info: Certificate renewal completed)",
            "High CPU usage on WebServer3 (Alert: Usage exceeded 90%)",
            "Failed login attempt on Admin Portal (Warning: Incorrect password)",
            "Successful data backup on Backup Server (Info: Backup completed)",
            "Suspicious API call pattern detected on WebApp1 (Alert: Possible bot activity)",
            "Disk space low on Database Server (Warning: Less than 10% space remaining)",
            "System scan completed (Info: No issues detected)",
            "VPN connection established from unknown location (Alert: Verify user)",
            "Intrusion prevention system triggered on Network (Alert: Unusual activity)",
            "New user created in WebApp2 (Info: Role assigned - Viewer)",
            "Antivirus update applied on all endpoints (Info: Definitions updated)"
        ]
    
    def disorganize_logs(self):
        """
        Shuffle the preset logs for demonstration.
        """
        random.shuffle(self.logs)

    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return self.quicksort(left) + middle + self.quicksort(right)

    def binary_search(self, arr, target):
        """
        Perform binary search on a sorted array.
        Returns the index of the target if found, else returns -1.
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid  # Found the target
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # Target not found

    def get_logs(self):
        """
        Return the current state of logs (useful for displaying in UI).
        """
        return self.logs

    def sort_logs(self):
        """
        Sort the logs using quicksort and update the logs list.
        """
        self.logs = self.quicksort(self.logs)

    def search_log(self, log_entry):
        """
        Search for a log entry in the sorted logs.
        Returns the position if found, else indicates not found.
        """
        sorted_logs = self.quicksort(self.logs)  # Ensure logs are sorted
        index = self.binary_search(sorted_logs, log_entry)
        return index if index != -1 else "Log entry not found."
