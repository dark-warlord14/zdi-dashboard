# ZDI-14-352: Microsoft Internet Explorer ConvertBitmaptoPng Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-352
- **ZDI-CAN:** ZDI-CAN-2382
- **Date:** 2014-10-14
- **CVE:** CVE-2014-4138
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-352/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. In addition, the user must allow the web page to access the clipboard when so prompted. The vulnerability relates to how Internet Explorer converts bitmap-format graphics to PNG-format graphics. A web page can define an image using SVG, which, when copied and pasted back into the document, will overflow a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-056

## Disclosure Timeline

- 2014-06-23 - Vulnerability reported to vendor
- 2014-10-14 - Coordinated public release of advisory
