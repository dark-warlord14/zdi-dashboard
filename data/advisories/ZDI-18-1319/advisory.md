# ZDI-18-1319: Advantech WebAccess Node Product Installation File Access Control Modification Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1319
- **ZDI-CAN:** ZDI-CAN-6828
- **Date:** 2018-10-25
- **CVE:** CVE-2018-14828
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Fritz Sands of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1319/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Advantech WebAccess Node. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the access control that is set and modified during the installation of the product. The product installation weakens access control restrictions of pre-existing system files and sets weak access control restrictions on new files. An attacker can leverage this vulnerability to escalate privileges to the level of an administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-296-01

## Disclosure Timeline

- 2018-07-17 - Vulnerability reported to vendor
- 2018-10-25 - Coordinated public release of advisory
