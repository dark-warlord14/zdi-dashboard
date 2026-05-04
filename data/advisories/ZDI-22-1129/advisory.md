# ZDI-22-1129: AVEVA Edge APP File Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1129
- **ZDI-CAN:** ZDI-CAN-17370
- **Date:** 2022-08-23
- **CVE:** CVE-2022-36970
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** AVEVA
- **Affected Products:** Edge
- **Credit:** Aaron Ferber
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1129/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of AVEVA Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of APP files. Crafted data in a APP file can cause the application to execute arbitrary Visual Basic scripts. The user interface fails to provide sufficient indication of the hazard. An attacker can leverage this vulnerability to execute code in the context of current process.

## Additional Details

AVEVA has issued an update to correct this vulnerability. More details can be found at: https://www.aveva.com/content/dam/aveva/documents/support/cyber-security-updates/SecurityBulletin_AVEVA-2022-005.pdf

## Disclosure Timeline

- 2022-06-28 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
