# ZDI-17-1007: QNAP QTS Web sysinfoReq Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-1007
- **ZDI-CAN:** ZDI-CAN-5279
- **Date:** 2017-12-20
- **CVE:** CVE-2017-17033
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** QNAP
- **Affected Products:** QTS
- **Credit:** @nervoir
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-1007/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of QNAP QTS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the lang parameter provided to the sysinfoReq.cgi endpoint. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/nas-201712-15

## Disclosure Timeline

- 2017-10-09 - Vulnerability reported to vendor
- 2017-12-20 - Coordinated public release of advisory
