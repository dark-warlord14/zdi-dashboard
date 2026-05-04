# ZDI-11-061: (0Day) EMC Replication Manager Client irccd.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-061
- **ZDI-CAN:** ZDI-CAN-614
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0647
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** Replication Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-061/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the EMC Replication Manager Client. Authentication is not required to exploit this vulnerability. The Replication Manager client installs a service binds the irccd.exe process to TCP port 6542. This service accepts commands using an XML-based protocol. It exposes a vulnerability through it's RunProgram functionality. By abusing this function an attacker can execute arbitrary code under the context of currently logged in user.

## Additional Details

April 4, 2011: EMC released the update for Networker Module for Microsoft Applications. Advisory can be found at: http://www.securityfocus.com/archive/1/517250 February 7, 2011: EMC has stated that this vulnerability has been fixed in EMC Replication Manager version 5.3 available through EMC Powerlink. However, the bug is still present in the EMC Networker Module for Microsoft Applications. It will be fixed in these products at a later date. EMC has released Security Advisory ESA-2011-004 to address this issue (covering CVE-2011-0647).

## Disclosure Timeline

- 2009-10-27 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
