# ZDI-07-002: CA BrightStor ARCserve Backup Tape Engine Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-002
- **ZDI-CAN:** ZDI-CAN-118
- **Date:** 2007-01-11
- **CVE:** CVE-2007-0168
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** BrightStor ARCserve Server
- **Credit:** LSsecurity - LSsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-002/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Computer Associates BrightStor ARCserve Backup. User interaction is not required to exploit this vulnerability. The specific flaw exists in the handling of RPC requests to the Tape Engine service which listens by default on TCP port 6502 with the following UUID: 62b93df0-8b02-11ce-876c-00805f842837 The handler function for RPC opnum 0xBF directly calls user-supplied data in the RPC request, resulting in trivial arbitrary code execution.

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: http://supportconnectw.ca.com/public/storage/infodocs/babimpsec-notice.asp

## Disclosure Timeline

- 2006-11-01 - Vulnerability reported to vendor
- 2007-01-11 - Coordinated public release of advisory
