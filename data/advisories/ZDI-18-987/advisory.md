# ZDI-18-987: Delta Industrial Automation CNCSoft ScreenEditor DPB File MarcoAlarm wMessageLen Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-987
- **ZDI-CAN:** ZDI-CAN-6303
- **Date:** 2018-09-05
- **CVE:** CVE-2018-10598
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** CNCSoft
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-987/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Delta Industrial Automation CNCSoft ScreenEditor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of DPB files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the administrator.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-219-01

## Disclosure Timeline

- 2018-05-29 - Vulnerability reported to vendor
- 2018-09-05 - Coordinated public release of advisory
- 2018-09-05 - Advisory Updated
