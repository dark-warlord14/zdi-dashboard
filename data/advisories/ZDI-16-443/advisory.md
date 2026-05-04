# ZDI-16-443: Oracle WebLogic JBoss Interceptors Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-443
- **ZDI-CAN:** ZDI-CAN-3497
- **Date:** 2016-07-21
- **CVE:** CVE-2016-3510
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** WebLogic
- **Credit:** Alvaro Munoz (@pwntester) & Christian Schneider (@cschneider4711)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-443/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle WebLogic. Authentication is not required to exploit this vulnerability. The specific flaw exists in the use of JBoss Interceptors library. By sending a specially crafted request, the application can be made to deserialize untrusted data during the handling of the request. An attacker can leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpujul2016-2881720.html

## Disclosure Timeline

- 2016-02-16 - Vulnerability reported to vendor
- 2016-07-21 - Coordinated public release of advisory
