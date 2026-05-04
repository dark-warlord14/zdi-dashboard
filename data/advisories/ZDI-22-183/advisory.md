# ZDI-22-183: Bentley MicroStation CONNECT OBJ File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-183
- **ZDI-CAN:** ZDI-CAN-15390
- **Date:** 2022-01-31
- **CVE:** CVE-2021-46596
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Bentley
- **Affected Products:** MicroStation CONNECT
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-183/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Bentley MicroStation CONNECT. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of OBJ files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Bentley has issued an update to correct this vulnerability. More details can be found at: https://www.bentley.com/en/common-vulnerability-exposure/BE-2021-0007

## Disclosure Timeline

- 2021-10-01 - Vulnerability reported to vendor
- 2022-01-31 - Coordinated public release of advisory
