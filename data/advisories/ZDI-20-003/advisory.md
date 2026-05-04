# ZDI-20-003: Cisco Data Center Network Manager TrustedClientTokenValidator Hard-coded Cryptographic Key Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-003
- **ZDI-CAN:** ZDI-CAN-9021
- **Date:** 2020-01-03
- **CVE:** CVE-2019-15975
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-003/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Cisco Data Center Network Manager. The specific flaw exists within the processing of the dbadmin/addUser functionality. The issue results from trusting input that has been encrypted with a hard-coded and discoverable cryptographic key. An attacker can leverage this vulnerability to add new global admins to the system.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20200102-dcnm-auth-bypass

## Disclosure Timeline

- 2019-08-09 - Vulnerability reported to vendor
- 2020-01-03 - Coordinated public release of advisory
