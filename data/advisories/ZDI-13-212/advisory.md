# ZDI-13-212: Adobe Reader ToolButton Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-212
- **ZDI-CAN:** ZDI-CAN-1601
- **Date:** 2013-09-11
- **CVE:** CVE-2013-3346
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat
- **Credit:** Soroush Dalili
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-212/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the callbacks associated with ToolButton objects. A reference to the ToolButton object is kept when executing a callback which can lead to a use-after-free scenario if the callback removes the ToolButton object. An attacker can leverage this situation to execute code under the context of the user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb13-15.html

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-09-11 - Coordinated public release of advisory
