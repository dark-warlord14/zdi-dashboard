# ZDI-17-913: Microsoft Chakra Spread Operator Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-913
- **ZDI-CAN:** ZDI-CAN-4912
- **Date:** 2017-11-20
- **CVE:** CVE-2017-8595
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-913/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the JavaScript spread operator. By performing actions in JavaScript, an attacker can trigger an overflow of a stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8595

## Disclosure Timeline

- 2017-06-22 - Vulnerability reported to vendor
- 2017-11-20 - Coordinated public release of advisory
