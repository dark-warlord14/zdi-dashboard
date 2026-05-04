# ZDI-20-1019: Parallels Desktop VGA Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1019
- **ZDI-CAN:** ZDI-CAN-11363
- **Date:** 2020-08-18
- **CVE:** CVE-2020-17401
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** grigoritchy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1019/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive informations on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the VGA virtual device. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated array. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2020-07-15 - Vulnerability reported to vendor
- 2020-08-18 - Coordinated public release of advisory
