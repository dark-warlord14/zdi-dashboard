# ZDI-20-1013: Parallels Desktop Networking Service Integer Underflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1013
- **ZDI-CAN:** ZDI-CAN-11134
- **Date:** 2020-08-18
- **CVE:** CVE-2020-17395
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Meysam Firouzi @R00tkitSMM
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1013/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the prl_naptd process. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2020-06-03 - Vulnerability reported to vendor
- 2020-08-18 - Coordinated public release of advisory
