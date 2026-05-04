# ZDI-15-117: IBM Lotus Domino LDAP ModifyRequest add Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-117
- **ZDI-CAN:** ZDI-CAN-2666
- **Date:** 2015-04-06
- **CVE:** CVE-2015-0117
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-117/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Domino. Authentication is not required to exploit this vulnerability. The specific flaw exists within LDAP handling functionality which listens by default on TCP port 389. The vulnerable code blindly copies attacker supplied data from a specially formatted LDAP ModifyRequest packet to a fixed length stack buffer. This can be leveraged by a remote attacker to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21700029

## Disclosure Timeline

- 2015-01-08 - Vulnerability reported to vendor
- 2015-04-06 - Coordinated public release of advisory
