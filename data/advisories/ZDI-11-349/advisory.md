# ZDI-11-349: Adobe Shockwave NPAPI Plug-in Drag and Drop Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-349
- **ZDI-CAN:** ZDI-CAN-1114
- **Date:** 2011-12-17
- **CVE:** CVE-2011-2127
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-349/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the NPAPI version of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application manages a reference to a COM object. Upon destruction of the tab containing the plugin, the application will disable Drag and Drop functionality utilizing a method within the ole32 shared library. This will cause the application to attempt to destroy the object a second time. Under controlled circumstances, this can grant an attacker the ability to execute remote code under the context of the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-05-26 - Vulnerability reported to vendor
- 2011-12-17 - Coordinated public release of advisory
