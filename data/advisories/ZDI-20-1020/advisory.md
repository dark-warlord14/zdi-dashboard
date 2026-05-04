# ZDI-20-1020: Parallels Desktop prl_hypervisor Incorrect Permission Assignment for Critical Resource Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1020
- **ZDI-CAN:** ZDI-CAN-11063
- **Date:** 2020-08-18
- **CVE:** CVE-2020-17402
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1020/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the prl_hypervisor kext. By examining a log file, an attacker can disclose a memory address. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2020-07-15 - Vulnerability reported to vendor
- 2020-08-18 - Coordinated public release of advisory
- 2024-07-08 - Advisory Updated
