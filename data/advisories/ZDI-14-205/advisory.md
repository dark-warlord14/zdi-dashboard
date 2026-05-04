# ZDI-14-205: AlienVault OSSIM av-centerd Util.pm set_file Arbitrary File Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-205
- **ZDI-CAN:** ZDI-CAN-2293
- **Date:** 2014-06-13
- **CVE:** CVE-2014-4151
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** AlienVault
- **Affected Products:** OSSIM
- **Credit:** HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-205/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AlienVault OSSIM. Authentication is not required to exploit this vulnerability. The specific flaw exists within the av-centerd SOAP service. The issue lies in the handling of set_file requests allowing for an arbitrary file write with attacker controlled data. An attacker could leverage this vulnerability to execute code with root privileges.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: http://forums.alienvault.com/discussion/2806

## Disclosure Timeline

- 2014-04-18 - Vulnerability reported to vendor
- 2014-06-13 - Coordinated public release of advisory
