# ZDI-21-1395: OpenText Brava! Desktop GIF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1395
- **ZDI-CAN:** ZDI-CAN-14096
- **Date:** 2021-12-03
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** OpenText
- **Affected Products:** Brava! Desktop
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1395/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of OpenText Brava! Desktop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of GIF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Fixed in version 16.6.5.

## Disclosure Timeline

- 2021-06-16 - Vulnerability reported to vendor
- 2021-12-03 - Coordinated public release of advisory
