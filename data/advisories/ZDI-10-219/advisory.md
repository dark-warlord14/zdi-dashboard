# ZDI-10-219: Mozilla Firefox LookupGetterOrSetter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-219
- **ZDI-CAN:** ZDI-CAN-929
- **Date:** 2010-10-19
- **CVE:** CVE-2010-3183
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-219/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in js3250.dll. When a JavaObject is created and deleted, there is not a proper sanity check for the LookupGetterorSetter() function, which can result in a dangling pointer being passed to the JS_ValueToId() function. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the CURRENT user.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-67.html

## Disclosure Timeline

- 2010-09-22 - Vulnerability reported to vendor
- 2010-10-19 - Coordinated public release of advisory
