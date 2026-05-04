# ZDI-11-047: (0Day) IBM Lotus Domino LDAP Bind Request Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-047
- **ZDI-CAN:** ZDI-CAN-779
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0917
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** Francis Provencher for Protek Researchh Lab's
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-047/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Domino. Authentication is not required to exploit this vulnerability. The flaw exists within the nLDAP.exe component which listens by default on TCP port 389. When handling the an LDAP Bind Request packet the process blindly copies user supplied data into an undersized shared memory buffer. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

http://www-01.ibm.com/support/docview.wss?uid=swg21461514

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
