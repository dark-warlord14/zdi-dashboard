# ZDI-11-052: (0Day) Lotus Domino Server diiop Client Request Operation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-052
- **ZDI-CAN:** ZDI-CAN-759
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0914
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** Intevydis http://intevydis.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-052/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Domino. Authentication is not required to exploit this vulnerability. The flaw exists within the ndiiop.exe component which listens by default on a dynamic TCP port. When handling a GIOP client Request packet type the process can be made to mis-allocate a buffer size due to a signed-ness bug. Later, the process blindly copies user supplied data into this under allocated heap buffer. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

http://www-01.ibm.com/support/docview.wss?uid=swg21461514

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
