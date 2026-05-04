# ZDI-21-1071: Schneider Electric Struxureware Data Center Expert Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1071
- **ZDI-CAN:** ZDI-CAN-13077
- **Date:** 2021-09-15
- **CVE:** CVE-2021-22794
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** Struxureware Data Center Expert
- **Credit:** David Yesland
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1071/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric Struxureware Data Center Expert. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of firmware updates. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-257-03

## Disclosure Timeline

- 2021-04-14 - Vulnerability reported to vendor
- 2021-09-15 - Coordinated public release of advisory
