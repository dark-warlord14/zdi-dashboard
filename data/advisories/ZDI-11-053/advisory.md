# ZDI-11-053: (0Day) Lotus Domino Server diiop getEnvironmentString Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-053
- **ZDI-CAN:** ZDI-CAN-758
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0913
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** Intevydis, http://intevydis.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-053/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Domino. Authentication is not required to exploit this vulnerability. The flaw exists within the ndiiop.exe component which listens by default on a dynamic TCP port. When handling a GIOP getEnvironmentString request the process blindly copies user supplied argument into an stack buffer while checking the local variable cache. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

http://www-01.ibm.com/support/docview.wss?uid=swg21461514

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
