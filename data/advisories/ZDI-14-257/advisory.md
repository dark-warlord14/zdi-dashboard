# ZDI-14-257: Oracle Business Intelligence Mobile App Designer UIXCacheResourceServlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-257
- **ZDI-CAN:** ZDI-CAN-2107
- **Date:** 2014-07-18
- **CVE:** CVE-2014-4249
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Business Intelligence
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-257/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Business Intelligence Mobile App Designer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UIXCacheResourceServlet servlet. The issue lies in the ability to download arbitrary files using a directory traversal vulnerability. A remote attacker can abuse this to disclose sensitive information that could result in remote code under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujul2014-1972956.html

## Disclosure Timeline

- 2014-01-30 - Vulnerability reported to vendor
- 2014-07-18 - Coordinated public release of advisory
