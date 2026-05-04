# ZDI-26-306: Oracle VirtualBox SoundBlaster 16 Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-306
- **ZDI-CAN:** ZDI-CAN-28806
- **Date:** 2026-04-28
- **CVE:** CVE-2026-35230
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** VMBreakers(SANGBIN KIM, GANGMIN KIM, Un3xploitable)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-306/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the SoundBlaster 16 virtual device. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2026.html

## Disclosure Timeline

- 2026-03-25 - Vulnerability reported to vendor
- 2026-04-28 - Coordinated public release of advisory
- 2026-04-28 - Advisory Updated
