# ZDI-20-1380: SaltStack Salt rest_cherrypy tgt Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1380
- **ZDI-CAN:** ZDI-CAN-11167
- **Date:** 2020-11-24
- **CVE:** CVE-2020-16846
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** SaltStack
- **Affected Products:** Salt
- **Credit:** KPC of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1380/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SaltStack Salt. Authentication is not required to exploit this vulnerability. The specific flaw exists within the rest_cherrypy module. When parsing the tgt parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the salt-api process.

## Additional Details

SaltStack has issued an update to correct this vulnerability. More details can be found at: https://www.saltstack.com/blog/on-november-3-2020-saltstack-publicly-disclosed-three-new-cves/

## Disclosure Timeline

- 2020-06-12 - Vulnerability reported to vendor
- 2020-11-24 - Coordinated public release of advisory
