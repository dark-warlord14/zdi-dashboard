# ZDI-21-431: Parallels Desktop Toolgate Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-431
- **ZDI-CAN:** ZDI-CAN-12528
- **Date:** 2021-04-21
- **CVE:** CVE-2021-31423
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** GDPR
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-431/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Toolgate component. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2021-01-20 - Vulnerability reported to vendor
- 2021-04-21 - Coordinated public release of advisory
- 2024-02-07 - Advisory Updated
