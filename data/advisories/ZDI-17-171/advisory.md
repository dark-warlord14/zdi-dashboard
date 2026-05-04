# ZDI-17-171: Microsoft Windows JavaScript Spread Operator Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-171
- **ZDI-CAN:** ZDI-CAN-4422
- **Date:** 2017-03-21
- **CVE:** CVE-2017-0032
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-171/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the JavaScript spread operator as implemented in chakra.dll. By performing actions in JavaScript, an attacker can trigger an overflow of a stack-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms17-007.aspx

## Disclosure Timeline

- 2017-01-10 - Vulnerability reported to vendor
- 2017-03-21 - Coordinated public release of advisory
