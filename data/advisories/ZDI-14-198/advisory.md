# ZDI-14-198: AlienVault OSSIM av-centerd Util.pm update_system/upgrade_pro_web Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-198
- **ZDI-CAN:** ZDI-CAN-2282
- **Date:** 2014-06-11
- **CVE:** CVE-2014-3805
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** AlienVault
- **Affected Products:** OSSIM
- **Credit:** agix
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-198/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AlienVault Ossim. Authentication is not required to exploit this vulnerability. The specific flaw exists within the av-centerd SOAP service. The issue lies in the handling of the update_system/upgrade_pro_web requests due to a failure to safely sanitize user data before executing a command. An attacker could leverage this vulnerability to execute code with root privileges.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: http://forums.alienvault.com/discussion/2690

## Disclosure Timeline

- 2014-04-18 - Vulnerability reported to vendor
- 2014-06-11 - Coordinated public release of advisory
