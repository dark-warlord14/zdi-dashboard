# ZDI-15-600: Microsoft Windows JScript External Object Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-600
- **ZDI-CAN:** ZDI-CAN-3335
- **Date:** 2015-12-08
- **CVE:** CVE-2015-6134
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-600/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code in applications using the JScript scripting language on vulnerable installations of Microsoft Windows. Microsoft Internet Explorer is an affected application. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw relates to how JScript handles external objects that also serve as callable objects within script. An "external object" is an object that is provided by the hosting application, as opposed to being provided by the script engine. Through the use of certain script methods, an attacker can cause JScript to use an integer as if it were a pointer to a callable object. An attacker can leverage this to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-124.aspx

## Disclosure Timeline

- 2015-10-08 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
