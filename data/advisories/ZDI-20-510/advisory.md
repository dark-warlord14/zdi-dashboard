# ZDI-20-510: Oracle VirtualBox VBoxSVGA Type Confusion Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-510
- **ZDI-CAN:** ZDI-CAN-10742
- **Date:** 2020-04-16
- **CVE:** CVE-2020-2907
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Barakat Soror
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-510/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the SVGA rendering command SVGA_3D_CMD_DRAW_PRIMITIVES. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2020.html

## Disclosure Timeline

- 2020-04-02 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
