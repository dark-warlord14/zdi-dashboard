# ZDI-18-946: Microsoft Windows Dxgkrnl Type Confusion Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-946
- **ZDI-CAN:** ZDI-CAN-6118
- **Date:** 2018-08-14
- **CVE:** CVE-2018-8405
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** ChenNan and RanchoIce of Tencent ZhanluLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-946/
## Vulnerability Details

This vulnerability allows attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the D3DKMTCreateAllocation method. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to escalate privileges to SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8405

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
