# ZDI-22-1042: ICONICS GENESIS64 colorpalletes Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1042
- **ZDI-CAN:** ZDI-CAN-16509
- **Date:** 2022-08-03
- **CVE:** CVE-2022-29834
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** ICONICS
- **Affected Products:** GENESIS64
- **Credit:** Chris Anastasio and Steven Seeley of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1042/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of ICONICS GENESIS64. Authentication is not required to exploit this vulnerability. The specific flaw exists within the colorpalletes endpoint. When parsing the path parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

ICONICS has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-202-04

## Disclosure Timeline

- 2022-03-30 - Vulnerability reported to vendor
- 2022-08-03 - Coordinated public release of advisory
