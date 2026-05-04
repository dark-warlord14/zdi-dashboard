# ZDI-18-500: Advantech WebAccess Node Product Installation File Access Control Modification Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-500
- **ZDI-CAN:** ZDI-CAN-5670
- **Date:** 2018-05-18
- **CVE:** CVE-2018-8841
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess Node
- **Credit:** Fritz Sands of the Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-500/
## Vulnerability Details

This vulnerability allows local attackers to escalate privilege on vulnerable installations of Advantech WebAccess Node. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the access control that is set and modified during the installation of the product. The product installation weakens access control restrictions of pre-existing system files and sets weak access control restrictions on new files. An attacker can leverage this vulnerability to execute arbitrary code under the context of Administrator, the IUSR account, or SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-135-01

## Disclosure Timeline

- 2018-02-23 - Vulnerability reported to vendor
- 2018-05-18 - Coordinated public release of advisory
- 2018-05-18 - Advisory Updated
