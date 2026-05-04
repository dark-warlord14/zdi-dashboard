# ZDI-13-086: Microsoft HTTP.SYS Remote Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-086
- **ZDI-CAN:** ZDI-CAN-1804
- **Date:** 2013-05-29
- **CVE:** CVE-2013-1305
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Information Services
- **Credit:** Marek Kroemeke 22733db72ab3ed94b5f8a1ffcde850251fe6f466 AKAT-1
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-086/
## Vulnerability Details

This vulnerability allows remote attackers to cause a denial of service condition on vulnerable installations of IIS. No user interaction is required to exploit this vulnerability. The specific flaw exists within handling of HTTP headers in the Windows kernel. By providing a duplicate of a particular header, an attacker is able to cause an infinite loop in the HTTP header parser. This will fully exhaust the resources of one processor on the vulnerable server and will prevent IIS from responding to any other requests.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-039

## Disclosure Timeline

- 2013-03-22 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
