# ZDI-15-521: Microsoft Windows VBScript Filter Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-521
- **ZDI-CAN:** ZDI-CAN-3115
- **Date:** 2015-10-13
- **CVE:** CVE-2015-6055
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-521/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code in applications using the VBScript scripting language running on vulnerable installations of Microsoft Windows. Microsoft Internet Explorer is an affected application. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to the Filter function in VBScript. By passing unexpected arguments to this function, an attacker can cause an integer to be incorrectly interpreted as a pointer to an object in memory. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-106

## Disclosure Timeline

- 2015-08-03 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
