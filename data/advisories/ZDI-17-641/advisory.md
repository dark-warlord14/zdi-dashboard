# ZDI-17-641: Microsoft Chakra eval Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-641
- **ZDI-CAN:** ZDI-CAN-4826
- **Date:** 2017-08-08
- **CVE:** CVE-2017-8641
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** wh1ant
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-641/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the JavaScript eval function. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8641

## Disclosure Timeline

- 2017-05-30 - Vulnerability reported to vendor
- 2017-08-08 - Coordinated public release of advisory
