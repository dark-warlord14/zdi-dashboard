# ZDI-25-046: Adobe Photoshop node_modules Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-046
- **ZDI-CAN:** ZDI-CAN-25333
- **Date:** 2025-01-20
- **CVE:** CVE-2025-21127
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Photoshop
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-046/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Adobe Photoshop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the file upx.js. The product loads a JavaScript file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of a target user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/photoshop/apsb25-02.html

## Disclosure Timeline

- 2024-10-03 - Vulnerability reported to vendor
- 2025-01-20 - Coordinated public release of advisory
- 2025-01-20 - Advisory Updated
