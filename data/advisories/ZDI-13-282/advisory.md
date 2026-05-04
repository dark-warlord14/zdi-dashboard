# ZDI-13-282: EMC Connectrix Manager Converged Network Edition inmservlets.war Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-282
- **ZDI-CAN:** ZDI-CAN-1749
- **Date:** 2013-12-18
- **CVE:** CVE-2013-6810
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** EMC
- **Affected Products:** Connectrix Manager Converged Network Edition
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-282/
## Vulnerability Details

This vulnerability allows remote attackers to read arbitrary text files on vulnerable installations of EMC Connectrix Manager Converged Network Edition. Authentication is not required to exploit this vulnerability. The specific flaw exists within one of the pages served as part of the immservlets which allows an unauthenticated user to read an arbitrary text file anywhere on the system. An attacker can use this to either disclose sensitive data, or to disclose information about the server that can be used in a subsequent attack.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://my.brocade.com/wps/myportal/!ut/p/b1/04_SjzQ0MzEwM7S0sDDSj9CPykssy0xPLMnMz0vMAfGjzOKd3BzDjE2MjQ39vbycDTzdXYJCLb18jQx8zIAKIoEKDHAARwNC-sP1o_ArMYEqwGOFn0d-bqp-blSOpaeuoyIA_fi0nA!!/dl4/d5/L2dJQSEvUUt3QS80SmtFL1o2X0JGQVYzNDMzMU9KSkMwSUdEUlU5Sk0yMDcx/

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-12-18 - Coordinated public release of advisory
