# ZDI-17-172: Microsoft Windows JavaScript Spread Operator Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-172
- **ZDI-CAN:** ZDI-CAN-4430
- **Date:** 2017-03-21
- **CVE:** CVE-2017-0015
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-172/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the JavaScript spread operator as implemented in chakra.dll. By performing actions in JavaScript, an attacker can trigger access to memory prior to initialization. An attacker can leverage this vulnerability to disclose sensitive information under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms17-007.aspx

## Disclosure Timeline

- 2017-01-10 - Vulnerability reported to vendor
- 2017-03-21 - Coordinated public release of advisory
