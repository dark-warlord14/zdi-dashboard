# ZDI-22-386: Parallels Desktop HDAudio Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-386
- **ZDI-CAN:** ZDI-CAN-14969
- **Date:** 2022-02-18
- **CVE:** CVE-2021-34987
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Ben McBride
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-386/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the HDAudio virtual device. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2021-09-10 - Vulnerability reported to vendor
- 2022-02-18 - Coordinated public release of advisory
