# ZDI-21-213: Parallels Desktop Toolgate Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-213
- **ZDI-CAN:** ZDI-CAN-12068
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27260
- **CVSS:** 3.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-213/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Toolgate component. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2020-10-06 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
