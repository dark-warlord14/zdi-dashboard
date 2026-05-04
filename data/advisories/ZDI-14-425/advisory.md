# ZDI-14-425: Trihedral VTScada Integer Overflow Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-425
- **ZDI-CAN:** ZDI-CAN-2599
- **Date:** 2014-12-12
- **CVE:** CVE-2014-9192
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Trihedral Engineering Ltd
- **Affected Products:** VTScada
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-425/
## Vulnerability Details

This vulnerability allows remote attackers to cause a denial of service to vulnerable installations of Trihedral VTScada. Authentication is not required to exploit this vulnerability. The specific flaw exists within the included HTTP server. By providing a small negative content length, an attacker is able to cause an integer overflow, resulting in the allocation of too small a buffer. The resulting heap overwrite will terminate the HTTP server.

## Additional Details

Trihedral Engineering Ltd has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-14-343-02

## Disclosure Timeline

- 2014-11-19 - Vulnerability reported to vendor
- 2014-12-12 - Coordinated public release of advisory
