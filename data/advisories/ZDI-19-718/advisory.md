# ZDI-19-718: Delta Industrial Automation DOPSoft DPA File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-718
- **ZDI-CAN:** ZDI-CAN-8251
- **Date:** 2019-08-16
- **CVE:** CVE-2019-13513
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** DOPSoft
- **Credit:** kimiya of 9SG Security Team - kimiya@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-718/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected instances of Delta Industrial Automation DOPSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPA files. The issue results from the lack of proper validation of user-supplied data, which can result in a read before the start of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-225-01

## Disclosure Timeline

- 2019-03-27 - Vulnerability reported to vendor
- 2019-08-16 - Coordinated public release of advisory
