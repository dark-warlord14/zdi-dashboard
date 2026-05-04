# ZDI-10-133: Mozilla Firefox CSS font-face Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-133
- **ZDI-CAN:** ZDI-CAN-831
- **Date:** 2010-07-20
- **CVE:** CVE-2010-2752
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** J23 (http://twitter.com/HansJ23)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-133/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within handling of references to external font resources. A value is used as a 16 bit integer in an array allocation and later as 32 bit when iterating over and then populating these fields. By creating enough references, a remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-39.html

## Disclosure Timeline

- 2010-06-23 - Vulnerability reported to vendor
- 2010-07-20 - Coordinated public release of advisory
