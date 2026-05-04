# ZDI-20-011: Cisco Data Center Network Manager DbAdminRest installSwitchLicense Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-011
- **ZDI-CAN:** ZDI-CAN-9025
- **Date:** 2020-01-03
- **CVE:** CVE-2019-15980
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-011/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco Data Center Network Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the fm/fmrest/dbadmin/installSwitchLicense path in the service. When parsing the filename parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of SYSTEM.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20200102-dcnm-path-trav

## Disclosure Timeline

- 2019-08-13 - Vulnerability reported to vendor
- 2020-01-03 - Coordinated public release of advisory
