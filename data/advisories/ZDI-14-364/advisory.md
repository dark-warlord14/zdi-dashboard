# ZDI-14-364: Panasonic Network Camera View GetImageDataPrint Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-364
- **ZDI-CAN:** ZDI-CAN-2357
- **Date:** 2014-10-14
- **CVE:** CVE-2014-8755
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Panasonic
- **Affected Products:** Network Camera View
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-364/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Panasonic Network Camera View. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the GetImageDataPrint method of the WebVideoCam ActiveX control. The issue lies in the ability to nullify an arbitrary address in memory. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Panasonic has issued an update to correct this vulnerability. More details can be found at: http://security.panasonic.com/pss/security/library/howto_update_NCV.html

## Disclosure Timeline

- 2014-06-09 - Vulnerability reported to vendor
- 2014-10-14 - Coordinated public release of advisory
