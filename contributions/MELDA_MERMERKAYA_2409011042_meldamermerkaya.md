# Contribution Report: Melda Mermerkaya

- **Full Name:** Melda Mermerkaya
- **Student ID:** 2409011042
- **GitHub Username:** meldamermerkaya

---

## 1. Role and Responsibility in the Project
- **Module 2 (IPv4 Address Masking - `mask_log_line`):**
  - Responsible for detecting, validating, and masking client IPv4 addresses within log entries to safeguard user privacy.

## 2. Technical Contributions and Code Details
- **Tokenization:**
  - Tokenized each log entry by whitespace (`words = line.split()`) to extract the leading element (`words[0]`) representing the client IP candidate.
- **Strict IPv4 Format Validation:**
  - Split the IP candidate on dots (`parts = ip.split(".")`) and verified that it contains exactly 4 octets (`len(parts) == 4`).
  - Verified each octet consists solely of numeric digits (`p.isdigit()`).
  - Confirmed that each octet length is at most 3 digits and within the integer range of 0 to 255 (`0 <= int(p) <= 255`).
  - Enforced a rule against leading zeros for numbers greater than one digit (e.g., rejecting `01` or `001`) to align with standard dot-decimal IPv4 representation (`len(p) > 1 and p[0] == "0"`).
- **Masking Mechanism:**
  - Replaced validated IPv4 addresses with `[MASKED_IP]`.
  - Reconstructed the log line while preserving all subsequent fields intact (`" ".join(words) + "\n"`).

## 3. Testing and Verification
- Tested with standard IPv4 addresses (`192.168.1.1`, `10.0.0.1`), out-of-range addresses (`999.1.1.1`), invalid formats (`01.1.1.1`, non-numeric strings), and empty lines.
