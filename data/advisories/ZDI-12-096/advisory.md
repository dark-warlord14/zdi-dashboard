# ZDI-12-096: HP Data Protector Express Opcode 0x330 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-096
- **ZDI-CAN:** ZDI-CAN-1393
- **Date:** 2012-06-21
- **CVE:** CVE-2012-0122
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector Express
- **Credit:** e6af8de8b1d4b2b6d5ba2610cbf9cd38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-096/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Data Protector Express. Authentication is not required to exploit this vulnerability. User interaction is not required to exploit this vulnerability. The specific flaw exists within the dpwinsdr.exe process which listens on TCP port 3817 by default. The process has insufficient bounds checking on user-supplied data copied to a fixed-length buffer on the stack. Remote, unauthenticated attackers can exploit this vulnerability by sending malformed opcode 0x330 message packets to the target, which could ultimately lead to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03229235

## Disclosure Timeline

- 2011-11-29 - Vulnerability reported to vendor
- 2012-06-21 - Coordinated public release of advisory
