# ZDI-13-210: ISC BIND rdata Denial Of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-210
- **ZDI-CAN:** ZDI-CAN-1911
- **Date:** 2013-08-13
- **CVE:** CVE-2013-4854
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** ISC
- **Affected Products:** BIND
- **Credit:** Maxim Shudrak
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-210/
## Vulnerability Details

This vulnerability allows remote attackers to cause a denial of service condition on vulnerable installations of ISC BIND. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of an rdata section with a length that is less than four. The issue lies in the creation of an error message when an invalid message class is specified. An attacker can leverage this vulnerability to crash a remote instance of ISC BIND.

## Additional Details

ISC has issued an update to correct this vulnerability. More details can be found at: https://kb.isc.org/article/AA-01015/0/CVE-2013-4854%3A-A-specially-crafted-query-can-cause-BIND-to-terminate-abnormally.html

## Disclosure Timeline

- 2013-07-15 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
