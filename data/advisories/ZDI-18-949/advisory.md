# ZDI-18-949: Microsoft Windows D3DKMTSubmitCommand BasicRender Driver Out-of-bounds Memory Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-949
- **ZDI-CAN:** ZDI-CAN-6148
- **Date:** 2018-08-14
- **CVE:** CVE-2018-8401
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** RanchoIce and ChenNan of Tencent ZhanluLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-949/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within processing of data from the D3DKMTSubmitCommand API by the BasicRender device driver. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges to SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8401

## Disclosure Timeline

- 2018-05-03 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
