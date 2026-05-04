# ZDI-14-327: Microsoft Internet Explorer CSS Transition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-327
- **ZDI-CAN:** ZDI-CAN-2346
- **Date:** 2014-09-25
- **CVE:** CVE-2014-4067
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** lokihardt@asrt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-327/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. By setting a "background" style property in a specific way and then performing a visual transition, an attacker can cause Internet Explorer to write beyond an allocated region of memory. An attacker can leverage this vulnerability to execute code in the context of the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://go.microsoft.com/fwlink/?LinkId=507027

## Disclosure Timeline

- 2014-05-28 - Vulnerability reported to vendor
- 2014-09-25 - Coordinated public release of advisory
