# ZDI-18-945: Microsoft Windows NtGdiClearBitmapAttributes Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-945
- **ZDI-CAN:** ZDI-CAN-6117
- **Date:** 2018-08-14
- **CVE:** CVE-2018-8404
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** RanchoIce of Tencent ZhanluLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-945/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing a malformed bitmap handle as a parameter to the NtGdiClearBitmapAttributes API. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges to SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8404

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
