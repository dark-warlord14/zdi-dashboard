# ZDI-23-1479: (0Day) Control Web Panel wloggui Command Injection Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1479
- **ZDI-CAN:** ZDI-CAN-21079
- **Date:** 2023-09-27
- **CVE:** CVE-2023-42122
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Control Web Panel
- **Affected Products:** Control Web Panel
- **Credit:** Muhammad Ikhsanudin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1479/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Control Web Panel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the cwpsrv process, which listens on the loopback interface. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

05/09/23 – ZDI requested a PSIRT contact. 05/10/23 – The vendor provided a contact, and ZDI reported the vulnerability to the vendor. 09/22/23 – ZDI asked for an update and informed the vendor that we intend to publish the case as a zero-day advisory on 09/27/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-05-10 - Vulnerability reported to vendor
- 2023-09-27 - Coordinated public release of advisory
