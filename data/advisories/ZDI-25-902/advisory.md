# ZDI-25-902: Dassault Systèmes eDrawings Viewer JT File Parsing Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-902
- **ZDI-CAN:** ZDI-CAN-27467
- **Date:** 2025-09-22
- **CVE:** CVE-2025-9450
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Dassault Systèmes
- **Affected Products:** eDrawings
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-902/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Dassault Syst��mes eDrawings Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JT files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Dassault Systèmes has issued an update to correct this vulnerability. More details can be found at: https://www.3ds.com/trust-center/security/security-advisories/cve-2025-9450

## Disclosure Timeline

- 2025-07-03 - Vulnerability reported to vendor
- 2025-09-22 - Coordinated public release of advisory
- 2025-09-22 - Advisory Updated
