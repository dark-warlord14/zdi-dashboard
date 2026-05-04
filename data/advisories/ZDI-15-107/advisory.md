# ZDI-15-107: SolarWinds Firewall Security Manager userlogin.jsp Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-107
- **ZDI-CAN:** ZDI-CAN-1999
- **Date:** 2015-03-13
- **CVE:** CVE-2015-2284
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SolarWinds
- **Affected Products:** Firewall Security Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-107/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Firewall Security Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of client sessions. The issue lies in the ability to elevate to administrative privileges. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://downloads.solarwinds.com/solarwinds/Release/HotFix/FSM-v6.6.5-HotFix1.zip

## Disclosure Timeline

- 2013-11-26 - Vulnerability reported to vendor
- 2015-03-13 - Coordinated public release of advisory
