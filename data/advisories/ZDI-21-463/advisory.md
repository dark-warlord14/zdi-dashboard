# ZDI-21-463: X.Org Server XChangeFeedbackControl Integer Underflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-463
- **ZDI-CAN:** ZDI-CAN-12549
- **Date:** 2021-04-22
- **CVE:** CVE-2021-3472
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-463/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of XChangeFeedbackControl requests. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://lists.x.org/archives/xorg-announce/2021-April/003080.html

## Disclosure Timeline

- 2020-12-16 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
