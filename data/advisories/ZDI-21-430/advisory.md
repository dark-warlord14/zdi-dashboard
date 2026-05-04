# ZDI-21-430: Parallels Desktop e1000e Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-430
- **ZDI-CAN:** ZDI-CAN-12527
- **Date:** 2021-04-21
- **CVE:** CVE-2021-31422
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** GDPR
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-430/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the e1000e virtual device. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2021-01-20 - Vulnerability reported to vendor
- 2021-04-21 - Coordinated public release of advisory
- 2024-02-07 - Advisory Updated
