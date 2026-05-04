# ZDI-07-003: CA BrightStor ARCserve Backup Message Engine Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-003
- **ZDI-CAN:** ZDI-CAN-129
- **Date:** 2007-01-11
- **CVE:** CVE-2007-0169
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** BrightStor ARCserve Server
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-003/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Computer Associates BrightStor ARCserve Backup. User interaction is not required to exploit this vulnerability. The specific flaws exists in the Message Engine RPC service which listens by default on TCP ports 6503 and 6504 with the following UUIDs: dc246bf0-7a7a-11ce-9f88-00805fe43838 506b1890-14c8-11d1-bbc3-00805fa6962e The service exposes buffer overflow vulnerabilities in the handlers for RPC opnums 0x2F and 0x75 that allow for arbitrary code execution when handling user-supplied data from the RPC request.

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: http://supportconnectw.ca.com/public/storage/infodocs/babimpsec-notice.asp

## Disclosure Timeline

- 2006-11-08 - Vulnerability reported to vendor
- 2007-01-11 - Coordinated public release of advisory
