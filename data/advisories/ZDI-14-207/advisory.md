# ZDI-14-207: AlienVault OSSIM av-centerd Util.pm get_file Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-207
- **ZDI-CAN:** ZDI-CAN-2289
- **Date:** 2014-06-13
- **CVE:** CVE-2014-4153
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** AlienVault
- **Affected Products:** OSSIM
- **Credit:** HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-207/
## Vulnerability Details

This vulnerability allows remote attackers to obtain sensitive information on vulnerable installations of AlienVault OSSIM. Authentication is not required to exploit this vulnerability. The specific flaw exists within the av-centerd SOAP service. The issue lies within the improper handling of a parameter in get_file requests. An attacker can leverage this vulnerability to read arbitrary files from the underlying OS with root privileges.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: http://forums.alienvault.com/discussion/2806

## Disclosure Timeline

- 2014-04-18 - Vulnerability reported to vendor
- 2014-06-13 - Coordinated public release of advisory
