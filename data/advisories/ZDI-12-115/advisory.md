# ZDI-12-115: HP OpenView Performance Agent coda.exe Opcode 0x8C Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-115
- **ZDI-CAN:** ZDI-CAN-1326
- **Date:** 2012-07-12
- **CVE:** CVE-2012-2020
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Performance Agent
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-115/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP OpenView Performance Agent. Authentication is not required to exploit this vulnerability. The specific flaw exists within the coda.exe process which listens on a random TCP port by default. The process trusts a value within a GET request as a size. It then proceeds to copy that many bytes of user-supplied data into a fixed-length buffer on the stack. Remote unauthenticated attackers can exploit this vulnerability by sending malformed message packets to the target, which could ultimately lead to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay?docId=emr_na-c03397769

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2012-07-12 - Coordinated public release of advisory
