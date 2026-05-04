# ZDI-14-128: Adobe Reader AcroPDF messageHandler Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-128
- **ZDI-CAN:** ZDI-CAN-2001
- **Date:** 2014-05-13
- **CVE:** CVE-2014-0527
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** chkr_d591
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-128/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the AcroPDF ActiveX control. The issue lies in the messageHandler property of the control. By manipulating the messageHandler's attributes an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://helpx.adobe.com/security/products/reader/apsb14-15.html

## Disclosure Timeline

- 2013-10-23 - Vulnerability reported to vendor
- 2014-05-13 - Coordinated public release of advisory
