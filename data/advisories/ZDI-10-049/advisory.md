# ZDI-10-049: Mozilla Firefox PluginArray nsMimeType Dangling Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-049
- **ZDI-CAN:** ZDI-CAN-655
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0177
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.5.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-049/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that a user must be coerced to viewing a malicious document. The specific flaw exists within the way the application implements the window.navigator.plugins array. Due to the application freeing the contents of the array while a reference to one of the elements is still being used, an attacker can utilize the free reference to call arbitrary code. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-19.html

## Disclosure Timeline

- 2010-01-06 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
