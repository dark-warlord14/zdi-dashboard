# ZDI-12-021: Adobe Reader BMP Resource Signedness Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-021
- **ZDI-CAN:** ZDI-CAN-1426
- **Date:** 2012-02-08
- **CVE:** CVE-2011-4373
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Alin Rad Pop
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-021/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within 2d.x3d, which is Adobe Reader's code responsible for processing BMP files. When passing a negative size parameter in the 'colors' field, a series of signed comparisons will be averted, and the overly large size parameter is passed to a memcpy(). This will cause a heap-based buffer overflow, allowing an attacker to execute code under the context of the user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb12-01.html

## Disclosure Timeline

- 2011-10-28 - Vulnerability reported to vendor
- 2012-02-08 - Coordinated public release of advisory
