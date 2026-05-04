# ZDI-25-286: Dassault Systèmes eDrawings Viewer OBJ File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-286
- **ZDI-CAN:** ZDI-CAN-26017
- **Date:** 2025-05-13
- **CVE:** CVE-2025-1883
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Dassault Systèmes
- **Affected Products:** eDrawings
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-286/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Dassault Syst��mes eDrawings Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of OBJ files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Dassault Systèmes has issued an update to correct this vulnerability. More details can be found at: https://www.cve.org/CVERecord?id=CVE-2025-1883

## Disclosure Timeline

- 2025-01-30 - Vulnerability reported to vendor
- 2025-05-13 - Coordinated public release of advisory
- 2025-05-13 - Advisory Updated
