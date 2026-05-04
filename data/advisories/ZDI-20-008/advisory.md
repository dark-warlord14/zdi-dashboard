# ZDI-20-008: Cisco Data Center Network Manager SecurityManager Hard-coded Cryptographic Key Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-008
- **ZDI-CAN:** ZDI-CAN-9140
- **Date:** 2020-01-03
- **CVE:** CVE-2019-15976
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-008/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Cisco Data Center Network Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the validation of SSO tokens of SOAP packets. The issue results from the use of a hard-coded key to validate the message digest. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of SYSTEM.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20200102-dcnm-auth-bypass

## Disclosure Timeline

- 2019-08-13 - Vulnerability reported to vendor
- 2020-01-03 - Coordinated public release of advisory
