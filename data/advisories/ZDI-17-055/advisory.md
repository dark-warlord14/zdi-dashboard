# ZDI-17-055: Oracle WebLogic RMI Registry UnicastRef Object Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-055
- **ZDI-CAN:** ZDI-CAN-3826
- **Date:** 2017-01-24
- **CVE:** CVE-2017-3248
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** WebLogic
- **Credit:** Tenable Network Security - Jacob Baines
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-055/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle WebLogic. Authentication is not required to exploit this vulnerability. The specific flaw exists within the insufficient blacklisting of certain Java objects. The issue lies in the failure to properly validate user-supplied data which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpujan2017-2881727.html

## Disclosure Timeline

- 2016-06-30 - Vulnerability reported to vendor
- 2017-01-24 - Coordinated public release of advisory
