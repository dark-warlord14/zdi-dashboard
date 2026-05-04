# ZDI-15-029: Microsoft Internet Explorer UnitValueProperty Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-029
- **ZDI-CAN:** ZDI-CAN-2628
- **Date:** 2015-02-10
- **CVE:** CVE-2015-0053
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-029/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer handles certain properties of DOM objects. By performing certain actions in script an attacker can cause a property to have an invalid value. When Internet Explorer attempts to read back the property's value, Internet Explorer uses an uninitialized value in memory as a pointer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-009

## Disclosure Timeline

- 2014-11-19 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
