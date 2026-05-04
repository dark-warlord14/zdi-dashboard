# ZDI-15-116: IBM Lotus Domino SSL2 Client Master Key Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-116
- **ZDI-CAN:** ZDI-CAN-2684
- **Date:** 2015-04-06
- **CVE:** CVE-2015-0134
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-116/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Domino. Authentication is not required to exploit this vulnerability. The flaw exists within the nldap.exe component which listens by default on TCP port 636. When handling Client Master Key Message packets, the process blindly copies attacker supplied data into an undersized buffer. A remote attacker could exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21700029

## Disclosure Timeline

- 2015-01-27 - Vulnerability reported to vendor
- 2015-04-06 - Coordinated public release of advisory
