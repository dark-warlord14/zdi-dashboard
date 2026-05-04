# ZDI-14-200: AlienVault OSSIM av-centerd Util.pm admin_ip Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-200
- **ZDI-CAN:** ZDI-CAN-2297
- **Date:** 2014-06-11
- **CVE:** CVE-2014-3804
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** AlienVault
- **Affected Products:** OSSIM
- **Credit:** HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-200/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AlienVault OSSIM. Authentication is not required to exploit this vulnerability. The specific flaw exists within the av-centerd SOAP service. The issue lies in the handling of the set_ossim_setup admin_ip requests due to a failure to safely sanitize user data before executing a command. An attacker could leverage this vulnerability to execute code with root privileges.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: http://forums.alienvault.com/discussion/2690

## Disclosure Timeline

- 2014-04-18 - Vulnerability reported to vendor
- 2014-06-11 - Coordinated public release of advisory
