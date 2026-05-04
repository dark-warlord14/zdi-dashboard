# ZDI-16-660: Delta Industrial Automation WPLSoft File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-660
- **ZDI-CAN:** ZDI-CAN-3914
- **Date:** 2016-12-15
- **CVE:** CVE-2016-5802
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** WPLSoft
- **Credit:** axt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-660/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation WPLSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of dvp files. The issue lies in the failure to properly validate user-supplied data which can result in a write outside the bounds of an allocated data structure. An attacker can leverage this vulnerability to execute arbitrary code under the context of current process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-348-03

## Disclosure Timeline

- 2016-08-30 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
