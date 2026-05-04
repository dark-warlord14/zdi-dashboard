# ZDI-21-1289: Open Design Alliance (ODA) ODAViewer U3D File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1289
- **ZDI-CAN:** ZDI-CAN-14337
- **Date:** 2021-11-10
- **CVE:** CVE-2021-43277
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Open Design Alliance (ODA)
- **Affected Products:** ODAViewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1289/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Open Design Alliance (ODA) ODAViewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of U3D files. Crafted data in a U3D file can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Open Design Alliance (ODA) has issued an update to correct this vulnerability. More details can be found at: https://www.opendesign.com/security-advisories

## Disclosure Timeline

- 2021-07-02 - Vulnerability reported to vendor
- 2021-11-10 - Coordinated public release of advisory
