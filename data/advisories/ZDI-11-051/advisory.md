# ZDI-11-051: (0Day) IBM Lotus Notes cai URI Handler Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-051
- **ZDI-CAN:** ZDI-CAN-647
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0912
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Notes
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-051/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Notes. User interaction is required to exploit this vulnerability. The specific flaw exists within the handling of malformed strings within cai:// URIs. The '--launcher.library' switch can be injected and directed to load a DLL from a network share. This will result in code execution under the context of the current user.

## Additional Details

http://www-01.ibm.com/support/docview.wss?uid=swg21461514

## Disclosure Timeline

- 2009-12-18 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
