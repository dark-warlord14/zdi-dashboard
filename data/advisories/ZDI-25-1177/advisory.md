# ZDI-25-1177: Foxit PDF Reader U3D File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1177
- **ZDI-CAN:** ZDI-CAN-28523
- **Date:** 2025-12-19
- **CVE:** CVE-2025-66496
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Mat Powell of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1177/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of U3D files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2025-11-04 - Vulnerability reported to vendor
- 2025-12-19 - Coordinated public release of advisory
- 2025-12-19 - Advisory Updated
