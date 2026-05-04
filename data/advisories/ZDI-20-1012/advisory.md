# ZDI-20-1012: Parallels Desktop OEMNet Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1012
- **ZDI-CAN:** ZDI-CAN-11132
- **Date:** 2020-08-18
- **CVE:** CVE-2020-17394
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1012/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the OEMNet component. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2020-05-27 - Vulnerability reported to vendor
- 2020-08-18 - Coordinated public release of advisory
