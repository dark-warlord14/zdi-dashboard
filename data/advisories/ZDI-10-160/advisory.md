# ZDI-10-160: Adobe Shockwave Player Director File FFFFFF45 Record Processing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-160
- **ZDI-CAN:** ZDI-CAN-841
- **Date:** 2010-08-24
- **CVE:** CVE-2010-2871
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-160/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application's support for 3D objects. While parsing the 0xFFFFFF45 RIFF record type, the process performs arithmetic on a size value and uses the result for a heap-based allocation. By specifying a large enough value an attacker can force the integer to wrap and thus the process will under-allocate the buffer. This memory is later copied into using a different size value which results in object corruption that can be leveraged to execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-20.html

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-08-24 - Coordinated public release of advisory
