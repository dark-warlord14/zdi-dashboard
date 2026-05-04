# ZDI-16-648: Delta Industrial Automation WPLSoft DVP File Parsing Heap-Based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-648
- **ZDI-CAN:** ZDI-CAN-3865
- **Date:** 2016-12-15
- **CVE:** CVE-2016-5805
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** WPLSoft
- **Credit:** axt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-648/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation WPLSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within parsing of a DVP file. The process does not properly validate the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-348-03

## Disclosure Timeline

- 2016-07-21 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
