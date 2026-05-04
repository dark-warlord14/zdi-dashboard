# ZDI-20-012: Cisco Data Center Network Manager serverinfo Hardcoded Password Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-012
- **ZDI-CAN:** ZDI-CAN-9037
- **Date:** 2020-01-03
- **CVE:** CVE-2019-15977
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-012/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Cisco Data Center Network Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of web requests. The system contains a hard-coded administrator username and password that can be used to bypass authentication for some functions. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of SYSTEM.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20200102-dcnm-auth-bypass

## Disclosure Timeline

- 2019-08-13 - Vulnerability reported to vendor
- 2020-01-03 - Coordinated public release of advisory
