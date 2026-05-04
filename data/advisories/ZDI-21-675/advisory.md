# ZDI-21-675: Schneider Electric IGSS WSP and CGF File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-675
- **ZDI-CAN:** ZDI-CAN-13657
- **Date:** 2021-06-10
- **CVE:** CVE-2021-22762
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-675/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric IGSS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of WSP and CGF files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-159-04

## Disclosure Timeline

- 2021-05-12 - Vulnerability reported to vendor
- 2021-06-10 - Coordinated public release of advisory
