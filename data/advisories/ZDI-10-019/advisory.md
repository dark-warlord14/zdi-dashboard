# ZDI-10-019: Mozilla Firefox showModalDialog Cross-Domain Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-019
- **ZDI-CAN:** ZDI-CAN-535
- **Date:** 2010-02-19
- **CVE:** CVE-2009-3988
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:N
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.0.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-019/
## Vulnerability Details

This vulnerability allows remote attackers to bypass specific script execution enforcements on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the lack of cross domain policy enforcement. Through usage of the showModalDialog() JavaScript method an attacker can gather sensitive information from another website. This vulnerability can be exploited to obtain website credentials not originating from the attacking site.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-04.html

## Disclosure Timeline

- 2009-08-06 - Vulnerability reported to vendor
- 2010-02-19 - Coordinated public release of advisory
