# ZDI-18-537: Delta Industrial Automation DOPSoft DPA File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-537
- **ZDI-CAN:** ZDI-CAN-5975
- **Date:** 2018-06-05
- **CVE:** CVE-2018-10623
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** DOPSoft
- **Credit:** b0nd @garage4hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-537/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation DOPSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of fields in DPA file. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code under the context of the current process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-151-01

## Disclosure Timeline

- 2018-04-05 - Vulnerability reported to vendor
- 2018-06-05 - Coordinated public release of advisory
- 2018-06-05 - Advisory Updated
