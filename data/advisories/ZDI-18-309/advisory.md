# ZDI-18-309: The Squid Software Foundation Squid Reverse Proxy sslBumpAccessCheck Null Pointer Dereference Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-309
- **ZDI-CAN:** ZDI-CAN-6088
- **Date:** 2018-04-19
- **CVE:** CVE-2018-1172
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** The Squid Software Foundation
- **Affected Products:** Squid
- **Credit:** Michael Marshall of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-309/
## Vulnerability Details

This vulnerability allows remote attackers to deny service on vulnerable installations of The Squid Software Foundation Squid. Authentication is not required to exploit this vulnerability. The specific flaw exists within ClientRequestContext::sslBumpAccessCheck(). A crafted request can trigger the dereference of a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition to users of the system.

## Additional Details

The Squid Software Foundation has issued an update to correct this vulnerability. More details can be found at: http://www.squid-cache.org/Advisories/SQUID-2018_3.txt

## Disclosure Timeline

- 2018-04-16 - Vulnerability reported to vendor
- 2018-04-19 - Coordinated public release of advisory
- 2018-04-19 - Advisory Updated
