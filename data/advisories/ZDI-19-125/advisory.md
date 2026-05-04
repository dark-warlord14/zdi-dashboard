# ZDI-19-125: (Pwn2Own) Apple iOS mediaserverd crte Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-125
- **ZDI-CAN:** ZDI-CAN-7474
- **Date:** 2019-01-24
- **CVE:** CVE-2019-6221
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** iOS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-125/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple iOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of crte messages within the mediaserverd service. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-11-15 - Vulnerability reported to vendor
- 2019-01-24 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated
