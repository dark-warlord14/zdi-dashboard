# ZDI-16-652: Delta Industrial Automation WPLSoft SFC File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-652
- **ZDI-CAN:** ZDI-CAN-3861
- **Date:** 2016-12-15
- **CVE:** CVE-2016-5802
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** WPLSoft
- **Credit:** axt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-652/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation WPLSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within parsing a SFC file. The process does not properly validate user-supplied data which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-348-03

## Disclosure Timeline

- 2016-07-29 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
