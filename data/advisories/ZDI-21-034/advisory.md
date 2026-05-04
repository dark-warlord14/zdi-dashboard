# ZDI-21-034: Delta Industrial Automation DOPSoft XLS File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-034
- **ZDI-CAN:** ZDI-CAN-11664
- **Date:** 2021-01-14
- **CVE:** CVE-2020-27275
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** DOPSoft
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-034/
## Vulnerability Details

This vulnerability allows remote atackers to execute arbitrary code on affected installations of Delta Industrial Automation DOPSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XLS files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://us-cert.cisa.gov/ics/advisories/icsa-21-005-05

## Disclosure Timeline

- 2020-08-28 - Vulnerability reported to vendor
- 2021-01-14 - Coordinated public release of advisory
