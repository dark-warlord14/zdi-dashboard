# ZDI-20-102: Cisco Data Center Network Manager createLanFabric Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-102
- **ZDI-CAN:** ZDI-CAN-9286
- **Date:** 2020-01-03
- **CVE:** CVE-2019-15978
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-102/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco Data Center Network Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the processing of requests to the fabrics endpoint. When parsing the name parameter in the createLanFabric method, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20200102-dcnm-comm-inject

## Disclosure Timeline

- 2019-09-27 - Vulnerability reported to vendor
- 2020-01-03 - Coordinated public release of advisory
