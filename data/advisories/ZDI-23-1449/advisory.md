# ZDI-23-1449: (0Day) Intel Driver & Support Assistant Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1449
- **ZDI-CAN:** ZDI-CAN-21846
- **Date:** 2023-09-21
- **CVE:** CVE-2023-42099
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Intel
- **Affected Products:** Driver & Support Assistant
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1449/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Intel Driver & Support Assistant. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the DSA Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

09/13/23 – ZDI reported the vulnerability to the vendor. 09/14/23 – The vendor states they are rejecting the case as it is out of the scope of the Intel Bug Bounty Program. 09/14/23 – ZDI provided additional details on why this vulnerability should be remediated and that we intend to publish the case as a zero-day advisory on 09/21/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-09-13 - Vulnerability reported to vendor
- 2023-09-21 - Coordinated public release of advisory
