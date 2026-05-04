# ZDI-21-472: Autodesk FBX Review FBX File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-472
- **ZDI-CAN:** ZDI-CAN-12613
- **Date:** 2021-04-23
- **CVE:** CVE-2021-27027
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Autodesk
- **Affected Products:** FBX Review
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-472/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Autodesk FBX Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of FBX files. Crafted data in an FBX file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2021-0001

## Disclosure Timeline

- 2021-01-21 - Vulnerability reported to vendor
- 2021-04-23 - Coordinated public release of advisory
