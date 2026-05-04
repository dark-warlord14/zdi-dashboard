# ZDI-18-1331: Advantech WebAccess Client Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1331
- **ZDI-CAN:** ZDI-CAN-7167
- **Date:** 2018-10-31
- **CVE:** CVE-2018-17908
- **CVSS:** 8.4
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1331/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Advantech WebAccess Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the access control that is set and modified during the installation of the product. The product installation weakens access control restrictions by disabling User Account Control. An attacker can leverage this vulnerability to execute arbitrary code in the context of the Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-298-02

## Disclosure Timeline

- 2018-08-22 - Vulnerability reported to vendor
- 2018-10-31 - Coordinated public release of advisory
