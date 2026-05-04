# ZDI-20-650: Eaton Intelligent Power Manager mc2 Incorrect Privilege Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-650
- **ZDI-CAN:** ZDI-CAN-11085
- **Date:** 2020-05-12
- **CVE:** CVE-2020-6652
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Eaton
- **Affected Products:** Intelligent Power Manager
- **Credit:** zebasquared
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-650/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Eaton Intelligent Power Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the mc2 binary. The issue results from the lack of proper validation of user privileges prior to performing privileged actions. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from non-admin users.

## Additional Details

Eaton has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-133-01

## Disclosure Timeline

- 2019-12-23 - Vulnerability reported to vendor
- 2020-05-12 - Coordinated public release of advisory
- 2020-05-12 - Advisory Updated
