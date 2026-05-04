# ZDI-17-281: (Pwn2Own) Adobe Reader DC util streamFromString Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-281
- **ZDI-CAN:** ZDI-CAN-4588
- **Date:** 2017-08-01
- **CVE:** CVE-2017-3056
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** willj from Tencent PC Manager
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-281/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the util.streamFromString method. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-11.html

## Disclosure Timeline

- 2017-03-19 - Vulnerability reported to vendor
- 2017-08-01 - Coordinated public release of advisory
