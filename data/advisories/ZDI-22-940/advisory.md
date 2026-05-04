# ZDI-22-940: Parallels Desktop ACPI Out-Of-Bounds Read Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-940
- **ZDI-CAN:** ZDI-CAN-16554
- **Date:** 2022-06-30
- **CVE:** CVE-2022-34889
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Ben McBride
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-940/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the ACPI virtual device. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/125013

## Disclosure Timeline

- 2022-03-02 - Vulnerability reported to vendor
- 2022-06-30 - Coordinated public release of advisory
