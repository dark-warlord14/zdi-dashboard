# ZDI-15-365: Apache Groovy Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-365
- **ZDI-CAN:** ZDI-CAN-2947
- **Date:** 2015-07-20
- **CVE:** CVE-2015-3253
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Elastic
- **Affected Products:** Groovy, Elasticsearch
- **Credit:** cpnrodzc7
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-365/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apache Groovy. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Closure implementation which accepts and deserializes a Java serialized binary stream. An attacker can leverage this vulnerability to execute arbitrary code under the context of the user.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: http://groovy-lang.org/security.html Elastic has issued an update to correct this vulnerability. More details can be found at: https://www.elastic.co/community/security

## Disclosure Timeline

- 2015-06-30 - Vulnerability reported to vendor
- 2015-07-20 - Coordinated public release of advisory
