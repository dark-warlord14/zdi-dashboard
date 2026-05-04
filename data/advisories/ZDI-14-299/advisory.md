# ZDI-14-299: SolarWinds Storage Manager AuthenticationFilter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-299
- **ZDI-CAN:** ZDI-CAN-2087
- **Date:** 2014-08-27
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SolarWinds
- **Affected Products:** Storage Manager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-299/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Storage Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AuthenticationFilter class. The issue lies in the ability to subvert the authentication filter. An attacker can leverage this vulnerability to upload malicious scripts that can then be used to execute code under the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://www.solarwinds.com/documentation/storage/storagemanager/docs/releasenotes/releasenotes.htm

## Disclosure Timeline

- 2014-02-16 - Vulnerability reported to vendor
- 2014-08-27 - Coordinated public release of advisory
