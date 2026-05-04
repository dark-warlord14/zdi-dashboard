# ZDI-25-618: Dassault Systèmes eDrawings Viewer JT File Parsing Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-618
- **ZDI-CAN:** ZDI-CAN-26895
- **Date:** 2025-07-17
- **CVE:** CVE-2025-6974
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Dassault Systèmes
- **Affected Products:** eDrawings
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-618/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Dassault Syst��mes eDrawings Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JT files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Dassault Systèmes has issued an update to correct this vulnerability. More details can be found at: https://www.3ds.com/trust-center/security/security-advisories/CVE-2025-6974

## Disclosure Timeline

- 2025-04-17 - Vulnerability reported to vendor
- 2025-07-17 - Coordinated public release of advisory
- 2025-07-17 - Advisory Updated
