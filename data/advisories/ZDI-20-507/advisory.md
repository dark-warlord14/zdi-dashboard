# ZDI-20-507: Oracle VirtualBox VBoxVGA VBoxVHWASurfaceBase Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-507
- **ZDI-CAN:** ZDI-CAN-10423
- **Date:** 2020-04-16
- **CVE:** CVE-2020-2758
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Calvin Fong (Lord_Idiot) of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-507/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the VBoxVGA graphics controller component. When handling the VBoxVHWASurfaceBase object, the process does not properly validate the existence of the object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2020.html

## Disclosure Timeline

- 2020-03-03 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
