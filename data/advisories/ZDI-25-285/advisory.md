# ZDI-25-285: Dassault Systèmes eDrawings Viewer SLDPRT File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-285
- **ZDI-CAN:** ZDI-CAN-26029
- **Date:** 2025-05-13
- **CVE:** CVE-2025-1884
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Dassault Systèmes
- **Affected Products:** eDrawings
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-285/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Dassault Syst��mes eDrawings Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SLDPRT files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Dassault Systèmes has issued an update to correct this vulnerability. More details can be found at: https://www.cve.org/CVERecord?id=CVE-2025-1884

## Disclosure Timeline

- 2025-01-30 - Vulnerability reported to vendor
- 2025-05-13 - Coordinated public release of advisory
- 2025-05-13 - Advisory Updated
