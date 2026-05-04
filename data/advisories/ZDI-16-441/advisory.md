# ZDI-16-441: Oracle WebLogic JtaTransactionManager Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-441
- **ZDI-CAN:** ZDI-CAN-3588
- **Date:** 2016-07-21
- **CVE:** CVE-2016-3586
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** WebLogic
- **Credit:** Alvaro Munoz (@pwntester) & Christian Schneider (@cschneider4711)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-441/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle WebLogic. Authentication is not required to exploit this vulnerability. The specific flaw exists within the use of JtaTransactionManager. It is possible to execute arbitrary commands upon deserialization. The attacker can leverage this vulnerability to execute code in the context of the process.

## Disclosure Timeline

- 2016-04-13 - Vulnerability reported to vendor
- 2016-07-21 - Coordinated public release of advisory
