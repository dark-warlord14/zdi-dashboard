# ZDI-07-004: CA BrightStor ARCserve Backup Tape Engine Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-004
- **ZDI-CAN:** ZDI-CAN-130
- **Date:** 2007-01-11
- **CVE:** CVE-2007-0169
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** BrightStor ARCserve Server
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-004/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Computer Associates BrightStor ARCserve Backup. User interaction is not required to exploit this vulnerability. The specific flaw exists in the Tape Engine RPC service which listens by default on TCP port 6503 with the following UUID: 2b93df0-8b02-11ce-876c-00805f842837 The service exposes a buffer overflow in the handler for RPC opnum 0xCF that allows for arbitrary code execution when handling user-supplied data from the RPC request.

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: http://supportconnectw.ca.com/public/storage/infodocs/babimpsec-notice.asp

## Disclosure Timeline

- 2006-11-08 - Vulnerability reported to vendor
- 2007-01-11 - Coordinated public release of advisory
