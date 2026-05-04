# ZDI-20-785: VMware Workstation SVGA DXInvalidateContext Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-785
- **ZDI-CAN:** ZDI-CAN-10786
- **Date:** 2020-06-30
- **CVE:** CVE-2020-3962
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Corentin Bayet (@OnlyTheDuck) and Bruno Pujos (@BrunoPujos) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-785/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware Workstation. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the handling of the SVGA DXInvalidateContext command. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2020-0015.html

## Disclosure Timeline

- 2020-06-26 - Vulnerability reported to vendor
- 2020-06-30 - Coordinated public release of advisory
