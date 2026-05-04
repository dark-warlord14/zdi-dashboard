# ZDI-25-904: Dassault Systèmes eDrawings Viewer PAR File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-904
- **ZDI-CAN:** ZDI-CAN-27283
- **Date:** 2025-09-22
- **CVE:** CVE-2025-9447
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Dassault Systèmes
- **Affected Products:** eDrawings
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-904/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Dassault Syst��mes eDrawings Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PAR files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Dassault Systèmes has issued an update to correct this vulnerability. More details can be found at: https://www.3ds.com/trust-center/security/security-advisories/cve-2025-9447

## Disclosure Timeline

- 2025-06-17 - Vulnerability reported to vendor
- 2025-09-22 - Coordinated public release of advisory
- 2025-09-22 - Advisory Updated
