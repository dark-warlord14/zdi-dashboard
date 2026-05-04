# ZDI-17-1005: QNAP QTS authLogin Host Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-1005
- **ZDI-CAN:** ZDI-CAN-5263
- **Date:** 2017-12-20
- **CVE:** CVE-2017-17030
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** QNAP
- **Affected Products:** QTS
- **Credit:** Peter Andersson (@nervoir)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-1005/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of QNAP QTS. Authentication is not required to exploit this vulnerability. The specific flaw exists within authLogin.cgi. When parsing the Host header, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/nas-201712-15

## Disclosure Timeline

- 2017-10-09 - Vulnerability reported to vendor
- 2017-12-20 - Coordinated public release of advisory
