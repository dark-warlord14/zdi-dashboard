# ZDI-20-1385: VMware ESXi SLP Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1385
- **ZDI-CAN:** ZDI-CAN-12409
- **Date:** 2020-11-25
- **CVE:** CVE-2020-3992
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** ESXi
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1385/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware ESXi. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of SLP messages. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2020-0023.html

## Disclosure Timeline

- 2020-11-13 - Vulnerability reported to vendor
- 2020-11-25 - Coordinated public release of advisory
