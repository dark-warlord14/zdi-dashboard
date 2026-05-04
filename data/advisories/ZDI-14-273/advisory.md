# ZDI-14-273: AlienVault OSSIM av-centerd Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-273
- **ZDI-CAN:** ZDI-CAN-2193
- **Date:** 2014-08-01
- **CVE:** CVE-2014-5158
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** AlienVault
- **Affected Products:** OSSIM
- **Credit:** grimmlin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-273/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AlienVault OSSIM. Authentication is not required to exploit this vulnerability. The specific flaw exists within the av-centerd SOAP service. The issue lies in the handling of the requests due to a failure to safely sanitize user data before executing a command. An attacker could leverage this vulnerability to execute code with root privileges.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: http://forums.alienvault.com/discussion/2559/security-advisory-multiple-vulnerabilities

## Disclosure Timeline

- 2014-05-25 - Vulnerability reported to vendor
- 2014-08-01 - Coordinated public release of advisory
