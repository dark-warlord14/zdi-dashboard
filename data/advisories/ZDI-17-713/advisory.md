# ZDI-17-713: Advantech WebAccess Product Installation File Access Control Modification Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-713
- **ZDI-CAN:** ZDI-CAN-4897
- **Date:** 2017-08-30
- **CVE:** CVE-2017-12713
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Fritz Sands - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-713/
## Vulnerability Details

This vulnerability allows local attackers to escalate privilege on vulnerable installations of Advantech WebAccess. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the access control that is set and modified during the installation of the product. The product installation weakens access control restrictions of pre-existing system files and sets weak access control restrictions on new files. An attacker can leverage this vulnerability to execute arbitrary code under the context of Administrator, the IUSR account, or SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-241-02

## Disclosure Timeline

- 2017-06-16 - Vulnerability reported to vendor
- 2017-08-30 - Coordinated public release of advisory
