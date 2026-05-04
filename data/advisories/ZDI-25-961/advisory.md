# ZDI-25-961: Oracle VirtualBox USB Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-961
- **ZDI-CAN:** ZDI-CAN-27933
- **Date:** 2025-10-27
- **CVE:** CVE-2025-62641
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** VMBreakers(SANGBIN KIM, GANGMIN KIM, Un3xploitable)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-961/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the USB device. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2025.html

## Disclosure Timeline

- 2025-09-25 - Vulnerability reported to vendor
- 2025-10-27 - Coordinated public release of advisory
- 2025-10-27 - Advisory Updated
