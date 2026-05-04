# ZDI-21-1171: Fatek Automation WinProladder PDW File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1171
- **ZDI-CAN:** ZDI-CAN-13744
- **Date:** 2021-10-14
- **CVE:** CVE-2021-38440
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Fatek Automation
- **Affected Products:** WinProladder
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1171/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Fatek Automation WinProladder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDW files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Fatek Automation has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-280-06

## Disclosure Timeline

- 2021-05-13 - Vulnerability reported to vendor
- 2021-10-14 - Coordinated public release of advisory
