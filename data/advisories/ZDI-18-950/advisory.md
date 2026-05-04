# ZDI-18-950: Microsoft Windows dxgkrnl Driver D3DKMTRender Method Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-950
- **ZDI-CAN:** ZDI-CAN-6120
- **Date:** 2018-08-14
- **CVE:** CVE-2018-8400
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** RanchoIce and ChenNan of Tencent ZhanluLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-950/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the D3DKMTRender routine in the dxgkrnl driver. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to escalate privileges to SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8400

## Disclosure Timeline

- 2018-05-03 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
