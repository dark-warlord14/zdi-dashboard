# ZDI-09-068: EMC RepliStor Server Service DoASOCommand Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-068
- **ZDI-CAN:** ZDI-CAN-452
- **Date:** 2009-04-07
- **CVE:** CVE-2009-1120
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** EMC
- **Affected Products:** RepliStor
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-068/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC RepliStor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DoRcvRpcCall RPC function exposed via the rep_srv.exe process which listens by default on TCP port 7144. The function responsible for handling opcode 36 calls CreateProcessW with user-supplied arguments. A malicious attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

EMC has released a Security Alert (ESA) identifier ESA-09-003 to customers through Powerlink.

## Disclosure Timeline

- 2009-03-13 - Vulnerability reported to vendor
- 2009-04-07 - Coordinated public release of advisory
