# ZDI-24-1529: Dassault Systèmes eDrawings Viewer X_B File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1529
- **ZDI-CAN:** ZDI-CAN-25011
- **Date:** 2024-11-19
- **CVE:** CVE-2024-10204
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Dassault Systèmes
- **Affected Products:** eDrawings Viewer
- **Credit:** Andrea Micalizzi aka rgod (@rgod777)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1529/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Dassault Syst��mes eDrawings Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of X_B files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Dassault Systèmes has issued an update to correct this vulnerability. More details can be found at: https://www.cve.org/CVERecord?id=CVE-2024-10204

## Disclosure Timeline

- 2024-08-01 - Vulnerability reported to vendor
- 2024-11-19 - Coordinated public release of advisory
- 2024-11-19 - Advisory Updated
