# ZDI-17-044: Apache Groovy MethodClosure Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-044
- **ZDI-CAN:** ZDI-CAN-3936
- **Date:** 2017-12-27
- **CVE:** CVE-2016-6814
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apache
- **Affected Products:** Groovy
- **Credit:** Sam Thomas of Secarma Limited
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-044/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apache Groovy. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on implementation. The specific flaw exists within the handling of serialized MethodClosure objects. A crafted stream of bytes, when deserialized, can result in the creation of an unsafe instance of MethodClosure. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: http://groovy-lang.org/security.html

## Disclosure Timeline

- 2016-09-19 - Vulnerability reported to vendor
- 2017-12-27 - Coordinated public release of advisory
